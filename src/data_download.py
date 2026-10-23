import os
import pandas as pd
from .config import config


def data_download():
  file_path = config.get('data_path')
  if os.path.exists(file_path):
    print("Данные уже загружены")
    return 1

  os.makedirs("data", exist_ok=True)

  url = config.get('data_url')
  if url is None:
    raise ValueError('Нет ссылки на данные в конфиге (data_url)')

  dtypes = {
    'treatment': 'int8', 'exposure': 'int8', 
    'visit': 'int8', 'conversion': 'int8'
  }
  for i in range(12):
    dtypes[f'f{i}'] = 'float32'

  df = pd.read_csv(url, compression='gzip', dtype=dtypes)

  df.to_parquet(file_path, index=False)

  return 0