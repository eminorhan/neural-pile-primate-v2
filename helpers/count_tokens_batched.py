import numpy as np
from datasets import load_dataset
import concurrent.futures
import os
import time

# Global variable to hold the dataset.
# Loaded in the main process and accessed by index in worker processes.
# We rely on the datasets library and multiprocessing to handle
# access to this object from different processes.
ds = None

def count_tokens_for_indices(indices_chunk):
    """
    Worker function to count tokens for a given chunk of indices.
    Accesses the global 'ds' dataset object using the provided indices.
    """
    global ds # Declare ds as global to access the dataset loaded in the main process

    local_token_counts = np.zeros(256, dtype=int)

    # Iterate through the indices assigned to this worker
    for i in indices_chunk:
        try:
            # Access the dataset row directly using the index
            row = ds[int(i)] # Ensure index is an integer
            spike_counts_array = np.array(row["spike_counts"]).flatten()
            # Use np.bincount to count occurrences of each token (0-255)
            counts_in_row = np.bincount(spike_counts_array, minlength=256)
            # Accumulate the counts in the local counter for this worker
            local_token_counts += counts_in_row
        except Exception as e:
            # Handle potential errors during processing of a specific index/row
            print(f"Error processing index {i} in worker {os.getpid()}: {e}")
            # Depending on your needs, you might want to log this error
            # or handle it differently. For now, we skip the problematic row.
            pass

    return local_token_counts # Return the accumulated counts for this chunk

if __name__ == "__main__":
    print("Loading dataset...")
    load_start_time = time.time()
    # Load the dataset in the main process. This dataset object will be
    # accessed by the worker processes using indices.
    # We remove num_proc here as we are managing the parallelization
    # of the counting loop explicitly.
    ds = load_dataset("eminorhan/neural-bench-rodent", split="train")
    load_end_time = time.time()
    print(f"Dataset loaded in {load_end_time - load_start_time:.2f} seconds.")

    print("Starting parallel token counting using index distribution...")
    count_start_time = time.time()

    total_rows = len(ds)
    # Determine the number of worker processes to use.
    # Using os.cpu_count() is a good default, but capping it can be beneficial
    # to avoid excessive process creation overhead and resource contention.
    num_processes = os.cpu_count() # adjust as needed
    print(f"Using {num_processes} processes for counting.")

    # Create chunks of indices. Instead of extracting data, we just divide
    # the range of row indices into chunks.
    all_indices = np.arange(total_rows)
    # Determine the size of each index chunk. We aim for multiple chunks
    # per process to help with load balancing.
    index_chunk_size = max(1, total_rows // (num_processes * 10)) # Aim for ~10 chunks per process initially

    index_chunks = []
    # Create the list of index chunks
    for i in range(0, total_rows, index_chunk_size):
        index_chunks.append(all_indices[i:i + index_chunk_size])

    print(f"Created {len(index_chunks)} index chunks (approx {index_chunk_size} indices per chunk).")

    # Initialize the final token counter array in the main process.
    # This array will accumulate counts from all worker processes.
    final_token_counts = np.zeros(256, dtype=int)

    # Use concurrent.futures.ProcessPoolExecutor to manage the pool of worker processes.
    # The context manager handles the creation and termination of the worker pool.
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        # Submit the count_tokens_for_indices function for each chunk of indices
        # to the process pool. Store the returned Future objects, which represent
        # the pending results. We map futures to the number of rows they represent
        # for progress reporting.
        futures = {executor.submit(count_tokens_for_indices, chunk): len(chunk) for chunk in index_chunks}

        # Aggregate results as the futures complete.
        # as_completed yields futures as they finish, allowing us to process results
        # without waiting for all futures to complete in submission order.
        print("Aggregating results as chunks complete...")
        processed_chunks_count = 0
        processed_rows_count = 0
        total_chunks = len(index_chunks)

        for future in concurrent.futures.as_completed(futures):
            # Get the number of rows for the completed chunk from our futures dictionary
            chunk_rows = futures[future]
            try:
                # Get the result (the partial token counts) from the completed future
                partial_counts = future.result()
                # Add the partial counts from the worker to the final counts in the main process
                final_token_counts += partial_counts

                processed_chunks_count += 1
                processed_rows_count += chunk_rows

                # Print progress periodically or when all chunks are processed
                if processed_chunks_count % max(1, total_chunks // 10) == 0 or processed_chunks_count == total_chunks:
                     print(f"Processed {processed_chunks_count}/{total_chunks} chunks ({processed_rows_count}/{total_rows} rows)...")
            except Exception as exc:
                # Catch and report exceptions that occur in worker processes
                print(f'A chunk processing generated an exception: {exc}')

    count_end_time = time.time()
    print(f"\nToken counting complete in {count_end_time - count_start_time:.2f} seconds.")
    print(f"Total execution time (including loading): {count_end_time - load_start_time:.2f} seconds.")

    # Print the final aggregated token counts
    print("\nFinal Token Counts:")
    for token, count in enumerate(final_token_counts):
        print(f"Token {token}: {count} occurrences")

    # Save the final counts to a numpy file
    np.save("token_counts_rodent.npy", final_token_counts)
    print("\nToken counts saved to token_counts_rodent.npy")