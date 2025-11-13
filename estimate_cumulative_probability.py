import sys
from datasets import load_dataset, load_dataset_builder


DATASET_NAME = "eminorhan/neural-pile-primate-1x8"
SPLIT_NAME = "train"
PROBABILITY_COLUMN = "probability"
NUM_ROWS_TO_SUM = 131072  # number of rows from the top to sum


def calculate_cumulative_probability():
    """
    Loads the top N rows of a dataset and calculates the
    cumulative sum of their 'probability' column.
    """
    
    print(f"Loading dataset: '{DATASET_NAME}' (Split: '{SPLIT_NAME}')")

    # Use split slicing to efficiently load *only* the first NUM_ROWS_TO_SUM
    # This is much faster and more memory-efficient than loading everything.
    # This assumes the dataset is already sorted from most to least probable.
    split_slice = f"{SPLIT_NAME}[:{NUM_ROWS_TO_SUM}]"
    
    print(f"Loading slice: {split_slice}")
    
    ds = load_dataset(DATASET_NAME, split=split_slice)

    print(f"Successfully loaded {len(ds)} rows.")

    # Access the probability column
    # This returns a list of all probability values for the loaded slice
    probabilities = ds[PROBABILITY_COLUMN]

    # Calculate the cumulative sum
    cumulative_prob = sum(probabilities)

    # Load the dataset *builder* (metadata only) to fetch the total number of rows
    builder = load_dataset_builder(DATASET_NAME)           
    total_rows = builder.info.splits[SPLIT_NAME].num_examples

    print("\n" + "="*30)
    print("      Calculation Complete")
    print(f"  Dataset: {DATASET_NAME}")
    print(f"  Total rows: {total_rows:,}")
    print(f"  Rows Summed: {len(probabilities):,}")
    print(f"  Cumulative Probability: {cumulative_prob:.10f}")
    print("="*30)

if __name__ == "__main__":
    calculate_cumulative_probability()