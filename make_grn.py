import pandas as pd
import numpy as np
from scipy.io import loadmat
import math

yeast_mat = loadmat('yeast.mat')
yeastnames_mat = loadmat('ystnames.mat')
yeast_expressions = pd.DataFrame(yeast_mat['Yeast'])
yeast_names = pd.DataFrame(yeastnames_mat['yystr'])

df_orig = pd.DataFrame(yeast_mat['Yeast'].T, columns=yeastnames_mat['yystr'])

# set df as a small sample of the main dataset 
# df = df_orig
df = df_orig.sample(16, axis=1)

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

# START partial correlation analysis
# initial parameters
# n_samples = 100
# zero = 0.001
# part_zero = 0.1
# tripplet_samples =  pd.DataFrame(np.zeros(shape=(n_samples, 8)), 
#                     columns=['a', 'b', 'c', 'r_ac','r_ac_b', 'no_effect', 'full_expl', 'part_expl'],
#                     dtype=str) # setting str datatye is necessary as we have mixed data in the frame
# for i in range(n_samples):
#     tripplet = df.sample(3, axis=1)
#     corr = tripplet.corr()
#     r_ab, r_bc, r_ac = corr.iloc[0][1], corr.iloc[1][2], corr.iloc[0][2]
#     # calculate partial correlations
#     r_ac_b = (r_ac * r_ab * r_bc) / math.sqrt((1 - math.pow(r_ab, 2)) * (1 - math.pow(r_bc, 2)))
    
#     tripplet_samples.loc[i]['a'], tripplet_samples.loc[i]['b'], tripplet_samples.loc[i]['c'] = tripplet.keys()
#     tripplet_samples.loc[i]['r_ac'], tripplet_samples.loc[i]['r_ac_b'] = r_ac, r_ac_b
#     tripplet_samples.loc[i]['no_effect'] = 1 if abs(r_ac - r_ac_b) > zero else 0
#     tripplet_samples.loc[i]['full_expl'] = 1 if abs(r_ac_b) < zero else 0
#     tripplet_samples.loc[i]['part_expl'] = 1 if abs(r_ac_b) < part_zero and abs(r_ac_b) > zero else 0
# END partial correlaiton analysis

# create initial grn
# TODO: use sparse data type later instead of the normal data type
grn = pd.DataFrame(np.zeros(shape=(len(df.keys()), len(df.keys()))), index=df.keys(), columns=df.keys())
keys = grn.keys()
# each row denotes a child node and each column denotes a parent node
for i in range(len(keys)):
    p = keys[i]
    n_parents = np.random.randint(2, 8)
    # for q in df.sample(n_parents, axis=1).keys():
    #     grn[p][q] = grn[q][p] = 1
    candidates = pd.Series([keys[j] for j in range(i+1, len(keys))] )
    # for j in range(i+1, len(keys)):
    remaining_parents = min(n_parents, len(candidates))
    if remaining_parents > 0:
        for q in candidates.sample(remaining_parents):
            grn[q][p] = 1
grn_sparse = grn.to_sparse()
