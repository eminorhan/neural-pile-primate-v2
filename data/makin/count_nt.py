import os
import math
import h5py
import argparse
import numpy as np
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
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="data",type=str, help='Data directory')
    parser.add_argument('--bin_size',default=0.02, type=float, help='time bin size (in seconds) for calculating spike counts (default: 0.02)')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .mat files in the sorted folder
    mat_files = find_mat_files(args.data_dir)
    print(f"Files: {mat_files}")
    print(f"Total number of files: {len(mat_files)}")

    neurons = []
    times = []

    for file_path in sorted(mat_files):
        print(f"Processing file: {file_path}")
        with h5py.File(file_path, "r") as f:
            data = f['spikes']
            u, n = data.shape
            all_channels = []
            for i_n in range(n):
                spike_times = []
                for i_u in range(u):
                    group = f['spikes'][i_u, i_n]
                    obj = f[group][()]
                    if obj.ndim == 2:
                        spike_times.append(obj.flatten())
                if spike_times != []:
                    spike_times = np.concatenate(spike_times)
                all_channels.append(spike_times)

            max_time = max([-np.inf if isinstance(u, list) else u.max() for u in all_channels])
            min_time = min([np.inf if isinstance(u, list) else u.min() for u in all_channels])

            spike_counts = np.vstack([np.histogram(row, bins=np.arange(min_time, max_time + args.bin_size, args.bin_size))[0] for row in all_channels]).astype(np.uint8)  # spike count matrix (nxt: n is #channels, t is time bins)

            neurons.append(spike_counts.shape[0])
            times.append(spike_counts.shape[1])
            
    print(f"({len(neurons)}) Neurons: {neurons}")
    print(f"({len(times)}) Times: {times}")