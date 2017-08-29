#!/usr/bin/env python

import sys

fh = sys.stdin

total = 0
for line in fh:
    if "NM:i:0" in line:
        total = total + 1
    else:
        continue
    print total