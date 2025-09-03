import os
import argparse
import numpy as np
from pynwb import NWBHDF5IO
from datasets import Dataset


_folder_mapping = {
    'sub-T5-held-in-calib': 'in-calib',
    'sub-T5-held-in-minival': 'in-minival',
    'sub-T5-held-out-calib': 'out-calib'
    }


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="sub-T5-held-in-calib",type=str, choices=["sub-T5-held-in-calib", "sub-T5-held-in-minival", "sub-T5-held-out-calib"], help='Data directory')
    return parser


def find_indices(time_stamps, start_times, stop_times):
    # find the index of the closest time point in time_stamps
    def find_closest(time_points, target_time):
        # index of the closest time point in time_stamps
        return np.argmin(np.abs(np.array(time_points) - target_time))
    
    # indices for start_times
    start_indices = [find_closest(time_stamps, start_time) for start_time in start_times]
    
    # indices for stop_times
    stop_indices = [find_closest(time_stamps, stop_time) for stop_time in stop_times]
    
    return start_indices, stop_indices


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .nwb files in the sorted folder
    nwb_files = [f for f in sorted(os.listdir(args.data_dir)) if f.endswith('.nwb')]
    print(f"Files: {nwb_files}")

    # lists to store results for each session
    block_nums_list, sentences_list, eval_mask_list, time_stamps_list, spike_counts_list, spike_counts_slices_list, identifier_list = [], [], [], [], [], [], []

    for file_name in nwb_files:
        file_path = os.path.join(args.data_dir, file_name)
        with NWBHDF5IO(file_path, "r") as io:
            nwbfile = io.read()
            trials = nwbfile.intervals['trials']
            block_nums = nwbfile.intervals['trials']['block_num'].data[:]
            sentences = nwbfile.intervals['trials']['cue'].data[:]
            sentences = [s.replace('>', ' ').replace('~', '.') for s in sentences]
            start_times = nwbfile.intervals['trials']['start_time'].data[:]
            stop_times = nwbfile.intervals['trials']['stop_time'].data[:]
            eval_mask = nwbfile.acquisition['eval_mask'].data[:].astype(bool)
            spike_counts = nwbfile.acquisition['binned_spikes'].data[:]
            time_stamps = nwbfile.acquisition['binned_spikes'].timestamps[:]
            start_indices, stop_indices = find_indices(time_stamps, start_times, stop_times)
            spike_counts_slices = [spike_counts[start_index:stop_index, :] for start_index, stop_index in zip(start_indices, stop_indices)]
            identifier = nwbfile.identifier

            # append trials
            block_nums_list.append(block_nums)
            sentences_list.append(sentences)
            eval_mask_list.append(eval_mask)
            time_stamps_list.append(time_stamps)
            spike_counts_list.append(spike_counts)
            spike_counts_slices_list.append(spike_counts_slices)
            identifier_list.append(identifier)

    def gen_data():
        for a, b, c, d, e, f, g in zip(block_nums_list, sentences_list, eval_mask_list, time_stamps_list, spike_counts_list, spike_counts_slices_list, identifier_list):
            yield {
                "block_nums": a,
                "sentences": b,
                "eval_mask": c,
                "time_stamps": d,
                "spike_counts": e,
                "spike_counts_slices": f,
                "identifier": g
                }

    ds = Dataset.from_generator(gen_data)
        
    # push data to hub
    ds.push_to_hub("eminorhan/h2", _folder_mapping[os.path.basename(args.data_dir)], token=True)
