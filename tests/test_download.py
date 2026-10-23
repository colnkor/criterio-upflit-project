import pandas as pd
import os
import pytest
from src.data_download import data_download

p = 'data/criteo-uplift.parquet'

@pytest.fixture
def data():
  return pd.read_parquet(p)

def test_download():
  res = data_download()
  assert res >= 0

def test_is_downloaded_and_opens(data):
  assert os.path.exists(p)
  assert data is not None

def test_data_shape(data):
  assert data.shape[0] >= 13_979_000
  assert data.shape[1] == 16