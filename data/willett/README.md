**Dataset URL:** https://datadryad.org/stash/dataset/doi:10.5061/dryad.x69p8czpq

To download the data, go to the URL above and download `diagnosticBlocks.tar.gz`, `sentences.tar.gz`, and `tuningTasks.tar.gz` (we use all available data). Extract them inside a new folder called `data`. Then, to create the corresponding HF dataset, run *e.g.*:
```python
python create_dataset.py --hf_repo_name "eminorhan/willett" --token_count_limit 10_000_000
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks).

**Token count:** 1,796,119,552

**HF repo:** https://huggingface.co/datasets/eminorhan/willett

**Recorded area & stimulus, task, or behavior:** Recordings from human premotor cortex during attempted speech.

**Paper URL:** https://www.nature.com/articles/s41586-023-06377-x

```
@article{willett2023,
  title={A high-performance speech neuroprosthesis},
  author={Willett, Francis R and Kunz, Erin M and Fan, Chaofei and Avansino, Donald T and Wilson, Guy H and Choi, Eun Young and Kamdar, Foram and Glasser, Matthew F and Hochberg, Leigh R and Druckmann, Shaul and others},
  journal={Nature},
  volume={620},
  number={7976},
  pages={1031--1036},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```

