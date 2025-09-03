**Dataset URL:** https://dandiarchive.org/dandiset/000121

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:000121
python create_dataset.py --hf_repo_name "eminorhan/even-chen" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF repo name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for calculating spike counts (default: 20 ms).

**Token count:** 783,441,792

**HF repo:** https://huggingface.co/datasets/eminorhan/even-chen

**Recorded area & stimulus, task, or behavior:** Recordings from macaque dorsal premotor cortex (PMd) during cursor movement tasks.

**Paper URL:** https://doi.org/10.1371/journal.pcbi.1006808

```
@article{evenchen2019,
  title={Structure and variability of delay activity in premotor cortex},
  author={Even-Chen, Nir and Sheffer, Blue and Vyas, Saurabh and Ryu, Stephen I and Shenoy, Krishna V},
  journal={PLoS Computational Biology},
  volume={15},
  number={2},
  pages={e1006808},
  year={2019},
  publisher={Public Library of Science San Francisco, CA USA}
}
```

