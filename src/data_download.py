def data_download():
  import os
  import pandas as pd

  os.makedirs("data", exist_ok=True)
  url = "https://huggingface.co/datasets/criteo/criteo-uplift/resolve/main/criteo-research-uplift-v2.1.csv.gz"

  dtypes = {
    'treatment': 'int8', 'exposure': 'int8', 
    'visit': 'int8', 'conversion': 'int8'
  }
  for i in range(12):
    dtypes[f'f{i}'] = 'float32'

  df = pd.read_csv(url, compression='gzip', dtype=dtypes)

  df.to_parquet('data/criteo-uplift.parquet', index=False)


data_download()