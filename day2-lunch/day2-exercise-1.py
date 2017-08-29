#!/usr/bin/env python

import sys

fh = sys.stdin

total = 0
for line in fh:
    if line.startswith("@"):
        continue
    else:
        total = total + 1
    print total