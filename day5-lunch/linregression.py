#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

#tab = open(sys.argv[1])
avg = []
dfavg = pd.read_csv(sys.argv[1], sep = "\t", header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
dfavg = dfavg.sort_values("t_name")
avg = dfavg["mean0"].values.tolist()
#print avg
    #fields = line.rstrip("\r\n").split()
    #avg.append(float(fields[4]))

fpkms = []
df = pd.read_csv(sys.argv[2], sep = "\t")
df = df.sort_values("t_name")
fpkms = df["FPKM"].values.tolist()
#print fpkms
#print len(fpkms), len(avg)

x = avg
y = fpkms

model = sm.OLS(x, y)
results = model.fit()
print (results.summary())