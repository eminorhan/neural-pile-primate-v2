import os
import math
import argparse
import numpy as np
import scipy.io
from datasets import Dataset


def find_mat_files(root_dir):
    """
    Crawls through a directory (including subdirectories), finds all files
    that end with ".mat" and returns the full paths of all the found files in a list.

    Args:
        root_dir: The root directory to start the search from.

    Returns:
        A list of full paths to the found .mat files, or an empty list if
        no files are found or if the root directory is invalid.
        Returns None if root_dir is not a valid directory.
    """

    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' is not a valid directory.")
        return None

    mat_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".mat"):
                full_path = os.path.join(dirpath, filename)
                mat_files.append(full_path)
    return mat_files


def extract_subject_session_id(file_path):
    """
    Extracts subject and session identifier strings from a full file path.

    Args:
        file_path (str): The full file path.

    Returns:
        str: Subject identifier string.
        str: Session identifier string.
    """
    directory, filename = os.path.split(file_path)
    subdirectory = os.path.basename(directory)
    filename_without_extension, _ = os.path.splitext(filename)
    return f"{subdirectory}", f"{filename_without_extension}"


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple .mat files into a single dataset', add_help=False)
    parser.add_argument('--data_dir', default="data", type=str, help='Data directory')
    parser.add_argument('--bin_size', default=0.02, type=int, help='Bin size (ms)')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    NUM_CHANNELS = 128  # number of recorded channels in this dataset

    # get all .mat files in the sorted folder
    mat_files = find_mat_files(args.data_dir)
    print(f"Files: {mat_files}")
    print(f"Total number of files: {len(mat_files)}")

    neurons = []
    times = []

    for file_path in sorted(mat_files):
        print(f"Processing file: {file_path}")
        mat_data = scipy.io.loadmat(file_path)

        spike_data = []
        for i in range(NUM_CHANNELS):
            key = f'Spk_{i:03d}a_sh'
            if key in mat_data:
                spike_data.append(mat_data[key][0])
            else:
                print(f"Warning: Key {key} not found in {file_path}")
                spike_data.append(np.array([])) #append empty array if channel data is missing.

        # Find the maximum spike time to determine the number of bins
        max_time = 0
        for channel_spikes in spike_data:
            if channel_spikes.size > 0:
                max_time = max(max_time, channel_spikes.max())

        num_bins = int(np.ceil(max_time / args.bin_size))
        spike_counts = np.zeros((NUM_CHANNELS, num_bins), dtype=np.uint8)

        for channel_idx, channel_spikes in enumerate(spike_data):
            if channel_spikes.size > 0:
                bin_indices = (channel_spikes / args.bin_size).astype(int)
                bin_indices = bin_indices[bin_indices < num_bins] # Ensure indices are within bounds.
                np.add.at(spike_counts[channel_idx], bin_indices, 1)

        neurons.append(spike_counts.shape[0])
        times.append(spike_counts.shape[1])
            
    print(f"({len(neurons)}) Neurons: {neurons}")
    print(f"({len(times)}) Times: {times}")