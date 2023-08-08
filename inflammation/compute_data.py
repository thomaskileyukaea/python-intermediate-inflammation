import glob
import os
import numpy as np

from inflammation import models


def compute_standard_deviation_by_data(all_loaded_data):
    means_by_day = map(models.daily_mean, all_loaded_data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation

def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets

    Needs a data_source to provide the data that the analysis will be performed on.
    It then works out the mean inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    data = data_source.load_data()
    daily_standard_deviation = compute_standard_deviation_by_data(data)

    return daily_standard_deviation
