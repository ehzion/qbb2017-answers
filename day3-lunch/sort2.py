#!/usr/bin/env python

import random

r = random.randint(1, 100)

nums = range(0, 100, 10)
print nums

key = 90

first = 0
last = len(nums)

found = False

while first < last and not found:
    midpoint = (first + last) / 2
    print "Checking in the range [%d, %d] midpoint[%d]=%d" % (first, last, midpoint, nums[midpoint])
    if nums[midpoint] == key:
        found = True
        print "Found %d at %d" % (key, midpoint)
    elif key > nums[midpoint]:
        first = midpoint + 1
    else:
        last = midpoint
