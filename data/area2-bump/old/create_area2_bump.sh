#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH --time=00:10:00
#SBATCH --job-name=create_area2_bump
#SBATCH --output=create_area2_bump_%A_%a.out

export HF_HOME="/vast/eo41/huggingface"
export HF_DATASETS_CACHE="/vast/eo41/huggingface"

python -u create_area2_bump.py --data_dir "sub-Han"

echo "Done"