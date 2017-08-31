#!/usr/bin/env python

"""
Usage: ./02-filter.py <ctab> <chr> <FPKM>

- Filter for transcripts on chr with abundance > FPKM
"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep = "\t")

roi1 = df["FPKM"] > int(sys.argv[3])
roi2 = df["chr"] == sys.argv[2]

print df[roi1 & roi2]