#!/usr/bin/env python

# Import sys
import sys

argument = sys.argv[2]
# Use open to access the file from mapping 1 info
f = open( sys.argv[1])
# Use to create a dictionary for mapping 1 info
flydict = {}
# Creating the dictionary
for line in f:
    col = line.rstrip("\r\n").split("\t")
    # Had to delete an extra space that was introduced
    flybase = col[0][:-1]
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
    # Argument to skip lines
    if argument == "skip":
        # Finds FlyBase ID in flydict
        if fields[8] in flydict:
            # Stops printing after 100 lines of output
            if count <= 100:
                # Changes FlyBase ID to AC
                fields[8] = flydict[fields[8]][0]
                # Rejoins fields creating a new line with change above
                print "\t".join(fields)
                # Increases count to allow program to stop after 100 lines of output
                count = count + 1
    # Argument to replace with default value
    if argument == "defv":
        # Stops printing after 100 lines of output
        if count <= 100:
            # Finds FlyBase ID in flydict
            if fields[8] in flydict:
                # Rejoins fields creating a new line with change above
                fields[8] = flydict[fields[8]][0]
                # Rejoins fields creating a new line with change above
                print "\t".join(fields)
                # Increases count to allow program to stop after 100 lines of output
                count = count + 1
            else:
                # If FlyBase ID is not in flydict, replaces with N/A
                fields[8] = "N/A"
                # Rejoins fields creating a new line with change above
                print "\t".join(fields)
                # Increases count to allow program to stop after 100 lines of output
                count = count + 1
            
