#!/usr/bin/env python

"""
Usage: ./00-reorder.py <csv_file> <tsv_file>

- Remove header
- Reorder columns: sex, sample, stage
- Subset "female" in sex column
- Convert delimeter from comma to tab

"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
# Specify desired column order
coi = ["sex", "sample", "stage"]
#print df[coi]
roi = df["sex"] == "female"
df[coi][roi].to_csv(sys.argv[2], sep = '\t', header = False, index = False)


#f = open(sys.argv[1])

#for i, line in enumerate(f):
#    if i ==0:
#        continue
#    fields = line.rstrip("\r\n").split(",")
#    if fields[1] == "female":
#        print "\t".join([fields[1], fields[0], fields[2]])
        
#f.close()