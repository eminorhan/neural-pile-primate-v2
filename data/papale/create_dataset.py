import argparse
import math
import h5py
import numpy as np
from datasets import Dataset


def read_mat_file(filepath):
    """
    Reads a .mat file (v7.3 or newer) and returns a dictionary of variables.

    Args:
        filepath (str): The path to the .mat file.

    Returns:
        dict: A dictionary where keys are variable names and values are NumPy arrays.
        Returns None and prints an error if the file cannot be read.
    """
    try:
        with h5py.File(filepath, 'r') as f:
            data = {}
            for k, v in f.items():
                data[k] = read_h5py_item(v)  # use helper function to handle different data types.
            return data
    except Exception as e:
        print(f"Error reading .mat file: {e}")
        return None


def read_h5py_item(item):
    """
    Helper function to recursively read h5py items and convert them to NumPy arrays.
    Handles datasets, groups, and references.
    """
    if isinstance(item, h5py.Dataset):
        return np.array(item)
    elif isinstance(item, h5py.Group):
        group_data = {}
        for k, v in item.items():
            group_data[k] = read_h5py_item(v)
        return group_data
    elif isinstance(item, h5py.Reference):
        return read_h5py_item(item.file[item])  # dereference the reference
    else:
        return item  # return the item if it's not a dataset, group, or reference.


