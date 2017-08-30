#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and prints it.

usage: ./00-parse-one-fasta.py < input.fa > output
"""

import sys

line = sys.stdin.readline()
# Verify it is a header line
assert line.startswith(">")

# Extract identifier
# ident = line.split()[0].lstrip(">")
ident = line.split()[0][1:]

sequences = []

while True:
    line = sys.stdin.readline().rstrip("\r\n")
    if line == "" or line.startswith(">"):
        break
    else:
        sequences.append(line)

print ident, "".join(sequences)
        