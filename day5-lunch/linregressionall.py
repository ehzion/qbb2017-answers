#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

#tab = open(sys.argv[1])
avg1 = []
dfavg1 = pd.read_csv(sys.argv[1], sep = "\t", header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
dfavg1 = dfavg1.sort_values("t_name")
avg1 = dfavg1["mean0"].values.tolist()

avg2 = []
dfavg2 = pd.read_csv(sys.argv[2], sep = "\t", header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
dfavg2 = dfavg2.sort_values("t_name")
avg2 = dfavg2["mean0"].values.tolist()

avg3 = []
dfavg3 = pd.read_csv(sys.argv[3], sep = "\t", header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
dfavg3 = dfavg3.sort_values("t_name")
avg3 = dfavg3["mean0"].values.tolist()

avg4 = []
dfavg4 = pd.read_csv(sys.argv[4], sep = "\t", header = None, names = ["t_name", "size", "covered", "sum", "mean0", "mean"])
dfavg4 = dfavg4.sort_values("t_name")
avg4 = dfavg4["mean0"].values.tolist()

fpkms = []
df = pd.read_csv(sys.argv[5], sep = "\t")
df = df.sort_values("t_name")
fpkms = df["FPKM"].values.tolist()
#print fpkms
#print len(fpkms), len(avg)

totalavg = zip(avg1, avg2, avg3, avg4)
#print totalavg

y = totalavg
x = fpkms

model = sm.OLS(x, y)
results = model.fit()
print (results.summary())