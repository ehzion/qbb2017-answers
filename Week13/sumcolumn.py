#!/usr/bin/env python

import sys

f = open(sys.argv[1])

linedict = {}

for line in f:
    info = line.rstrip("\t\n").split("\t")[1]
    if info in linedict.keys():
        linedict[info] += 1
    else:
        linedict[info] = 1
        
for key in linedict.keys():
    print linedict[key], "\t".join(key.split(";"))
        