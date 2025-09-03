**Dataset URL:** https://zenodo.org/records/3854034

To download the data from Zenodo, please run (requires a Zenodo access token):
```python
python download_dataset.py
```
when prompted, enter your Zenodo access token.

Then, to create the corresponding HF dataset, run *e.g.*:
```python
python create_dataset.py --hf_repo_name "eminorhan/makin" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF repo name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 375,447,744

**HF repo:** https://huggingface.co/datasets/eminorhan/makin

**Recorded area & stimulus, task, or behavior:** Recordings from macaque motor cortex (M1) and sensorimotor cortex (S1) during reaching movements.

**Paper URL:** https://iopscience.iop.org/article/10.1088/1741-2552/aa9e95

```
@article{makin2018,
  title={Superior arm-movement decoding from cortex with a new, unsupervised-learning algorithm},
  author={Makin, Joseph G and O’Doherty, Joseph E and Cardoso, Mariana MB and Sabes, Philip N},
  journal={Journal of Neural Engineering},
  volume={15},
  number={2},
  pages={026010},
  year={2018},
  publisher={IOP Publishing}
}
```