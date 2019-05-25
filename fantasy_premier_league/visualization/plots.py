import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid', font_scale=1.5)
sns.set_palette('cubehelix')


def prepare_data(dictionary, key_name, value_name, limit=10):
    """Prepare data for the bar plot. Convert key, value pairs to named objects"""
    data = []
    for key, value in dictionary.items():
        record = {key_name: key, value_name: value}
        data.append(record)
    return data[:limit]


def draw_chip_usage(raw_data):
    """Draw chip usage in vertical bar plot"""
    data = prepare_data(raw_data, 'name', 'usage', 10)
    draw_bar_plot(data, 'name', 'usage', 'Chip', 'Usage %', False, True)


def draw_captaincy_stats(raw_data):
    """Draw captaincy stats in horizontal bar plot"""
    data = prepare_data(raw_data, 'name', 'captaincy', 10)
    draw_bar_plot(data, 'captaincy', 'name', 'Captaincy %', 'Name', True, False)


def draw_ownership_stats(raw_data):
    """Draw ownership stats in horizontal bar plot"""
    data = prepare_data(raw_data, 'name', 'ownership', 10)
    draw_bar_plot(data, 'ownership', 'name', 'Ownership %', 'Name', True, False)


def draw_effective_ownership_stats(raw_data):
    """Draw effective ownership stats in horizontal bar plot"""
    data = prepare_data(raw_data, 'name', 'effective_ownership', 10)
    draw_bar_plot(data, 'effective_ownership', 'name', 'Effective Ownership %', 'Name', True, False)


def draw_bar_plot(data, key_name, value_name, xlabel, ylabel, x_percentage=False, y_percentage=False):
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

    plt.show()
