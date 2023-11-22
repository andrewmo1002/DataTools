import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import data_process_tools as dpt


def visual_distribution(df, mean_values, std_values):
    num_per_row = 4
    num_cols = len(mean_values)
    num_plots_per_row = min(num_cols, num_per_row)
    num_rows = (num_cols - 1) // num_plots_per_row + 1

    fig, axes = plt.subplots(num_rows, num_plots_per_row, figsize=(15, 4*num_rows), squeeze=False)
    for i, data_col in enumerate(mean_values.index):
        row = i // num_plots_per_row
        col = i % num_plots_per_row

        ax = axes[row, col]

        # Plotting histogram
        n, bins, patches = ax.hist(
            df[data_col],
            bins='auto',
            alpha=0.6
        )

        # ....
        
        mean = mean_values[data_col]
        std = std_values[data_col]

        # Setting x-axis limits within 3 std range
        lower_limit = mean - 3 * std
        upper_limit = mean + 3 * std
        ax.set_xlim(lower_limit, upper_limit)

        ax.axvline(
            mean,
            color='red',
            label='Mean',
            alpha=0.3,
            lw=3
        )

        for j in range(1, 3):  # Plotting 1, 2, and 3 std ranges
            y_values = np.linspace(0, max(n), 100)  # Adjust the number of points as needed
            std_range = mean + j * std, mean - j * std
            std_range = (max(std_range[0], lower_limit), min(std_range[1], upper_limit))
            ax.fill_betweenx(
                y_values, std_range[0], std_range[1],
                alpha=0.2,
                color='orange',
                label=f'{j} Std'
            )

        ax.set_title(f'{data_col}')
        ax.legend()

    plt.tight_layout()
    plt.show()


def visual_distribution(df, mean_values, std_values):
    num_per_row = 4
    num_cols = len(mean_values)
    num_plots_per_row = min(num_cols, num_per_row)
    num_rows = (num_cols - 1) // num_plots_per_row + 1

    fig, axes = plt.subplots(num_rows, num_plots_per_row, figsize=(15, 4*num_rows), squeeze=False)
    for i, data_col in enumerate(mean_values.index):
        row = i // num_plots_per_row
        col = i % num_plots_per_row

        ax = axes[row, col]

        # Plotting histogram
        n, bins, patches = ax.hist(
            df[data_col],
            bins='auto',
            alpha=0.6
        )

        ax.axvline(
            mean_values[data_col],
            color='red',
            label='Mean',
            alpha=0.3,
            lw=3
        )

        for j in range(1, 4):  # Plotting 1, 2, and 3 std ranges
            y_values = np.linspace(0, max(n), 100)  # Adjust the number of points as needed
            std_range = (mean_values[data_col] + j * std_values[data_col],
                         mean_values[data_col] - j * std_values[data_col])
            ax.fill_betweenx(
                y_values, std_range[0], std_range[1],
                alpha=0.3,
                color='orange',
                label=f'{j} Std'
            )

        ax.set_title(f'{data_col}')
        ax.legend()

    plt.tight_layout()
    plt.show()