def estimate_spike_counts(mua, threshold_sd=3.5, bin_size_ms=20):
    """
    Estimates spike counts from multiunit activity (MUA) data by detecting
    threshold crossings and binning them.

    Args:
        mua (np.ndarray): Multiunit activity data of shape (time_bins, trials, electrodes).
        threshold_sd (float): Number of standard deviations above the mean to set the threshold for spike detection.
        bin_size_ms (int): Size of the time bins in milliseconds for counting spikes.

    Returns:
        np.ndarray: Spike counts of shape (n_time_bins, trials, electrodes), where n_time_bins is the number of 20 ms bins.
    """
    time_bins, trials, electrodes = mua.shape

    # Estimate the threshold for each electrode
    thresholds = np.mean(mua, axis=0, keepdims=True) + threshold_sd * np.std(mua, axis=0, keepdims=True)

    # Detect threshold crossings (assuming a downward crossing indicates a potential spike)
    spike_mask = (mua[:-1] > thresholds) & (mua[1:] <= thresholds)

    # Find the indices of the threshold crossings
    spike_indices = np.where(spike_mask)
    spike_times = spike_indices[0]
    spike_trials = spike_indices[1]
    spike_electrodes = spike_indices[2]

    # Calculate the number of 20 ms bins
    n_bins = time_bins // bin_size_ms

    # Initialize the spike counts array
    spike_counts = np.zeros((n_bins, trials, electrodes), dtype=int)

    # Bin the spike times
    bin_assignments = spike_times // bin_size_ms

    # Populate the spike counts array
    np.add.at(spike_counts, (bin_assignments, spike_trials, spike_electrodes), 1)

    # concatenate trials and transpose
    spike_counts = spike_counts.reshape((n_bins * trials, electrodes))

    return spike_counts.T.astype(np.uint8)


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="data",type=str, help='Data directory')
    parser.add_argument('--hf_repo_name',default="eminorhan/papale",type=str, help='processed dataset will be pushed to this HF dataset repo')
    parser.add_argument('--token_count_limit',default=10_000_000, type=int, help='sessions with larger token counts than this will be split into chunks (default: 10_000_000)')
    parser.add_argument('--spike_threshold',default=3.5, type=float, help='threshold for estimating spikes (in std units)')
    parser.add_argument('--bin_size',default=20, type=int, help='bin size in units of 1 ms (default: 20)')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # lists to store results for each session
    spike_counts_list, subject_list, session_list, segment_list = [], [], [], []

    # token counter
    n_tokens = 0

    data_F = read_mat_file('THINGS_MUA_trials_F.mat')
    data_N = read_mat_file('THINGS_MUA_trials_N.mat')
    print(f"Loaded data files.")

    # ====== monkey F ======
    spike_counts_F = estimate_spike_counts(data_F["ALLMUA"], threshold_sd=args.spike_threshold, bin_size_ms=args.bin_size)
    n_tokens_F = np.prod(spike_counts_F.shape)

    # append sessions; if session data is large, divide spike_counts array into smaller chunks
    if n_tokens_F > args.token_count_limit:
        n_channels, n_time_bins = spike_counts_F.shape
        num_segments = math.ceil(n_tokens_F / args.token_count_limit)
        segment_size = math.ceil(n_time_bins / num_segments)
        print(f"Spike count shape / max: {spike_counts_F.shape} / {spike_counts_F.max()}. Dividing into {num_segments} smaller chunks ...")
        for i in range(num_segments):
            start_index = i * segment_size
            end_index = min((i + 1) * segment_size, n_time_bins)
            sub_array = spike_counts_F[:, start_index:end_index]
            spike_counts_list.append(sub_array)
            subject_list.append("monkey_F")
            session_list.append("F_0")
            segment_list.append(f"segment_{i}")
            print(f"Divided into segment_{i} with shape / max: {sub_array.shape} / {sub_array.max()}")
            n_tokens += np.prod(sub_array.shape)
    else:
        spike_counts_list.append(spike_counts_F)
        subject_list.append("monkey_F")
        session_list.append("F_0")
        segment_list.append("segment_0")  # default segment id
        print(f"Spike count shape / max: {spike_counts_F.shape} / {spike_counts_F.max()} (segment_0)")
        n_tokens += np.prod(spike_counts_F.shape)

    # ====== monkey N ======
    spike_counts_N = estimate_spike_counts(data_N["ALLMUA"], threshold_sd=args.spike_threshold, bin_size_ms=args.bin_size)
    n_tokens_N = np.prod(spike_counts_N.shape)

    # append sessions; if session data is large, divide spike_counts array into smaller chunks
    if n_tokens_N > args.token_count_limit:
        n_channels, n_time_bins = spike_counts_N.shape
        num_segments = math.ceil(n_tokens_N / args.token_count_limit)
        segment_size = math.ceil(n_time_bins / num_segments)
        print(f"Spike count shape / max: {spike_counts_N.shape} / {spike_counts_N.max()}. Dividing into {num_segments} smaller chunks ...")
        for i in range(num_segments):
            start_index = i * segment_size
            end_index = min((i + 1) * segment_size, n_time_bins)
            sub_array = spike_counts_N[:, start_index:end_index]
            spike_counts_list.append(sub_array)
            subject_list.append("monkey_N")
            session_list.append("N_0")
            segment_list.append(f"segment_{i}")
            print(f"Divided into segment_{i} with shape / max: {sub_array.shape} / {sub_array.max()}")
            n_tokens += np.prod(sub_array.shape)
    else:
        spike_counts_list.append(spike_counts_N)
        subject_list.append("monkey_N")
        session_list.append("N_0")
        segment_list.append("segment_0")  # default segment id
        print(f"Spike count shape / max: {spike_counts_N.shape} / {spike_counts_N.max()} (segment_0)")
        n_tokens += np.prod(spike_counts_N.shape)

    def gen_data():
        for a, b, c, d in zip(spike_counts_list, subject_list, session_list, segment_list):
            yield {
                "spike_counts": a,
                "subject_id": b,
                "session_id": c,
                "segment_id": d
                }
            
    ds = Dataset.from_generator(gen_data, writer_batch_size=1)
    print(f"Number of tokens in dataset: {n_tokens} tokens")
    print(f"Number of rows in dataset: {len(ds)}")

    # push all data to hub 
    ds.push_to_hub(args.hf_repo_name, max_shard_size="1GB", token=True)