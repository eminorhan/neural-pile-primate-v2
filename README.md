[![Static Badge](https://img.shields.io/badge/🤗_datasets-neural_pile_primate-blue)](https://huggingface.co/datasets/eminorhan/neural-pile-primate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Spiking neural activity data recorded from primates 

~40B uncompressed tokens of spiking neural activity data recorded from primates (tokens=neurons x time bins). Unless otherwise noted, the data consist of spike counts in 20 ms time bins recorded from each neuron. 

This repository contains the code and instructions for building the dataset from scratch. The actual final dataset is hosted at [this](https://huggingface.co/datasets/eminorhan/neural-pile-primate) public HF repository.

The current component datasets and token counts per dataset are as follows:

| Name               | Tokens          | Source                                                      | Details                        | Species  | Subjects | Sessions |
|:-------------------|----------------:|:------------------------------------------------------------|:-------------------------------|:---------|---------:|---------:|
| Xiao               | 17,695,820,059  | [dandi:000628](https://dandiarchive.org/dandiset/000628)    | [link](data/xiao)              | macaque  | 13       | 679      |
| Neupane (PPC)      | 7,899,849,087   | [dandi:001275](https://dandiarchive.org/dandiset/001275)    | [link](data/neupane-ppc)       | macaque  | 2        | 10       |
| Chen               | 2,720,804,574   | [dandi:001435](https://dandiarchive.org/dandiset/001435)    | [link](data/chen)              | macaque  | 2        | 51       |
| Card               | 2,484,658,688   | [dryad:dncjsxm85]( https://doi.org/10.5061/dryad.dncjsxm85) | [link](data/card)              | human    | 1        | 45       |
| Willett            | 1,796,119,552   | [dryad:x69p8czpq]( https://doi.org/10.5061/dryad.x69p8czpq) | [link](data/willett)           | human    | 1        | 44       |
| Churchland         | 1,278,669,504   | [dandi:000070](https://dandiarchive.org/dandiset/000070)    | [link](data/churchland)        | macaque  | 2        | 10       |
| Neupane (EC)       | 911,393,376     | [dandi:000897](https://dandiarchive.org/dandiset/000897)    | [link](data/neupane-entorhinal)| macaque  | 2        | 15       |
| Kim                | 804,510,741     | [dandi:001357](https://dandiarchive.org/dandiset/001357)    | [link](data/kim)               | macaque  | 2        | 159      |
| Even-Chen          | 783,441,792     | [dandi:000121](https://dandiarchive.org/dandiset/000121)    | [link](data/even-chen)         | macaque  | 2        | 12       |
| Temmar             | 781,701,792     | [dandi:001201](https://dandiarchive.org/dandiset/001201)    | [link](data/temmar)            | macaque  | 1        | 330      |
| Papale             | 775,618,560     | [g-node:TVSD](https://gin.g-node.org/paolo_papale/TVSD)     | [link](data/papale)            | macaque  | 2        | 2        |
| Perich             | 688,889,368     | [dandi:000688](https://dandiarchive.org/dandiset/000688)    | [link](data/perich)            | macaque  | 4        | 111      |
| Wojcik             | 422,724,515     | [dryad:c2fqz61kb](https://doi.org/10.5061/dryad.c2fqz61kb)  | [link](data/wojcik)            | macaque  | 2        | 50       |
| Makin              | 375,447,744     | [zenodo:3854034](https://zenodo.org/records/3854034)        | [link](data/makin)             | macaque  | 2        | 47       |
| H2                 | 297,332,736     | [dandi:000950](https://dandiarchive.org/dandiset/000950)    | [link](data/h2)                | human    | 1        | 47       |
| Lanzarini          | 259,179,392     | [osf:82jfr](https://osf.io/82jfr/)                          | [link](data/lanzarini)         | macaque  | 2        | 10       |
| Athalye            | 101,984,317     | [dandi:000404](https://dandiarchive.org/dandiset/000404)    | [link](data/athalye)           | macaque  | 2        | 13       |
| M1-A               | 45,410,816      | [dandi:000941](https://dandiarchive.org/dandiset/000941)    | [link](data/m1-a)              | macaque  | 1        | 11       |
| M1-B               | 43,809,344      | [dandi:001209](https://dandiarchive.org/dandiset/001209)    | [link](data/m1-b)              | macaque  | 1        | 12       |
| H1                 | 33,686,576      | [dandi:000954](https://dandiarchive.org/dandiset/000954)    | [link](data/h1)                | human    | 1        | 40       |
| Moore              | 30,643,839      | [dandi:001062](https://dandiarchive.org/dandiset/001062)    | [link](data/moore)             | marmoset | 1        | 1        |
| Rajalingham        | 14,923,100      | [zenodo:13952210](https://zenodo.org/records/13952210)      | [link](data/rajalingham)       | macaque  | 2        | 2        |
| DMFC-rsg           | 14,003,818      | [dandi:000130](https://dandiarchive.org/dandiset/000130)    | [link](data/dmfc-rsg)          | macaque  | 1        | 2        |
| M2                 | 12,708,384      | [dandi:000953](https://dandiarchive.org/dandiset/000953)    | [link](data/m2)                | macaque  | 1        | 20       |
| Area2-bump         | 7,394,070       | [dandi:000127](https://dandiarchive.org/dandiset/000127)    | [link](data/area2-bump)        | macaque  | 1        | 2        |

**Total number of tokens:** 40,281,725,444

The combined dataset takes up about 40 GB on disk when stored as memory-mapped `.arrow` files. The HF `datasets` library uses `.arrow` files for local caching, so you will need at least this much free disk space in order to be able to utilize it. 

## Requirements
Please see the auto-generated [`requirements.txt`](requirements.txt) file.

## Creating the component datasets
The [`data`](data) directory contains all the information needed to download and preprocess the individual component datasets and push them to the HF datasets hub (quick links to the subdirectories for component datasets are provided in the Details column in the table above). You can use these as a starting point if you would like to add more datasets to the mix. Adding further `dandisets` should be particularly easy based off of the current examples. When creating the component datasets, we split long sessions (>10M tokens) into smaller equal-sized chunks of no more than 10M tokens. This makes data loading more efficient and prevents errors while creating and uploading HF datasets.

## Merging the component datasets into a single dataset
Once we have created the individual component datasets, we merge them into a single dataset with the [`merge_datasets.py`](merge_datasets.py) script. This also shuffles the combined dataset, creates a separate test split (1% of the data), and pushes the dataset to the HF datasets hub. If you would like to add more datasets to the mix, simply add their HF dataset repository names to the `repo_list` in `merge_datasets.py`.

## Visualizing the datasets
[`visualize_dataset.py`](visualize_dataset.py) provides some basic functionality to visualize random samples from the datasets as a basic sanity check:
```python
python visualize_datasets.py --repo_name 'eminorhan/xiao' --n_examples 9
```
This will randomly sample `n_examples` examples from the corresponding dataset and visualize them as below, where *x* is the time axis (binned into 20 ms windows) and the *y* axis represents the recorded units:

![](rasters/xiao.jpg)

Users also have the option to visualize `n_examples` random examples from each component dataset by calling:
```python
python visualize_datasets.py --plot_all --n_examples 9
```
This will save the visualizations for all component datasets in a folder called `visuals` as in [here](rasters).

## Extracting motifs
For a more fine-grained analysis of the data, I also wrote a simple script in [`extract_motifs.py`](extract_motifs.py) that extracts motifs from the data and keeps track of their statistics over the whole dataset. Given a particular motif or patch size (*p_n*, *p_t*), *e.g.* (1, 8), *i.e.* 1 neuron and 8 time bins, this script will extract all **unique** motifs of this size over the entire dataset together with their frequency of occurrence. This script will also visualize the most common motifs in a figure like the following (blue is 0, red is 1 in this figure):

![](primate_(1x8)_motifs.jpeg)

For (1, 8) motifs, I find that ~9M unique motifs are instantiated over the whole dataset (out of a maximum possible of ~8B unique motifs of this size). The "silent" motif (all zeros) dominates the dataset with something like ~3M occurrences overall, distantly followed by various single spike motifs, followed by the "all ones" motif (111...1), followed by various two spike motifs, *etc.*, as shown above. More examples can be found in the [motifs](motifs) folder.

