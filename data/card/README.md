**Dataset URL:** https://datadryad.org/dataset/doi:10.5061/dryad.dncjsxm85

To download the data, go to the URL above and download the `t15_copyTask_neuralData.zip` archive (this contains the neural data). Extract it inside a new folder called `data`. Then, to create the corresponding HF dataset, run *e.g.*:
```python
python create_dataset.py --hf_repo_name "eminorhan/card" --token_count_limit 10_000_000
```
where `hf_repo_name` is the HF datasets repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks).

**Token count:** 2,484,658,688

**HF repo:** https://huggingface.co/datasets/eminorhan/card

**Recorded area & stimulus, task, or behavior:** Recordings from human ventral precentral gyrus during attempted speech.

**Paper URL:** https://www.medrxiv.org/content/10.1101/2023.12.26.23300110v2

```
@article{card2024,
  title={An accurate and rapidly calibrating speech neuroprosthesis},
  author={Card, Nicholas S and Wairagkar, Maitreyee and Iacobacci, Carrina and Hou, Xianda and Singer-Clark, Tyler and Willett, Francis R and Kunz, Erin M and Fan, Chaofei and Vahdati Nia, Maryam and Deo, Darrel R and others},
  journal={New England Journal of Medicine},
  volume={391},
  number={7},
  pages={609--618},
  year={2024}
}
```