import os
import argparse
import numpy as np
from pynwb import NWBHDF5IO
from datasets import Dataset


_folder_mapping = {
    'sub-Han': 'traintest',
    }


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="sub-Han",type=str, choices=["sub-Han"], help='Data directory')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .nwb files in the sorted folder
    nwb_files = [f for f in sorted(os.listdir(args.data_dir)) if f.endswith('.nwb')]
    print(f"Files: {nwb_files}")

    # lists to store results for each session
    spike_counts_list, identifier_list = [], []

    for file_name in nwb_files:
        file_path = os.path.join(args.data_dir, file_name)
        with NWBHDF5IO(file_path, "r") as io:
            nwbfile = io.read()

            # # behavior - train only (not extracting these for now)
            # force = nwbfile.processing['behavior']['force'].data[:]
            # hand_pos = nwbfile.processing['behavior']['hand_pos'].data[:]
            # hand_vel = nwbfile.processing['behavior']['hand_vel'].data[:]
            # joint_ang = nwbfile.processing['behavior']['joint_ang'].data[:]
            # joint_vel = nwbfile.processing['behavior']['joint_vel'].data[:]
            # muscle_len = nwbfile.processing['behavior']['muscle_len'].data[:]
            # muscle_vel = nwbfile.processing['behavior']['muscle_vel'].data[:]

            # we will save just spike activity for now
            units = nwbfile.units.to_dataframe()
            max_time = max([u.max() for u in units['spike_times']])
            spike_counts = np.vstack([np.histogram(row, bins=np.arange(0, max_time + 0.02, 0.02))[0] for row in units['spike_times']])  # spike count matrix (nxt: n is #channels, t is time bins)

            # file identifier
            identifier = nwbfile.identifier

            # append sessions
            spike_counts_list.append(spike_counts)
            identifier_list.append(identifier)

    def gen_data():
        for a, b in zip(spike_counts_list, identifier_list):
            yield {
                "spike_counts": a,
                "identifier": b,
                }

    ds = Dataset.from_generator(gen_data)
        
    # push all data to hub under "all"
    ds.push_to_hub("eminorhan/area2-bump", _folder_mapping[os.path.basename(args.data_dir)], token=True)