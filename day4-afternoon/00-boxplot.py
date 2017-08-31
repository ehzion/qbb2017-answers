#!/usr/bin/env python

"""
Usage: ./00-boxplot.py <samples.csv> <ctab_dir>

- Boxplot distribution of Sxl transcript in female
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_samples = pd.read_csv(sys.argv[1])
soi = df_samples["sex"] == "female"

df_gene = pd.DataFrame()
for sample in df_samples["sample"][soi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep = "\t")
    roi = df["gene_name"] == "Sxl"
    df_gene[sample] = np.log(df[roi]["FPKM"] + 1)
    
#print df_gene
    
plt.figure()
plt.boxplot(df_gene.values)
plt.savefig("boxplot.png")
plt.close()