import os
import math
import argparse
import numpy as np
from pynwb import NWBHDF5IO
from datasets import Dataset


def find_nwb_files(root_dir):
    """
    Crawls through a directory (including subdirectories), finds all files
    that end with ".nwb", but not with "_image.nwb" or "_behavior.nwb", and
    returns the full paths of all the found files in a list.

    Args:
        root_dir: The root directory to start the search from.

    Returns:
        A list of full paths to the found .nwb files, or an empty list if
        no files are found or if the root directory is invalid.
        Returns None if root_dir is not a valid directory.
    """

    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' is not a valid directory.")
        return None

    nwb_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".nwb") and not (filename.endswith("_image.nwb") or filename.endswith("_behavior.nwb")):
                full_path = os.path.join(dirpath, filename)
                nwb_files.append(full_path)
    return nwb_files


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


def rebin_counts(X, bin_size_ms=20):
    """
    Re-bins count data into larger time bins.

    Args:
        X: A NumPy array of shape (t, n) where t is the number of 1ms time bins
           and n is the number of events in each bin.
        bin_size_ms: The desired size of the new time bins in milliseconds.

    Returns:
        A NumPy array of shape (t_new, n) where t_new is the number of new time bins.
        Returns None if input array is invalid or bin size is not positive.
    """

    if not isinstance(X, np.ndarray) or X.ndim != 2 or X.shape[0] == 0 or X.shape[1] == 0:
      print("Invalid input array. Must be a 2D numpy array with non-zero dimensions.")
      return None

    if bin_size_ms <= 0 or not isinstance(bin_size_ms, int):
        print("Bin size must be a positive integer.")
        return None

    t, n = X.shape
    t_new = t // bin_size_ms  # Integer division to get the number of new bins

    if t_new == 0:
        print("The new bin size is larger than the total time duration, resulting in 0 bins.")
        return np.zeros((0, n), dtype=X.dtype)

    X_binned = np.zeros((t_new, n), dtype=X.dtype)  # Initialize the binned array

    for i in range(t_new):
        start_index = i * bin_size_ms
        end_index = (i + 1) * bin_size_ms
        X_binned[i, :] = np.sum(X[start_index:end_index, :], axis=0)

    return X_binned


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="data",type=str, help='Data directory')
    parser.add_argument('--bin_size',default=20, type=int, help='bin size in units of 1 ms (default: 20)')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .nwb files in the sorted folder
    nwb_files = find_nwb_files(args.data_dir)
    print(f"Files: {nwb_files}")
    print(f"Total number of files: {len(nwb_files)}")

    neurons = []
    times = []

    for file_path in sorted(nwb_files):
        print(f"Processing file: {file_path}")
        with NWBHDF5IO(file_path, "r") as io:
            nwbfile = io.read()

            rasters = nwbfile.processing['ecephys'].data_interfaces['rasters'].data[:]
            spike_counts = rebin_counts(rasters, bin_size_ms=args.bin_size).T.astype(np.uint8)  # re-bin rasters into 20 ms windows & transpose

            neurons.append(spike_counts.shape[0])
            times.append(spike_counts.shape[1])

    print(f"({len(neurons)}) Neurons: {neurons}")
    print(f"({len(times)}) Times: {times}")