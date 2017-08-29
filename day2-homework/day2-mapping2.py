#!/usr/bin/env python

# Import sys
import sys

# Use open to access the file from mapping 1 info
f = open( sys.argv[1])
# Use to create a dictionary for mapping 1 info
flydict = {}
# Creating the dictionary
for line in f:
    col = line.rstrip("\r\n").split("\t")
    flybase = col[0]
    ac = col[1]
    # Make sure every FlyBase ID is added to dictionary from mapping 1
    if flybase not in flydict:
        flydict[flybase] = [ac]
# To check that dictionary was created
## for key, value in flydict.iteritems():
##     print key, value

# Use to access t_data.ctab file from cat program
s = sys.stdin
# To stop writing after 100 lines of output
count = 0

for line in s:
    # Access the FlyBase ID in ctab data
    fields = line.rstrip("\r\n").split("\t")
    # Removes the header of ctab data
    if fields[8] == "gene_id":
        continue
    # Searches for a match to FlyBase ID in ctab data in flydict
    for fields[8] in flydict:
        # Stops printing after 100 lines of output
        if count <= 100:
            # Prints the line corresponding to the matched FlyBase ID along with the AC, the corresponding values in the dictionary
            print line.strip("\r\n"), "\t", flydict[fields[8]][0]
            # Increases count to allow program to stop after 100 lines of output
            count = count + 1