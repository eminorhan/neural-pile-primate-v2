**Dataset URL:** https://dandiarchive.org/dandiset/000070

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:000070
python create_dataset.py --hf_repo_name "eminorhan/churchland" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 1,278,669,504

**HF repo:** https://huggingface.co/datasets/eminorhan/churchland

**Recorded area & stimulus, task, or behavior:** Recordings from macaque motor cortex (M1) and dorsal premotor cortex (PMd) while performing reaching tasks with right hand.

**Paper URL:** https://www.nature.com/articles/nature11129

```
@article{churchland2012,
  title={Neural population dynamics during reaching},
  author={Churchland, Mark M and Cunningham, John P and Kaufman, Matthew T and Foster, Justin D and Nuyujukian, Paul and Ryu, Stephen I and Shenoy, Krishna V},
  journal={Nature},
  volume={487},
  number={7405},
  pages={51--56},
  year={2012},
  publisher={Nature Publishing Group UK London}
}
```