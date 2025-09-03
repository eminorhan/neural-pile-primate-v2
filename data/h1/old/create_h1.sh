#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH --time=00:30:00
#SBATCH --job-name=create_h1
#SBATCH --output=create_h1_%A_%a.out

export HF_HOME="/vast/eo41/huggingface"
export HF_DATASETS_CACHE="/vast/eo41/huggingface"

python -u create_h1.py --data_dir "sub-HumanPitt-held-in-calib"
python -u create_h1.py --data_dir "sub-HumanPitt-held-in-minival"
python -u create_h1.py --data_dir "sub-HumanPitt-held-out-calib"

echo "Done"