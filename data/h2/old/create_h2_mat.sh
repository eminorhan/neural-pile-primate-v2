#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH --time=00:10:00
#SBATCH --job-name=create_h2_mat
#SBATCH --output=create_h2_mat_%A_%a.out

python -u create_h2_mat.py --data_dir train --save_str train

echo "Done"