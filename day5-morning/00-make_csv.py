#!/usr/bin/env python

"""
Read all stringtie outputs and write table of FPKM values

usage: ./00-make_csv.py <samples.csv> <base>
"""

import sys
import pandas as pd
import os

df = pd.read_csv(sys.argv[1])

d = {}

for index, sample, sex, stage in df.itertuples():
    sample_df = pd.read_csv(os.path.join( sys.argv[2], sample, "t_data.ctab"), sep = "\t", index_col = "t_name")
    
    d[sex + "_" + stage] = sample_df["FPKM"]
    
df = pd.DataFrame(d)

df.to_csv(sys.stdout)