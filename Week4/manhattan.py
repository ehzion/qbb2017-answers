#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

f = open(sys.argv[1])

sig = []
notsig = []

line = 5
for i in f:
    fields = i.split()
    if "CHR" in i:
        continue
    elif "NA" in i:
        continue
    line += 1

for i in range(line):
    sig.append(None)
    notsig.append(None)


count = 0
f.seek(0)
for i in f:
    fields = i.split()
    if "CHR" in i:
        continue
    elif "NA" in i:
        continue
    elif "ADD" not in i:
        continue
    elif float(fields[8]) <= 10e-5:
        sig[count] = -np.log10(float(fields[8]))
        count += 1
    elif float(fields[8]) > 10e-5:
        notsig[count] = -np.log10(float(fields[8]))
        count += 1

plt.figure()
plt.scatter(range(len(sig)), sig, s=5, alpha=.6, c= "red")
plt.scatter(range(len(sig)), notsig, s=5, alpha=.6, c = "blue")
plt.xlabel("Gene Locations")
plt.ylabel("-log10(p)")
plt.savefig(str(sys.argv[2]) + "mplot.png")
plt.close()

f.close()