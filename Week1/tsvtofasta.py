#!/usr/bin/env python

import sys

f = open(sys.argv[1])

for line in f:
    fields = line.split("\t")
    print ">" + fields[0] + "\n" + fields[1]