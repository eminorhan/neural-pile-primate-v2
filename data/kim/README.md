**Dataset URL:** https://dandiarchive.org/dandiset/001357

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:001357
python create_dataset.py --hf_repo_name "eminorhan/kim" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF repo name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for calculating spike counts (default: 20 ms).

**Token count:** 804,510,741

**HF repo:** https://huggingface.co/datasets/eminorhan/kim

**Recorded area & stimulus, task, or behavior:** Recordings from macaque V4 in response to shape and texture stimuli.

**Paper URL:** https://www.jneurosci.org/content/45/5/e1893232024

```
@article{namima2025,
  title={High-density recording reveals sparse clusters (but not columns) for shape and texture encoding in macaque V4},
  author={Namima, Tomoyuki and Kempkes, Erin and Zamarashkina, Polina and Owen, Natalia and Pasupathy, Anitha},
  journal={Journal of Neuroscience},
  volume={45},
  number={5},
  year={2025},
  publisher={Society for Neuroscience}
}
```
