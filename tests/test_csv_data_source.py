import os

import numpy.testing as npt
import pytest


def test_load_data_source_from_folder_containing_multiple_csvs(tmpdir):
    from inflammation.data_source import CSVDataSource
    open(os.path.join(tmpdir, 'inflammation-01.csv'), 'x').close()
    open(os.path.join(tmpdir, 'inflammation-02.csv'), 'x').close()

    data_source = CSVDataSource(tmpdir)
    data = data_source.load_data()
    assert len(data) == 2


def test_load_data_on_empty_dir_raises_error(tmpdir):
    from inflammation.data_source import CSVDataSource
    with pytest.raises(ValueError):
        data_source = CSVDataSource(tmpdir)
        data_source.load_data()

def test_load_data_on_csv_loads_data(tmpdir):
    from inflammation.data_source import CSVDataSource
    with open(os.path.join(tmpdir, 'inflammation-01.csv'), 'x') as data_csv:
        data_csv.write('0,1,2')

    data_source = CSVDataSource(tmpdir)
    data = data_source.load_data()
    npt.assert_array_equal(data, [[0., 1., 2.]])
