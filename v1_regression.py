import torch
import numpy as np
import pandas as pd

csv_data = pd.read_csv('Regression.csv')

npArray = csv_data.to_numpy()