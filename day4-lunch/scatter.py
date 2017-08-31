#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv(sys.argv[1], sep = "\t")
coi1 = ["t_name", "FPKM"]

print df1[coi1].head()

df2 = pd.read_csv(sys.argv[2], sep = "\t")
coi2 = ["t_name", "FPKM"]

print df2[coi2].head()