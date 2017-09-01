#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

tab = open(sys.argv[1])
avg = []
for line in tab:
    fields = line.rstrip("\r\n").split()
    avg.append(float(fields[4]))

fpkms = []
df = pd.read_csv(sys.argv[2], sep = "\t")
fpkms = df["FPKM"].values.tolist()

#print len(fpkms), len(avg)

x = avg
y = fpkms

model = sm.OLS(x, y)
results = model.fit()
print (results.summary())