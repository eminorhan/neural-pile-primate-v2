import os
import argparse
import numpy as np
from scipy.io import loadmat
from datasets import Dataset

def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--save_str', default='test', type=str, help='String identifier for file to be saved')
    parser.add_argument('--data_dir', default='test', type=str, help='Data directory')
    return parser

if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    files = os.listdir(args.data_dir)
    files.sort()

    # this dict is for registering the recording day across data set splits
    files_dict_for_day_id = {
        't5.2022.05.18.mat': 0, 
        't5.2022.05.23.mat': 1, 
        't5.2022.05.25.mat': 2, 
        't5.2022.06.01.mat': 3, 
        't5.2022.06.03.mat': 4, 
        't5.2022.06.06.mat': 5, 
        't5.2022.06.08.mat': 6, 
        't5.2022.06.13.mat': 7, 
        't5.2022.06.15.mat': 8, 
        't5.2022.06.22.mat': 9, 
        't5.2022.09.01.mat': 10,
        't5.2022.09.29_n.mat': 11,
        't5.2022.09.29_r.mat': 11,
        't5.2022.10.06_n.mat': 12,
        't5.2022.10.06_r.mat': 12,
        't5.2022.10.18_n.mat': 13,
        't5.2022.10.18_r.mat': 13,
        't5.2022.10.25_n.mat': 14,
        't5.2022.10.25_r.mat': 14,
        't5.2022.10.27_n.mat': 15,
        't5.2022.10.27_r.mat': 15,
        't5.2022.11.01_n.mat': 16,
        't5.2022.11.01_r.mat': 16,
        't5.2022.11.03_n.mat': 17,
        't5.2022.11.03_r.mat': 17,
        't5.2022.12.08_n.mat': 18,
        't5.2022.12.08_r.mat': 18,
        't5.2022.12.15_n.mat': 19,
        't5.2022.12.15_r.mat': 19,
        't5.2023.02.28_n.mat': 20,
        't5.2023.02.28_r.mat': 20
        }
    
    file_idx = 0
    sentences, tx_feats, block_ids, day_ids = [], [], [], []  # all data to be saved

    for file in files:
        if file.endswith('.mat'):
            file_path = os.path.join(args.data_dir, file)
            data = loadmat(file_path)
            sentences.append(data['sentences'].squeeze())
            tx_feats.append(data['tx_feats'].squeeze())
            block_ids.append(data['blocks'].squeeze())
            day_ids.append(files_dict_for_day_id[file] * np.ones(data['blocks'].squeeze().shape, dtype=np.uint8))  # TODO: add error handling here
            print('File idx, path, n_trials:', file_idx, file_path, data['blocks'].squeeze().shape)
            file_idx += 1

    sentences = np.concatenate(sentences)
    tx_feats = np.concatenate(tx_feats)
    block_ids = np.concatenate(block_ids)
    day_ids = np.concatenate(day_ids)

    def gen_data():
        for a, b, c, d in zip(sentences, tx_feats, block_ids, day_ids):
            yield {
                "sentence": a[0].replace('>', ' ').replace('~', '.'),
                "tx_feat": b.astype(np.uint8),
                "block_id": c[0][0],
                "day_id": d
                }

    ds = Dataset.from_generator(gen_data)
        
    # push all data to hub under "all"
    ds.push_to_hub("eminorhan/h2", split=args.save_str, token=True)