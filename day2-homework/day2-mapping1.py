#!/usr/bin/env python

# Import sys
import sys

# Use standard input for file, will use cat to pipe to code
f = sys.stdin

# Use to print first 100 lines
count = 0 

for line in f:
    # Eliminates any line not containing DROME
    if "DROME" not in line:
        continue
    # Eliminates the lines with no FlyBase ID
    if "FBgn" not in line:
        continue
    else:
        # Splits row into individual strings
        row = line.split() 
        # Ensures only 100 lines of output
        if count <= 100:
            # Using negative indexes takes the last two entries, the FlyBase ID and AC
            print row[-1], "\t", row[-2]
            # Keeps count of lines, stops program after 100
            count = count + 1