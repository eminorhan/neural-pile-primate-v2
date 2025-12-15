import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import pdist
from datasets import load_dataset
import random

def reorder_neurons(spike_counts, method='correlation'):
    """
    Reorders neurons based on hierarchical clustering.
    Returns the sorted spike count array.
    """
    spike_counts = np.array(spike_counts)
    
    # Safety check for small arrays
    if spike_counts.shape[0] < 2:
        return spike_counts

    try:
        # Calculate distance
        dists = pdist(spike_counts, metric=method)
        # Handle NaN distances (common with silent neurons in correlation metric)
        dists = np.nan_to_num(dists, nan=2.0)
        
        # Cluster
        linkage_matrix = linkage(dists, method='ward', optimal_ordering=True)
        sorted_indices = leaves_list(linkage_matrix)
        
        return spike_counts[sorted_indices, :]
    except Exception as e:
        # Fallback if clustering fails (e.g., all zeros)
        return spike_counts

def save_comparison_grid(dataset_name, num_samples=8, output_filename='reordering_comparison.jpg'):
    """
    Loads dataset, samples n examples, plots (2, n) grid, and saves to JPG.
    """
    print(f"Loading dataset: {dataset_name}...")
    
    # 1. Load Dataset (If you have the object locally, pass it directly instead of loading)
    ds = load_dataset(dataset_name, split='train')

    # 2. Sample random indices
    total_rows = len(ds)
    # ensure we don't try to sample more than exist
    sample_indices = random.sample(range(total_rows), min(num_samples, total_rows))
    
    print(f"Processing indices: {sample_indices}")

    # 3. Setup Figure (Wide aspect ratio for 10 columns)
    fig, axes = plt.subplots(2, num_samples, figsize=(24, 6))
    
    # Adjust spacing
    plt.subplots_adjust(wspace=0.1, hspace=0.1)

    # 4. Loop through samples
    for i, idx in enumerate(sample_indices):
        # Extract data
        raw_data = np.array(ds[idx]['spike_counts'])
        sorted_data = reorder_neurons(raw_data, method='cosine')

        # --- Row 1: Unsorted ---
        ax_top = axes[0, i]
        ax_top.imshow(raw_data, aspect='auto', cmap='Greys', interpolation='nearest')
        ax_top.set_xticks([]) # Remove x-ticks for cleaner look
        ax_top.set_yticks([]) # Remove y-ticks
        
        # Only add title to the top row
        ax_top.set_title(f"ID {idx}", fontsize=10)
        
        if i == 0:
            ax_top.set_ylabel("Unsorted", fontsize=14, fontweight='bold')

        # --- Row 2: Sorted ---
        ax_bot = axes[1, i]
        ax_bot.imshow(sorted_data, aspect='auto', cmap='Greys', interpolation='nearest')
        ax_bot.set_xticks([])
        ax_bot.set_yticks([])
        
        if i == 0:
            ax_bot.set_ylabel("Sorted", fontsize=14, fontweight='bold')

    # 5. Save
    print(f"Saving visualization to {output_filename}...")
    plt.savefig(output_filename, dpi=150, bbox_inches='tight')
    plt.close(fig) # Close memory reference
    print("Done.")

if __name__ == "__main__":

    HF_REPO_NAME = "eminorhan/neural-pile-primate"
    NUM_SAMPLES = 8
    OUTPUT_FILENAME = "primate_reordering_comparison.jpeg"

    save_comparison_grid(HF_REPO_NAME, num_samples=NUM_SAMPLES, output_filename=OUTPUT_FILENAME)