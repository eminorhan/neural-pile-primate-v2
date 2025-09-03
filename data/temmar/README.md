**Dataset URL:** https://dandiarchive.org/dandiset/001201

To download the data and create the corresponding HF dataset, *e.g.*:
```python
mkdir data && cd data
dandi download DANDI:001201
python create_dataset.py --hf_repo_name "eminorhan/temmar" --token_count_limit 10_000_000
```
where `hf_repo_name` is the HF repo name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks).

**Token count:** 27,388,320

**HF repo:** https://huggingface.co/datasets/eminorhan/temmar

**Recorded area & stimulus, task, or behavior:** Recordings from macaque motor cortex (M1) during a self-paced finger movement task.

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