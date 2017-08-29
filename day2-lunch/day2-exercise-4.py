#!/usr/bin/env python

import sys

fh = sys.stdin

count = 0

for line in fh:
    if line.startswith("@"):
        continue
    else:
        fields = line.split("\t")
        count = count + 1
        if count <= 10:
            print str(fields[2])
        else:
            break