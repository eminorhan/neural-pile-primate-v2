import os
import argparse
import numpy as np
from pynwb import NWBHDF5IO
from datasets import Dataset


_folder_mapping = {
    'sub-MonkeyX-held-in-calib': 'in-calib',
    'sub-MonkeyX-held-in-minival': 'in-minival',
    'sub-MonkeyX-held-out-calib': 'out-calib'
    }


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="sub-MonkeyX-held-in-calib",type=str, choices=["sub-MonkeyX-held-in-calib", "sub-MonkeyX-held-in-minival", "sub-MonkeyX-held-out-calib"], help='Data directory')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .nwb files in the sorted folder
    nwb_files = [f for f in sorted(os.listdir(args.data_dir)) if f.endswith('.nwb')]
    print(f"Files: {nwb_files}")

    # lists to store results for each session
    emg_data_list, time_stamps_list, spike_counts_list, eval_mask_list, identifier_list = [], [], [], [], []

    for file_name in nwb_files:
        file_path = os.path.join(args.data_dir, file_name)
        with NWBHDF5IO(file_path, "r") as io:
            nwbfile = io.read()

            # emg traces
            raw_emg = nwbfile.acquisition['preprocessed_emg']
            muscles = [ts for ts in raw_emg.time_series]
            emg_data = []
            emg_timestamps = []
            for m in muscles: 
                mdata = raw_emg.get_timeseries(m)
                data = mdata.data[:]
                timestamps = mdata.timestamps[:]
                emg_data.append(data)
                emg_timestamps.append(timestamps)

            emg_data = np.vstack(emg_data).T 
            emg_timestamps = emg_timestamps[0]

            # spike activity
            units = nwbfile.units.to_dataframe()
            spike_counts = np.vstack([np.histogram(row, bins=np.append(emg_timestamps, emg_timestamps[-1] + 0.02))[0] for row in units['spike_times']])  # spike count matrix (nxt: n is #channels, t is time bins)

            # eval mask
            eval_mask = nwbfile.acquisition['eval_mask'].data[:].astype(bool)

            # file identifier
            identifier = nwbfile.identifier

            # append sessions
            emg_data_list.append(emg_data)
            time_stamps_list.append(emg_timestamps)
            spike_counts_list.append(spike_counts)
            eval_mask_list.append(eval_mask)
            identifier_list.append(identifier)

    def gen_data():
        for a, b, c, d, e in zip(emg_data_list, time_stamps_list, spike_counts_list, eval_mask_list, identifier_list):
            yield {
                "emg_data": a,
                "time_stamps": b,
                "spike_counts": c,
                "eval_mask": d,
                "identifier": e,
                }

    ds = Dataset.from_generator(gen_data)
        
    # push all data to hub under "all"
    ds.push_to_hub("eminorhan/m1-b", _folder_mapping[os.path.basename(args.data_dir)], token=True)
