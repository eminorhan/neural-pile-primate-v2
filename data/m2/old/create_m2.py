import os
import argparse
import numpy as np
from pynwb import NWBHDF5IO
from datasets import Dataset


_folder_mapping = {
    'sub-MonkeyN-held-in-calib': 'in-calib',
    'sub-MonkeyN-held-in-minival': 'in-minival',
    'sub-MonkeyN-held-out-calib': 'out-calib'
    }


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="sub-MonkeyN-held-in-calib",type=str, choices=["sub-MonkeyN-held-in-calib", "sub-MonkeyN-held-in-minival", "sub-MonkeyN-held-out-calib"], help='Data directory')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .nwb files in the sorted folder
    nwb_files = [f for f in sorted(os.listdir(args.data_dir)) if f.endswith('.nwb')]
    print(f"Files: {nwb_files}")

    # lists to store results for each session
    vel_data_list, labels_list, time_stamps_list, spike_counts_list, eval_mask_list, identifier_list = [], [], [], [], [], []

    for file_name in nwb_files:
        file_path = os.path.join(args.data_dir, file_name)
        with NWBHDF5IO(file_path, "r") as io:
            nwbfile = io.read()

            # finger velocity traces
            vel_container = nwbfile.acquisition['finger_vel']
            labels = [ts for ts in vel_container.time_series]
            vel_data = []
            vel_timestamps = None
            for ts in labels: 
                ts_data = vel_container.get_timeseries(ts)
                vel_data.append(ts_data.data[:])
                vel_timestamps = ts_data.timestamps[:]
            vel_data = np.vstack(vel_data).T

            # spike activity
            units = nwbfile.units.to_dataframe()
            spike_counts = np.vstack([np.histogram(row, bins=np.append(vel_timestamps, vel_timestamps[-1] + 0.02))[0] for row in units['spike_times']])  # spike count matrix (nxt: n is #channels, t is time bins)

            # eval mask
            eval_mask = nwbfile.acquisition['eval_mask'].data[:].astype(bool)

            # file identifier
            identifier = nwbfile.identifier

            # append sessions
            vel_data_list.append(vel_data)
            labels_list.append(labels)
            time_stamps_list.append(vel_timestamps)
            spike_counts_list.append(spike_counts)
            eval_mask_list.append(eval_mask)
            identifier_list.append(identifier)

    def gen_data():
        for a, b, c, d, e, f in zip(vel_data_list, labels_list, time_stamps_list, spike_counts_list, eval_mask_list, identifier_list):
            yield {
                "vel_data": a,
                "labels": b,
                "time_stamps": c,
                "spike_counts": d,
                "eval_mask": e,
                "identifier": f,
                }

    ds = Dataset.from_generator(gen_data)
        
    # push all data to hub under "all"
    ds.push_to_hub("eminorhan/m2", _folder_mapping[os.path.basename(args.data_dir)], token=True)
