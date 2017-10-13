#!/usr/bin/env python

import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

"""

usage: ./allele_hist.py BYxRM_segs_saccer3.bam.simplified.vcf allele_hist.png

"""

vcf = open(sys.argv[1])

allele_freq = []
for i in vcf:
    if i.startswith("#"):
        continue
    line = i.rstrip("\t\n").split()
    alf = line[7]
    alf_2 = alf[3:]
    if "," in alf_2:
        alf_3 = alf_2.split(",")
        for i in alf_3:
            allele_freq.append(float(i))
    else:
        allele_freq.append(float(alf_2))
        
plt.figure()
plt.hist(allele_freq, bins = 100)
plt.xlabel("Allele")
plt.ylabel("Frequency")
plt.title("Allele Frequency Spectrum")
plt.savefig(sys.argv[2])
plt.close()
