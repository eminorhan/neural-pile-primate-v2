**Dataset URL:** https://zenodo.org/records/13952210

We manually download the data from the dataset URL above. Specifically, we use the `mahler_hand_dmfc_dataset_50ms.mat` and `perle_hand_dmfc_dataset_50ms.mat` data files for creating the dataset. Put these in the same directory as the `create_dataset.py` file. Then, to create the corresponding HF dataset, simply run *e.g.*:
```python
python create_dataset.py --hf_repo_name "eminorhan/rajalingham"
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to.

**Token count:** 14,923,100

**HF repo:** https://huggingface.co/datasets/eminorhan/rajalingham

**Recorded area & stimulus, task, or behavior:** Recordings from macaque dorsomedial frontal cortex (DMFC) during a naturalistic ball interception task.

**Paper URL:** https://www.nature.com/articles/s41467-024-54688-y

```
@article{rajalingham2025,
  title={Dynamic tracking of objects in the macaque dorsomedial frontal cortex},
  author={Rajalingham, Rishi and Sohn, Hansem and Jazayeri, Mehrdad},
  journal={Nature Communications},
  volume={16},
  number={1},
  pages={346},
  year={2025},
  publisher={Nature Publishing Group UK London}
}
```