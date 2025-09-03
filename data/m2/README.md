**Dataset URL:** https://dandiarchive.org/dandiset/000953

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:000953
python create_dataset.py --hf_repo_name "eminorhan/m2" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 12,708,384

**HF repo:** https://huggingface.co/datasets/eminorhan/m2

**Recorded area & stimulus, task, or behavior:** Recordings from macaque motor cortex (M1) during a finger movement task.

**Paper URL:** https://doi.org/10.1016/j.neuron.2021.08.009

```
@article{nason2021,
  title={Real-time linear prediction of simultaneous and independent movements of two finger groups using an intracortical brain-machine interface},
  author={Nason, Samuel R and Mender, Matthew J and Vaskov, Alex K and Willsey, Matthew S and Kumar, Nishant Ganesh and Kung, Theodore A and Patil, Parag G and Chestek, Cynthia A},
  journal={Neuron},
  volume={109},
  number={19},
  pages={3164--3177},
  year={2021},
  publisher={Elsevier}
}
```