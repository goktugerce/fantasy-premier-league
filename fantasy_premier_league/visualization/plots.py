import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from .helpers import *

sns.set(style='darkgrid', font_scale=1.5)
sns.set_palette('cubehelix')


def draw_chip_usage(raw_data, save_path=None):
    """Draw chip usage in vertical bar plot"""
    data = prepare_data(raw_data, 'name', 'usage', 10)
    draw_bar_plot(data, 'name', 'usage', 'Chip', 'Usage %', False, True, save_path)


def draw_captaincy_stats(raw_data, save_path=None):
    """Draw captaincy stats in horizontal bar plot"""
    data = prepare_data(raw_data, 'name', 'captaincy', 10)
    draw_bar_plot(data, 'captaincy', 'name', 'Captaincy %', 'Name', True, False, save_path)


def draw_ownership_stats(raw_data, save_path=None):
    """Draw ownership stats in horizontal bar plot"""
    data = prepare_data(raw_data, 'name', 'ownership', 10)
    draw_bar_plot(data, 'ownership', 'name', 'Ownership %', 'Name', True, False, save_path)


def draw_effective_ownership_stats(raw_data, save_path=None):
    """Draw effective ownership stats in horizontal bar plot"""
    data = prepare_data(raw_data, 'name', 'effective_ownership', 10)
    draw_bar_plot(data, 'effective_ownership', 'name', 'Effective Ownership %', 'Name', True, False, save_path)


def draw_template_team(template_team, game='FPL', save_path=None):
    """Draw template team on subplot with player portraits or team kits"""
    data = prepare_template_team_data(template_team)
    images = prepare_images(data, game)

    fig = plt.figure(figsize=(12, 8))

    for index, image in enumerate(images):
        ax = fig.add_subplot(4, 5, image['index'] + 1)
        ax.title.set_text(data[index]['label'])
        plt.axis('off')
        plt.imshow(image['image'])

    plt.tight_layout(pad=0.5, w_pad=1, h_pad=1.0)

    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path)


def draw_bar_plot(data, key_name, value_name, xlabel, ylabel, x_percentage=False, y_percentage=False, save_path=None):
    """Wrapper function for bar plots."""
    plt.figure(figsize=(20, 10))

    ax = sns.barplot(x=key_name, y=value_name, data=pd.DataFrame(data))
    ax.set(xlabel=xlabel, ylabel=ylabel)

    if y_percentage:
        values = ax.get_yticks()
        ax.set_yticklabels(['{:,.2%}'.format(y) for y in values])

    if x_percentage:
        values = ax.get_xticks()
        ax.set_xticklabels(['{:,.2%}'.format(x) for x in values])

    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path)
