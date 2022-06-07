import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_blobs
from sklearn.cluster import k_means


# Create a dataset using make_blobs()

data_points = make_blobs(100, n_features=4, centers=5)
cols = ['feature1', 'feature2', 'feature3', 'feature4']

df = pd.DataFrame(data_points[0], columns=cols)
print(df.head())