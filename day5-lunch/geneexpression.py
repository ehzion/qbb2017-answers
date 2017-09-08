#!/usr/bin/env python

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], sep = "\t")
soip = df["strand"] == "+"
soin = df["strand"] == "-"
#coi = ["chr", "p_start", "p_end", "t_name"]

dfp = pd.DataFrame()
dfn = pd.DataFrame()


for strand in df[soip]:
    dfp["chromosome"] = df["chr"][soip]
    dfp["p_start"] = df["start"][soip] - 500
    dfp["p_end"] = df["start"][soip] + 500
    dfp["t_name"] = df["t_name"][soip]
    
for strand in df[soin]:
    dfn["chromosome"] = df["chr"][soin]
    dfn["p_start"] = df["end"][soin] - 500
    dfn["p_end"] = df["end"][soin] + 500
    dfn["t_name"] = df["t_name"][soin]

dfall = dfp.append(dfn)

num = dfall._get_numeric_data()
num[num<0] = 0


dfall.to_csv(sys.argv[2], sep ="\t", index = False, header = False)