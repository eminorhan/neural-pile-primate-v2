import numpy as np
from datasets import load_dataset

# Load the dataset
ds = load_dataset("eminorhan/neural-bench-primate", split="train", num_proc=32)

# Initialize a counter for tokens from 0 to 255
token_counts = np.zeros(256, dtype=int)

# Iterate over the dataset and update token counts
counter = 0
for row in ds:
    spike_counts_array = row["spike_counts"]
    counts_in_row = np.bincount(np.array(spike_counts_array).flatten(), minlength=256)
    token_counts += counts_in_row
    counter += 1
    print(f"{counter} of {len(ds)}")

# print the counts
for token, count in enumerate(token_counts):
    print(f"Token {token}: {count} occurrences")

np.save("token_counts_primate.npy", token_counts)

# access the count of a specific token, e.g., token 10:
# print(f"Occurrences of token 10: {token_counts[10]}")