**Dataset URL:** https://doi.org/10.5061/dryad.c2fqz61kb

Dataset downloaded manually from above URL.

To create the corresponding HF dataset, *e.g.*:
```python
python create_dataset.py --hf_repo_name "eminorhan/wojcik" --token_count_limit 10_000_000 --bin_size 20
```
where `hf_repo_name` is the HF repo name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is the bin size in ms for aggregating spike counts (default: 20 ms).

**Token count:** 422,724,515 tokens

**HF repo:** https://huggingface.co/datasets/eminorhan/wojcik

**Recorded area & stimulus, task, or behavior:** Recordings from macaque prefrontal cortex (PFC) during a rule learning task.

**Paper URL:** https://www.biorxiv.org/content/10.1101/2023.04.24.538054v2

```
@article{wojcik2023,
  title={Learning shapes neural geometry in the prefrontal cortex},
  author={W{\'o}jcik, Micha{\l} J and Stroud, Jake P and Wasmuht, Dante and Kusunoki, Makoto and Kadohisa, Mikiko and Buckley, Mark J and Myers, Nicholas E and Hunt, Laurence T and Duncan, John and Stokes, Mark G},
  journal={bioRxiv},
  pages={2023--04},
  year={2023},
  publisher={Cold Spring Harbor Laboratory}
}
```