from datasets import load_dataset
import numpy as np

def calculate_spike_zero_fraction_for_test_split(
    dataset_name="eminorhan/neural-bench-primate",
    split_name='test',
    num_proc=32
):
    """
    Loads the specified split of a dataset from Hugging Face Hub,
    calculates the fraction of zeros in the 'spike_counts' column for each row,
    and then computes the total fraction of zero entries across that split.

    Args:
        dataset_name (str): The name of the dataset on Hugging Face Hub.
        split_name (str): The name of the split to process (e.g., 'test', 'train').
        num_proc (int): The number of processes to use for dataset loading and processing.

    Returns:
        float: The total fraction of zero entries in 'spike_counts' across the specified split,
               or None if the dataset, split, or column is not found or in an unexpected format.
    """
    print(f"Loading dataset '{dataset_name}', split '{split_name}' with {num_proc} processes...")
    try:
        # Load only the specified split of the dataset
        ds = load_dataset(dataset_name, split=split_name, num_proc=num_proc)
    except ValueError as ve:
        print(f"Error loading dataset split: {ve}")
        print(f"Please ensure that the split '{split_name}' exists for the dataset '{dataset_name}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading the dataset: {e}")
        return None

    print(f"\nProcessing split: '{split_name}'")

    if 'spike_counts' not in ds.column_names:
        print(f"Column 'spike_counts' not found in split '{split_name}'.")
        return None

    # Using dataset.map() for potentially better performance.
    print("Processing rows using map()...")

    def get_counts_per_example(example):
        """Processes a single example to count zeros and total elements."""
        # Ensure 'spike_counts' is present and is array-like
        if example['spike_counts'] is None:
            return {'num_zeros': 0, 'num_elements': 0}
        
        spike_counts_array = np.array(example['spike_counts'], dtype=np.uint8) # Specify dtype for consistency
        
        # Handle cases where spike_counts_array might be empty or not as expected
        if spike_counts_array.ndim == 0: # If it's a scalar after conversion
             num_zeros = 1 if spike_counts_array == 0 else 0
             num_elements = 1
        elif spike_counts_array.size == 0: # If it's an empty array
            num_zeros = 0
            num_elements = 0
        else:
            num_zeros = np.sum(spike_counts_array == 0)
            num_elements = spike_counts_array.size
            
        return {
            'num_zeros': num_zeros,
            'num_elements': num_elements
        }

    try:
        processed_ds = ds.map(
            get_counts_per_example,
            num_proc=num_proc
        )
    except Exception as e:
        print(f"Error during the .map() operation: {e}")
        return None

    # Now sum up the counts from the processed dataset
    total_zeros = sum(processed_ds['num_zeros'])
    total_elements = sum(processed_ds['num_elements'])

    if total_elements == 0:
        print("\nNo 'spike_counts' data processed or all arrays were empty in the 'test' split.")
        return None

    overall_fraction_zeros = total_zeros / total_elements
    print(f"\nSplit '{split_name}': Found {total_zeros} zeros out of {total_elements} total elements.")
    print(f"Total fraction of zero entries in 'spike_counts' for split '{split_name}': {overall_fraction_zeros:.6f}")

    return overall_fraction_zeros

if __name__ == '__main__':
    # Get the current date to show the information is up-to-date
    from datetime import datetime
    current_date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Analysis run on: {current_date_str}")

    # Example usage for the 'test' split:
    # Adjust num_proc based on your CPU cores (e.g., 4, 8, 16, or 32 as in your example)
    # Using a lower num_proc for local testing if 32 is too high for your machine.
    num_processes = 32 # Feel free to change this back to 32
    
    fraction = calculate_spike_zero_fraction_for_test_split(
        dataset_name="eminorhan/neural-bench-primate",
        split_name='train',
        num_proc=num_processes
    )

    if fraction is not None:
        print(f"\nFinal calculated fraction of zeros for the 'test' split: {fraction:.6f}")
    else:
        print("\nCould not calculate the fraction of zeros.")