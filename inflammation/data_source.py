import glob
import os
from inflammation import models


class DataSource:
    """An abstract base class for providing a series of inflammation data."""

    def load_data(self):
        """Loads the data and returns it as a list, where each entry corresponds to one file,
        and each entry is a 2D array with patients inflammation by day."""
        raise NotImplementedError


class CSVDataSource(DataSource):
    """Loads all the inflammation csvs within a specified folder.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path
        super().__init__()

    def load_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation csv's found in path {self.dir_path}")
        data = map(models.load_csv, data_file_paths)
        return list(data)