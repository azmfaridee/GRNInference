import pandas as pd
from scipy.io import loadmat
import math

yeast_mat = loadmat('yeast.mat')
yeastnames_mat = loadmat('ystnames.mat')
yeast_expressions = pd.DataFrame(yeast_mat['Yeast'])
yeast_names = pd.DataFrame(yeastnames_mat['yystr'])

df_orig = pd.DataFrame(yeast_mat['Yeast'].T, columns=yeastnames_mat['yystr'])

# set df as a small sample of the main dataset 
# df = df_orig
# df = df_orig.sample(10, axis=1)

# START zero order correlation analysis
# pearsons_corr = df.corr()
# corr_threshold = 0.8
# keys = pearsons_corr.keys()
# for i in range(len(keys)):
#     for j in range(i+1, len(keys)):
#         p, q = keys[i], keys[j]
#         # print('Testing out pair ({}, {})'.format(p, q))
#         if pearsons_corr[p][q] > corr_threshold or pearsons_corr[p][q] < -corr_threshold:
#             print('pair ({}, {}) has very high correlations'.format(p, q))
# END zero order correlation analysis

n_samples = 100
partial_corr_threshold = 0.1
tripplet_samples =  pd.DataFrame(columns=['a', 'b', 'c', 'r_ac_b'])
for i in range(n_samples):
    tripplet = df_orig.sample(3, axis=1)
    corr = tripplet.corr()
    r_ab, r_bc, r_ac = corr.iloc[0][1], corr.iloc[1][2], corr.iloc[0][2]
    # calculate partial correlations
    r_ac_b = (r_ac * r_ab * r_bc) / math.sqrt((1 - math.pow(r_ab, 2)) * (1 - math.pow(r_bc, 2)))
    temp = pd.DataFrame([tripplet.keys().values], columns=['a', 'b', 'c'])
    temp['r_ac_b'] = [[r_ac_b]]
    tripplet_samples = tripplet_samples.append(temp)
    