# if __name__ == '__main__':
#     yeast_names = []
#     yeast_values = []
    
#     with open('yeast_names.txt') as f:
#         for l in f: yeast_names.append(l.strip('\n\x00'))

#     with open('yeast_values.txt') as f:
#         for l in f: yeast_values.append(map(lambda x: float(x), l.strip('\n\x00').split('\t')))
    
import pandas as pd
from scipy.io import loadmat

yeast_mat = loadmat('yeast.mat')
yeastnames_mat = loadmat('ystnames.mat')
# yeast_expressions = pd.DataFrame(yeast_mat['Yeast'])
# yeast_names = pd.DataFrame(yeastnames_mat['yystr'])

df = pd.DataFrame(yeast_mat['Yeast'].T, columns=yeastnames_mat['yystr'])
