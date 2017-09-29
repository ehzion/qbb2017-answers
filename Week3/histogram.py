#!/usr/bin/env python

import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

f = open(sys.argv[1])

allelefreq = []

for i in f:
    if i.startswith("#"):
        continue
    line = i.rstrip("\t\n").split()
    afreq = line[7].split(";")
    afreq2 = afreq[3][3:]
    if "," in afreq2:
        afreq3 = afreq2.split(",")
        for i in afreq3:
            allelefreq.append(float(i))
    else:
        allelefreq.append(float(afreq2))
        
plt.figure()
plt.hist(allelefreq, bins=20)
plt.savefig(sys.argv[2] + ".png")
plt.close