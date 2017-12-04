#!/usr/bin/python

import sys

line = sys.argv[1]
strlen = len(sys.argv[1])
sum = 0

for i in range(0, int(strlen)):
    a = line[i]
    b = line[(i+1)%strlen]
#    if i == strlen-1:
#        b = line[0] 
#    else:
#        b = line[i+1]
#
    if a == b:
        sum += int(a)

print sum

