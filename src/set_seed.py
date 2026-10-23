from .config import config
import numpy as np
import random


def set_seed():
  s = config.get('seed')

  random.seed(s)
  np.random.seed(s)