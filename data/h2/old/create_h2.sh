#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH --time=00:30:00
#SBATCH --job-name=create_h2
#SBATCH --output=create_h2_%A_%a.out

export HF_HOME="/vast/eo41/huggingface"
export HF_DATASETS_CACHE="/vast/eo41/huggingface"

python -u create_h2.py --data_dir "sub-T5-held-in-calib"
python -u create_h2.py --data_dir "sub-T5-held-in-minival"
python -u create_h2.py --data_dir "sub-T5-held-out-calib"

echo "Done"