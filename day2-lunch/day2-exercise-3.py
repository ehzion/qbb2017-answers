#!/usr/bin/env python

import sys

fh = sys.stdin

total = 0
for line in fh:
    if "NH:i:1" in line:
        total = total + 1
    else:
        continue
    print total