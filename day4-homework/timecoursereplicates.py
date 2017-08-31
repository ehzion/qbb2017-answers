#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <samples.csv> <ctab_dir>
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples = pd.read_csv(sys.argv[1])
soi = df_samples["sex"] == "female"

fpkms = []
for sample in df_samples["sample"][soi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep = "\t")
    roi = df["t_name"] == transcript
    fpkms.append(df[roi]["FPKM"].values)
    
    
soi2 = df_samples["sex"] == "male"

fpkms2 = []
for sample in df_samples["sample"][soi2]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep = "\t")
    roi2 = df["t_name"] == transcript
    fpkms2.append(df[roi2]["FPKM"].values)
    

   
df_replicates = pd.read_csv(sys.argv[3])
repoi = df_replicates["sex"] == "female"

fpkms3 = []
for sample in df_replicates["sample"][repoi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df2 = pd.read_csv(fname, sep = "\t")
    repoi = df2["t_name"] == transcript
    fpkms3.append(df2[repoi]["FPKM"].values)
    
repoi2 = df_replicates["sex"] == "male"

fpkms4 = []
for sample in df_replicates["sample"][repoi2]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df2 = pd.read_csv(fname, sep = "\t")
    repoi2 = df2["t_name"] == transcript
    fpkms4.append(df2[repoi2]["FPKM"].values)


labelx = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
x = [0, 1, 2, 3, 4, 5,  6, 7]
#w = [fpkms3[0], fpkms3[1], fpkms3[2], fpkms3[3]]
#z = [fpkms4[0], fpkms4[1], fpkms4[2], fpkms4[3]]
   
plt.figure()
plt.plot(fpkms, c = "red")
plt.plot(fpkms2, c = "blue")
d, = plt.plot([4, 5, 6, 7], fpkms3, 'o', c = "red", label = 'Female Replications') 
h, = plt.plot([4, 5, 6, 7], fpkms4, 'o', c = "blue", label = 'Male Replications')
plt.xticks(x, labelx, rotation='horizontal')
plt.ylim(0, 300)
plt.title("Sxl\n", style = 'italic', fontsize = 20)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance(RPKM)")
r, = plt.plot(fpkms, c = "red", label = 'Female')
b, = plt.plot(fpkms2, c = "blue", label = 'Male')
plt.legend([r, b, d, h], ['Female', 'Male','Female Replications', 'Male Replications'])
plt.savefig("timecoursemf.png")
plt.close()