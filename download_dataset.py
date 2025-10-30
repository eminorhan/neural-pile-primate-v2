from datasets import load_dataset

ds = load_dataset("eminorhan/neural-pile-primate", num_proc=32, split='train')
print(ds[0])
