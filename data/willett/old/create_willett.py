import os
import argparse
import numpy as np
from scipy.io import loadmat
from datasets import Dataset


_folder_mapping = {
    'train': 'train',
    'test': 'test',
    'validation': 'validation'
    }


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir', default='train', type=str, choices=['train', 'test', 'validation'], help='Data directory')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    files = os.listdir(args.data_dir)
    files.sort()

    # this dict is for registering the recording day across data set splits
    files_dict_for_day_id = {
        't12.2022.04.28.mat': 0, 
        't12.2022.05.05.mat': 1, 
        't12.2022.05.17.mat': 2, 
        't12.2022.05.19.mat': 3, 
        't12.2022.05.24.mat': 4, 
        't12.2022.05.26.mat': 5, 
        't12.2022.06.02.mat': 6, 
        't12.2022.06.07.mat': 7, 
        't12.2022.06.14.mat': 8, 
        't12.2022.06.16.mat': 9, 
        't12.2022.06.21.mat': 10, 
        't12.2022.06.23.mat': 11, 
        't12.2022.06.28.mat': 12, 
        't12.2022.07.05.mat': 13, 
        't12.2022.07.14.mat': 14, 
        't12.2022.07.21.mat': 15, 
        't12.2022.07.27.mat': 16, 
        't12.2022.07.29.mat': 17, 
        't12.2022.08.02.mat': 18, 
        't12.2022.08.11.mat': 19, 
        't12.2022.08.13.mat': 20, 
        't12.2022.08.18.mat': 21, 
        't12.2022.08.23.mat': 22, 
        't12.2022.08.25.mat': 23
        }
    
    file_idx = 0
    sentence, spike_power, tx1, tx2, tx3, tx4, block_id, day_id = [], [], [], [], [], [], [], []  # all data to be saved

    for file in files:
        if file.endswith('.mat'):
            file_path = os.path.join(args.data_dir, file)
            data = loadmat(file_path)
            sentence.append(data['sentenceText'])
            spike_power.append(data['spikePow'].squeeze())
            tx1.append(data['tx1'].squeeze())
            tx2.append(data['tx2'].squeeze())
            tx3.append(data['tx3'].squeeze())
            tx4.append(data['tx4'].squeeze())
            block_id.append(data['blockIdx'].squeeze())
            day_id.append(files_dict_for_day_id[file] * np.ones(data['blockIdx'].squeeze().shape, dtype=np.uint8))  # TODO: add error handling here
            print('File idx, path, n_trials:', file_idx, file_path, data['blockIdx'].squeeze().shape)
            file_idx += 1

    sentence = np.concatenate(sentence)
    spike_power = np.concatenate(spike_power)
    tx1 = np.concatenate(tx1)
    tx2 = np.concatenate(tx2)
    tx3 = np.concatenate(tx3)
    tx4 = np.concatenate(tx4)
    block_id = np.concatenate(block_id)
    day_id = np.concatenate(day_id)

    def gen_data():
        for a, b, c, d, e, f, g, h in zip(sentence, spike_power, tx1, tx2, tx3, tx4, block_id, day_id):
            yield {
                "sentence": a,
                "spike_power": b,
                "tx1": c,
                "tx2": d,
                "tx3": e,
                "tx4": f,
                "block_id": g,
                "day_id": h
                }

    ds = Dataset.from_generator(gen_data)
        
    # push data to hub
    ds.push_to_hub("eminorhan/willett", split=_folder_mapping[os.path.basename(args.data_dir)], token=True)

