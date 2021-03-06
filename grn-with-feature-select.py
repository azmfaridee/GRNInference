import pandas as pd
import numpy as np
from scipy.io import loadmat
import math

from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn import linear_model

# read data
yeast_mat = loadmat('yeast.mat')
yeastnames_mat = loadmat('ystnames.mat')
yeast_expressions = pd.DataFrame(yeast_mat['Yeast'])
yeast_names = pd.DataFrame(yeastnames_mat['yystr'])
df_orig = pd.DataFrame(yeast_mat['Yeast'].T, columns=yeastnames_mat['yystr'])

# n_samples = 20
# df = df_orig.sample(n_samples, axis=1)
df = df_orig

n_genes = len(df.keys())
grn = pd.DataFrame(np.zeros(shape=(len(df.keys()), len(df.keys()))), index=df.keys(), columns=df.keys())

# START FOR
for i in range(n_genes): #[0]:
    # i = 2 # for i = 6177, 4269 should be the top one
    keys = list(df.keys())
    target_gene = keys[i]
    keys.remove(target_gene)
    input_genes = keys
    # print(input_genes, target_gene)
    
    X = df[input_genes]
    y = df[target_gene]
    
    print('Training for target gene {}: {}'.format(i, target_gene))
    clf = RandomForestRegressor(n_estimators=200, oob_score=True, n_jobs=-1)
    # clf = SVR(kernel='linear')
    # clf = linear_model.Ridge()
    # scores = cross_val_score(clf, X, y, cv=5, n_jobs=-1)
    # print('Mean accuracy: {}'.format(scores.mean()))
    
    clf.fit(X, y)
    # importantce = pd.DataFrame(clf.feature_importances_)
    # top_5 = importantce.sort_values(0, ascending=False).head()
    # print('Top 5 geness {} out of {}\n'.format(top_5, importantce.size))
    
    for i, x in zip(range(clf.feature_importances_.size), clf.feature_importances_):
        # print(i, input_genes[i], x)
        grn[target_gene][input_genes[i]] = x
# END FOR

grn.to_csv('yeast_grn.csv')
