#!/usr/bin/env python

import sys
import fasta
import numpy as np


f = open(sys.argv[1])

nseqs = []

for ident, sequence in fasta.FASTAReader(f):
    nseqs.append(sequence)

print "Number of contigs = " + str(len(nseqs))
    
nlength = []

for i in range(len(nseqs)):
    nlength.append(len(nseqs[i]))
    
nlength.sort()
    
print "Max = " + str(max(nlength))
print "Min = " + str(min(nlength))

clength = 0

for i in nlength:
    clength += i
    
count = 0
pos = 0

for i in nlength:
    if count < clength/2:
        count += i
        pos += 1
    else:
        print "N50 = " + str(nlength[(int(pos) - 1)])
        break

print "Mean = " + str(np.mean(nlength))