import numpy as np
import matplotlib.pylab as plt
import matplotlib as mp
from datasets import load_dataset


def visualize_dataset():
    """
    Displays 3 random samples from the primate and rodent subsets of the dataset
    """

    ds_primate = load_dataset("eminorhan/neural-bench-primate", split="train")
    ds_rodent = load_dataset("eminorhan/neural-bench-rodent", split="train")
    print('Number of rows in dataset (primate):', len(ds_primate))
    print('Number of rows in dataset (rodent):', len(ds_rodent))

    indices_primate = np.random.choice(np.arange(0, len(ds_primate)), size=3, replace=False).tolist()
    indices_rodent = np.random.choice(np.arange(0, len(ds_primate)), size=3, replace=False).tolist()
    print('Random indices ready ...')

    subdata_primate = [ds_primate[i]['spike_counts'] for i in indices_primate]
    subdata_rodent = [ds_rodent[i]['spike_counts'] for i in indices_rodent]
    sources_primate = [ds_primate[i]['source_dataset'] for i in indices_primate]
    sources_rodent = [ds_rodent[i]['source_dataset'] for i in indices_rodent]
    print('Subdata ready ...')

    plt.clf()
    ax = 6 * [None]

    for i in range(3):
        ax[i] = plt.subplot(2, 3, i + 1)
        x = np.array(subdata_primate[i])
        plt.imshow(x, interpolation='nearest', aspect='auto', cmap='gray_r')
        plt.xlim([-1, x.shape[-1]])
        plt.ylim([-1, x.shape[0]])
        plt.xticks([0, x.shape[-1]-1], ['0', str(x.shape[-1] // 50)], fontsize=6)
        plt.yticks([0, x.shape[0]-1], [str(x.shape[0]), '1'], fontsize=6)
        plt.title(sources_primate[i], fontsize=9, color='cornflowerblue')
        ax[i].spines["right"].set_visible(False)
        ax[i].spines["top"].set_visible(False)
        ax[i].yaxis.set_ticks_position('left')
        ax[i].xaxis.set_ticks_position('bottom')
        if i == 0:
            plt.xlabel('Time (seconds)', fontsize=8)
            plt.ylabel('Neurons', fontsize=8)

    for i in range(3):
        ax[i+3] = plt.subplot(2, 3, i + 4)
        x = np.array(subdata_rodent[i])
        plt.imshow(x, interpolation='nearest', aspect='auto', cmap='gray_r')
        plt.xlim([-1, x.shape[-1]])
        plt.ylim([-1, x.shape[0]])
        plt.xticks([0, x.shape[-1]-1], ['0', str(x.shape[-1] // 50)], fontsize=6)
        plt.yticks([0, x.shape[0]-1], [str(x.shape[0]), '1'], fontsize=6)
        plt.title(sources_rodent[i], fontsize=9, color='peru')
        ax[i+3].spines["right"].set_visible(False)
        ax[i+3].spines["top"].set_visible(False)
        ax[i+3].yaxis.set_ticks_position('left')
        ax[i+3].xaxis.set_ticks_position('bottom')
        if i == 0:
            plt.xlabel('Time (seconds)', fontsize=8)
            plt.ylabel('Neurons', fontsize=8)
        
    plt.tight_layout()
    mp.rcParams['axes.linewidth'] = 0.75
    mp.rcParams['patch.linewidth'] = 0.75
    mp.rcParams['patch.linewidth'] = 1.15
    mp.rcParams['font.sans-serif'] = ['FreeSans']
    mp.rcParams['mathtext.fontset'] = 'cm'
    plt.savefig('examples.pdf', bbox_inches='tight', dpi=100)


if __name__ == '__main__':

    visualize_dataset()