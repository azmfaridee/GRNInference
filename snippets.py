import pandas as pd
import numpy as np

df = pd.read_csv('yeast_grn.csv', index_col=0)

sample = df.iloc[-1]
gene_id = sample.index[0]
sample.sort_values(ascending=False).head()