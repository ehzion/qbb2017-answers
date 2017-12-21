#!/usr/bin/env python


"""
./heatmap_week13.py abundance_table.tab
"""

import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(sys.argv[1],sep='\t',index_col=0)


samples = ['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']

dfsamples = df[samples]

labels = {"bin.1":'Staphylococcus haemolyticus',"bin.2":'Leuconostoc citreum',"bin.3":'Staphylococcus lugdunensis',"bin.4":'Enterococcus faecalis',"bin.5":'Cutibacterium avidum',"bin.6":'Staphylococcus epidermidis',"bin.7":'Staphylococcus aureus',"bin.8":"Anaerococcus prevotii"}

bins = []

for i in dfsamples.index.tolist():
    bins.append(labels[i])





plt.figure()
plt.imshow(dfsamples, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Newborn Gut Bacteria ")
plt.colorbar()
plt.xticks( range(len( dfsamples.columns)), dfsamples.columns, rotation = 'vertical')
plt.yticks( [ x for x in range(len(bins)) ], bins)
plt.tight_layout()
plt.savefig("heatmap.png")
plt.close()