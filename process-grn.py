# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 02:50:01 2017

@author: faridee1
"""

import pandas as pd
import numpy as np

df = pd.read_csv('yeast_grn.csv', index_col=0)
# this runs very slow because of using basic dict for large data instead of numpy or pandas data structure
top_5 = {}
for row_label in df.index:
    row = df.loc[row_label, :]
    row.sort_values(ascending=False, inplace=True)
    top_5[row_label] = row[:5]
