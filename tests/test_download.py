import pandas as pd
import os
import pytest

p = 'data/criteo-uplift.parquet'

@pytest.fixture
def data():
  return pd.read_parquet(p)

def test_is_downloaded_and_opens():
  assert os.path.exists(p)
  df = pd.read_parquet(p)
  assert df is not None

def test_data_shape(data):
  assert data.shape[0] >= 13_979_000
  assert data.shape[1] == 16