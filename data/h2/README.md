**Dataset URL:** https://dandiarchive.org/dandiset/000950

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:000950
python create_dataset.py --hf_repo_name "eminorhan/h2" --token_count_limit 10_000_000
```
where `hf_repo_name` is the HF repo name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks).

**Token count:** 297,332,736

**HF repo:** https://huggingface.co/datasets/eminorhan/h2

**Recorded area & stimulus, task, or behavior:** Recordings from human dorsal motor cortex ("hand knob" area) during attempted handwriting trials.

**Paper URL:** https://openreview.net/forum?id=STqaMqhtDi

```
@article{fan2023,
  title={Plug-and-play stability for intracortical brain-computer interfaces: A one-year demonstration of seamless brain-to-text communication},
  author={Fan, Chaofei and Hahn, Nick and Kamdar, Foram and Avansino, Donald and Wilson, Guy and Hochberg, Leigh and Shenoy, Krishna V and Henderson, Jaimie and Willett, Francis},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  pages={42258--42270},
  year={2023}
}
```
