#!/usr/bin/env python

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], sep = "\t")
soip = df["strand"] == "+"
soin = df["strand"] == "-"
coi = ["chr", "p_start", "p_end", "t_name"]

for strand in df["strand"][soip]:
    df["p_start"] = df["start"] - 500
    df["p_end"] = df["start"] + 500
for strand in df["strand"][soin]:
    df["p_start"] = df["end"] - 500
    df["p_end"] = df["end"] + 500

num = df._get_numeric_data()
num[num<0] = 0

df[coi].to_csv(sys.argv[2], sep ="\t", index = False, header = False)