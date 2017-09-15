#!/usr/bin/env python

"""
Usage: ./plot.py <dsdn.out> <nameofplot>
"""

import pandas as pd
import sys
import matplotlib.pyplot as plt
import statsmodels
import numpy as np


df = pd.read_csv(sys.argv[1], sep = "\t", header=None, names=["codon", "dNdS", "d"])

## Z = d /sqrt(var d)

stddev = np.std(df["d"])
zscore = []
for i in df["d"]:
    z = i/stddev
    zscore.append(z)
#print zscore

x = range(len(df["d"]))
y = df["dNdS"]

color = []

for i in range(len(zscore)):
    if zscore[i] > 1.96:
        color.append("r")
    else:
        color.append("b")


plt.figure()
plt.scatter(x, y, c = color, s = 15)
plt.title("Sequence Alignment and Evolution")
plt.xlabel("Codon")
plt.ylabel("dN/dS", rotation = 90)
plt.savefig(sys.argv[2] + ".png")
plt.close()