**Dataset URL:** https://dandiarchive.org/dandiset/000404

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:000404
python create_dataset.py --hf_repo_name "eminorhan/athalye" --token_count_limit 10_000_000
```
where `hf_repo_name` is the HF repo name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks).

Monkey G spike counts are sampled at 60 Hz, Monkey J spike counts are sampled at 200 Hz; we resample J to 50 Hz (and leave G at 60 Hz as it's close enough to 20 ms binning).

**Token count:** 101,984,317 tokens

**HF repo:** https://huggingface.co/datasets/eminorhan/athalye

**Recorded area & stimulus, task, or behavior:** Recordings from macaque premotor and motor cortex (PMd/M1) during center-out reach and obstacle avoidance tasks.

**Paper URL:** https://www.cell.com/current-biology/fulltext/S0960-9822(23)00778-9

```
@article{athalye2023,
  title={Invariant neural dynamics drive commands to control different movements},
  author={Athalye, Vivek R and Khanna, Preeya and Gowda, Suraj and Orsborn, Amy L and Costa, Rui M and Carmena, Jose M},
  journal={Current Biology},
  volume={33},
  number={14},
  pages={2962--2976},
  year={2023},
  publisher={Elsevier}
}
```