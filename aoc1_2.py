#!/usr/bin/python

import sys

line = sys.argv[1]
strlen = len(sys.argv[1])
half = strlen/2
sum = 0

for i in range(0, int(strlen)):
    a = line[i]
    b = line[(i+half)%strlen]

    if a == b:
        sum += int(a)

print sum

