import pandas as pd
from scipy.io import loadmat

yeast_mat = loadmat('yeast.mat')
yeastnames_mat = loadmat('ystnames.mat')
yeast_expressions = pd.DataFrame(yeast_mat['Yeast'])
yeast_names = pd.DataFrame(yeastnames_mat['yystr'])

df_orig = pd.DataFrame(yeast_mat['Yeast'].T, columns=yeastnames_mat['yystr'])

# set df as a small sample of the main dataset 
df = df_orig
# df = df_orig.T.sample(10).T
pearsons_corr = df.corr()

corr_threshold = 0.8
keys = pearsons_corr.keys()
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        p, q = keys[i], keys[j]
        # print('Testing out pair ({}, {})'.format(p, q))
        if pearsons_corr[p][q] > corr_threshold or pearsons_corr[p][q] < -corr_threshold:
            print('pair ({}, {}) has very high correlations'.format(p, q))