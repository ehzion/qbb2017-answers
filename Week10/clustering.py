#!/usr/bin/env python

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
from scipy import stats
from sklearn import datasets
from sklearn.cluster import KMeans



"""
./clustering.py hema_data.txt
"""

df = pd.read_csv(sys.argv[1], delimiter = '\t')
labels = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']
matrix = df[labels]

lmatrix = sch.linkage(matrix, method = "average")
heatmap = sch.leaves_list(lmatrix)

lmatrixtp = sch.linkage(matrix.T, method = "average")
heatmaptp = sch.leaves_list(lmatrixtp)

orderedmatrix = matrix.values[heatmap,:]

tlabels = np.array(labels)[heatmaptp]

plt.figure()
plt.imshow(orderedmatrix, aspect = 'auto', interpolation = 'nearest')
plt.grid(False)
plt.colorbar()
plt.xticks( [x for x in range(6)], tlabels) 
plt.savefig("Heatmap.png")
plt.close()


plt.figure()
sch.dendrogram(lmatrixtp, labels = labels)
plt.savefig("dendrogram.png")
plt.close()


kmeans = KMeans(n_clusters = 7, random_state = 0)
kmeans.fit(matrix)
labels = kmeans.predict(matrix)
matrixdf = pd.merge(pd.DataFrame(matrix, columns = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']), pd.DataFrame(labels, columns=['cluster']), left_index = True, right_index = True )
kcluster = matrixdf.sort_values('cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values


plt.figure()
plt.imshow(kcluster, aspect = 'auto', interpolation = 'nearest')
plt.grid(False)
plt.colorbar()
plt.xticks( [ x for x in range(6) ], tlabels) 
plt.savefig("kclusteredheatmap.png")
plt.close()



early = [ 'CFU', 'mys', 'mid' ]
late = [ 'poly', 'unk', 'int' ]

df = pd.read_csv( sys.argv[1], sep='\t' ).dropna(how='any')
df['avge'] = df[early].mean(axis=1)
df['avgl'] = df[late].mean(axis=1)
t_stat,p_val = stats.ttest_ind(df[early],df[late], axis=1)
df['p_value'] = p_val
df['ratio'] = df['avge'] / df['avgl']
df = df.mask( df['p_value'] > 0.05 ).dropna()
down = df.mask( df['ratio'] > 0.5 ).dropna()
up = df.mask( df['ratio'] < 2.0 ).dropna()
newdf= pd.concat([down, up])[['gene','ratio','p_value']].sort_values('p_value')
print newdf.to_csv(index=False,sep='\t')
