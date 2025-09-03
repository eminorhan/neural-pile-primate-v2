**Dataset URL:** https://gin.g-node.org/paolo_papale/TVSD

**NOTE:** Download speeds from the above URL are excrutiatingly slow in my experience (this seems to be a server side issue). So, to download the MUA data much faster through OneDrive links kindly provided by the author instead, please use:
```python
wget "https://herseninstituut-my.sharepoint.com/:u:/g/personal/papale_herseninstituut_knaw_nl/EZ5Z6MdGxbhLvk59Vn70pn8B-fk-4r5Tr5klhsfqEIm-Zw?e=kk7TUf&download=1"
wget "https://herseninstituut-my.sharepoint.com/:u:/g/personal/papale_herseninstituut_knaw_nl/EWuwwM-hXHlMi58rbgpTxwIBWxurgaf4EYfKk1Krf4k-Mw?e=ssyZSQ&download=1"
```
for data from monkey F and monkey N, respectively.

We do per-trial spike detection on the MUAs. To preprocess the data and create the corresponding HF dataset, run *e.g.*:
```python
python create_dataset.py --hf_repo_name "eminorhan/papale" --token_count_limit 10_000_000 --bin_size 20 --spike_threshold 3.5
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), `bin_size` is bin size in ms for aggregating spike counts (default: 20 ms), and `spike_threshold` is the threshold in units of std for detecting spikes.

**Token count:** 775,618,560

**HF repo:** https://huggingface.co/datasets/eminorhan/papale

**Recorded area & stimulus, task, or behavior:** Recordings from macaque V1, V4, and IT in response to ~22k natural images from the THINGS dataset.

**Paper URL:** https://www.cell.com/neuron/abstract/S0896-6273(24)00881-X

```
@article{papale2025,
  title={An extensive dataset of spiking activity to reveal the syntax of the ventral stream},
  author={Papale, Paolo and Wang, Feng and Self, Matthew W and Roelfsema, Pieter R},
  journal={Neuron},
  year={2025},
  publisher={Elsevier}
}
```

