
import argparse
import numpy as np
from scipy.io import loadmat
from datasets import Dataset


def read_mat_file(filepath):
    """
    Reads a .mat file and returns the reliable neural responses.

    Args:
        filepath (str): The path to the .mat file.

    Returns:
        dict: A dictionary where keys are variable names and values are NumPy arrays.
        Returns None and prints an error if the file cannot be read.
    """
    try:
        data = loadmat(filepath)
        return np.nan_to_num(data['neural_responses_reliable'][0,0][0])
    except Exception as e:
        print(f"Error reading .mat file: {e}")
        return None


def convert_to_spike_counts(mua_matrix):
    """
    Convert mean neural response into spike counts

    Args:
        mua_matrix (numpy.ndarray): neural activity matrix of shape (electrodes, trials, time_bins).

    Returns:
        numpy.ndarray: Concatenated binned spike count matrix of shape (electrodes, binned_time_bins * trials), dtype=uint8.
    """

    electrodes, trials, time_bins = mua_matrix.shape

    # concatenate trials
    concatenated_spikes = np.round(50 * mua_matrix.reshape((electrodes, time_bins * trials)))

    return concatenated_spikes.astype(np.uint8)


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    data_mahler = read_mat_file('data/mahler/mahler_hand_dmfc_dataset_50ms.mat')
    data_perle = read_mat_file('data/perle/perle_hand_dmfc_dataset_50ms.mat')
    print(f"Loaded data files.")

    spike_count_mat_mahler = convert_to_spike_counts(data_mahler)
    spike_count_mat_perle = convert_to_spike_counts(data_perle)

    neurons = [spike_count_mat_mahler.shape[0], spike_count_mat_perle.shape[0]]
    times = [spike_count_mat_mahler.shape[1], spike_count_mat_perle.shape[1]]

    print(f"({len(neurons)}) Neurons: {neurons}")
    print(f"({len(times)}) Times: {times}")