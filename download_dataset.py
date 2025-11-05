import numpy as np
from datasets import load_dataset

ds = load_dataset("eminorhan/neural-pile-primate", num_proc=32)
print(f"Number of data rows in train: {len(ds['train'])}")
print(f"Number of data rows in test: {len(ds['test'])}")

for i in range(9):
    spike_counts = np.array(ds['train'][i]['spike_counts'])
    print(f"Data row {i} shape: {spike_counts.shape}")

print(f"Done!")