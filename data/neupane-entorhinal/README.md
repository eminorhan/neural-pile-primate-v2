**Dataset URL:** https://dandiarchive.org/dandiset/000897

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:000897
python create_dataset.py --hf_repo_name "eminorhan/neupane-entorhinal" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 911,393,376 

**HF repo:** https://huggingface.co/datasets/eminorhan/neupane-entorhinal

**Recorded area & stimulus, task, or behavior:** Recordings from macaque entorhinal cortex during a mental navigation task.

**Paper URL:** https://www.nature.com/articles/s41586-024-07557-z

```
@article{neupane2024,
  title={Mental navigation in the primate entorhinal cortex},
  author={Neupane, Sujaya and Fiete, Ila and Jazayeri, Mehrdad},
  journal={Nature},
  volume={630},
  number={8017},
  pages={704--711},
  year={2024},
  publisher={Nature Publishing Group UK London}
}
```