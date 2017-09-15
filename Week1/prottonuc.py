#!/usr/bin/env python
"""
Usage: ./prottonuc.py <1000_homologs.fa> <alignment_prot.fa>
"""
import sys
import fasta
import itertools

nuc = open(sys.argv[1])
prot = open(sys.argv[2])
afile = open("alignmentnew.fa", "w")

for (nident, nseq), (pident, pseq) in itertools.izip(fasta.FASTAReader(nuc), fasta.FASTAReader(prot)):
    position = 0
    for p in pseq:
        if p == "-":
            afile.write("---")
        else:
            afile.write(nseq[position:position + 3])
            position = position + 3
    afile.write("\n")
    print afile

