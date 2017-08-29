#!/usr/bin/env python

import sys

fh = sys.stdin

fwd = 0
rev = 0
        
for line in fh:
    if line.startswith("@"):
        continue
    else:
        fields = line.split("\t")
        if int(fields[1]) == 16:
            rev = rev + 1
        else:
            fwd = fwd + 1
print "Forward:" + str(fwd)
print "Reverse:" + str(rev)
