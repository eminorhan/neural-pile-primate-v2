**Dataset URL:** https://dandiarchive.org/dandiset/000130

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:000130
python create_dataset.py --hf_repo_name "eminorhan/dmfc-rsg" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 14,003,818

**HF repo:** https://huggingface.co/datasets/eminorhan/dmfc-rsg

**Recorded area & stimulus, task, or behavior:** Recordings from macaque dorsomedial frontal cortex (DMFC) during a time-interval reproduction task.

**Paper URL:** https://doi.org/10.1016/j.neuron.2019.06.012

```
@article{sohn2019,
  title={Bayesian computation through cortical latent dynamics},
  author={Sohn, Hansem and Narain, Devika and Meirhaeghe, Nicolas and Jazayeri, Mehrdad},
  journal={Neuron},
  volume={103},
  number={5},
  pages={934--947},
  year={2019},
  publisher={Elsevier}
}
```