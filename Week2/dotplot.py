#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

f = open(sys.argv[1])

count = 1
plt.figure()

for i in f:
    if "zstart1" in i:
        continue
    else:
        fields = i.split("\t")
        plt.plot([count, count+float(fields[3])], [float(fields[0]), float(fields[1])])
        count += float(fields[3])
        
plt.xlabel("")
plt.ylabel("")
plt.ylim((0, 100000))
plt.xlim((0, 100000))

plt.savefig(sys.argv[2] + ".png")
plt.close
