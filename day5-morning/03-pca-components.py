#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv(sys.argv[1], index_col = 0)

n, p = df.shape

sexes = []
for colname in df.columns.values.tolist():
    sex, stage = colname.split("_")
    if "female" in sex:
        sexes.append("orange")
    else:
        sexes.append("green")

pca = PCA()

df = df.T

fit = pca.fit(df)

x = fit.transform(df)



plt.figure()
plt.scatter(x[:,0], x[:,1], alpha = 0.8, c = sexes)
plt.savefig(sys.argv[2])
plt.close()
