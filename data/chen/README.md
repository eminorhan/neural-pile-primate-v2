**Dataset URL:** https://dandiarchive.org/dandiset/001435

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:001435
python create_dataset.py --hf_repo_name "eminorhan/chen" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 2,720,804,574

**HF repo:** https://huggingface.co/datasets/eminorhan/chen

**Recorded area & stimulus, task, or behavior:** Recordings from macaque anterior cingulate cortex (ACC) during a two-player game with volatile hidden states.

**Paper URL:** https://www.biorxiv.org/content/10.1101/2025.02.13.638172v1

```
@article{chen2025,
  title={Evidence accumulation from experience and observation in the cingulate cortex},
  author={Chen, Ruidong and Radkani, Setayesh and Valluru, Neelima and Yoo, Seng Bum and Jazayeri, Mehrdad},
  journal={bioRxiv},
  pages={2025--02},
  year={2025},
  publisher={Cold Spring Harbor Laboratory}
}
```