**Dataset URL:** https://dandiarchive.org/dandiset/001209

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:001209
python create_dataset.py --hf_repo_name "eminorhan/m1-b" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 43,809,344

**HF repo:** https://huggingface.co/datasets/eminorhan/m1-b

**Recorded area & stimulus, task, or behavior:** Recordings from macaque motor cortex (M1) during a center-out reach task.

**Paper URL:** https://journals.physiology.org/doi/full/10.1152/jn.00686.2015

```
@article{rouse2015,
  title={Spatiotemporal distribution of location and object effects in reach-to-grasp kinematics},
  author={Rouse, Adam G and Schieber, Marc H},
  journal={Journal of Neurophysiology},
  volume={114},
  number={6},
  pages={3268--3282},
  year={2015},
  publisher={American Physiological Society Bethesda, MD}
}
```