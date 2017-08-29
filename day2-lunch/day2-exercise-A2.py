#!/usr/bin/env python

import sys

fh = sys.stdin

count = 0
   
for line in fh:
    if line.startswith("@"):
        continue
    else:
        fields = line.split("\t")
        if fields[2] == "2L" and (int(fields[3]) >= 10000) and (int(fields[3]) <= 20000):
            count = count + 1
        else:
            continue
print count