#!/usr/bin/env python

import sys
import fasta

"""
kmer_matcher.py <target.fa> <query.fa> <k>
"""
# Set up arguments
target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])
# Make dictionary
kmer_dict = {}

# Used fasta reader to get ident, sequence, from target to use to create dictionary
for ident, sequence in fasta.FASTAReader(target):
    # Makes all of the sequence uppercase
    sequence = sequence.upper()
    # I is position, creates kmer
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i+k]
        # Adds kmer to dictionary as key, ident and position as value
        if kmer not in kmer_dict:
            kmer_dict[kmer] = []
            kmer_dict[kmer].append((ident, i)) 
        # Adds additional values to existing dictionary keys
        else:
            kmer_dict[kmer].append((ident, i))
            
# Used to print 1000 lines of output      
count = 0

# Used fasta reader to get a sequence to form kmers from query (kmerQ) to compare to dictionary
for sequence in fasta.FASTAReader(query).next():
    # I is position, creates kmerQ
    for i in range(0, len(sequence) - k):
        kmerQ = sequence[i:i+k]
        # Finds kmerQ in kmer dictionary
        if kmerQ in kmer_dict:
            if count < 1000:
                # Allows each multiple values for one key to print on separate lines
                for value in kmer_dict[kmerQ]:
                    # Count here allows for every value to be counted, not just the kmer
                    count += 1
                    # Value[0] and Value[1] prints the ident and position from dictionary, i is position from query, kmerQ is the kmer used in comparison
                    print "\t".join((str(value[0]), str(value[1]), str(i), kmerQ))
