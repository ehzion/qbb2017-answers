#!/usr/bin/env python

# Print the unique gene names from a t_data.ctab file

import sys

# gene_names_seen = []
# gene_names_seen = set()
gene_names_count = {}

for i, line in enumerate( sys.stdin ):
    if i == 0:
        continue
    # Remove any new lines from end of line, 
    # Then split using tab as delimeter
    # --> List of strings representig fields
    fields = line.rstrip("\r\n").split("\t")
    gene_name = fields[9]
    t_name = fields[5]
    if gene_name not in gene_names_count:
        # gene_names_count[gene_name] = 1
        gene_names_count[gene_name] = [t_name]
    else:
        # gene_names_count[gene_name] += 1
        gene_names_count[gene_name].append(t_name)
        
for key, value in gene_names_count.iteritems():
    print key, value
     