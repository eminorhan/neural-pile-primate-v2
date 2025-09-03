#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH --time=00:10:00
#SBATCH --job-name=create_willett
#SBATCH --output=create_willett_%A_%a.out

export HF_HOME="/vast/eo41/huggingface"
export HF_DATASETS_CACHE="/vast/eo41/huggingface"

python -u create_willett.py --data_dir "train"
python -u create_willett.py --data_dir "test"
python -u create_willett.py --data_dir "validation"

echo "Done"