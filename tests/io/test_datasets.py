import pandas as pd
from traffic_predictor.io import datasets
import os


def test_csv_loader(data_path: str):
    loader = datasets.CSVLoader(path=os.path.join(data_path, "sample_data_read.csv"))
    data = loader.load_data()
    assert isinstance(data, pd.DataFrame)
    assert data.shape[0] == 5
    assert data.shape[1] == 3
    assert data.columns.tolist() == ["Gare", "ds", "traffic"]
    assert data.isna().sum().sum() == 0


def test_csv_saver(data_path: str):
    sample_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    saver = datasets.CSVSaver(path=os.path.join(data_path, "sample_data_write.csv"))
    saver.save_data(sample_df)
    assert os.path.exists(os.path.join(data_path, "sample_data_write.csv"))
