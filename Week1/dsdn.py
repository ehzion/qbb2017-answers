#!/usr/bin/env python

"""
Usage: ./dsdn.py <alignmentnew.fa>
"""

import sys
import numpy as np



bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))
## Source: http://www.petercollingridge.co.uk/python-bioinformatics-tools/codon-table

def codon(line):
    return [line[i:i+3] for i in range(0, len(line), 3)]

align = open(sys.argv[1])

refline = codon(align.readline())

dS = np.zeros(len(refline))
dN = np.zeros(len(refline))

for line in align:
    for index, (cd, ref) in enumerate(zip(codon(line), refline)):
        if cd == ref:
            continue
        if ref not in codon_table:
            continue
        if cd not in codon_table:
            continue
        if codon_table[cd] == codon_table[ref]:
            dS[index] += 1 
        else:
            dN[index] += 1 
            
d = dN - dS

for i in range(len(refline)):
    if dS[i] > 0:
        print ("%s \t %f \t %f") % (refline[i], dN[i]/dS[i], d[i])
        
        
