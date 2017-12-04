#!/usr/bin/python

import sys

checksum = 0

with open("spreadsheet.txt")as f:
       lines = f.read().splitlines()

for l in lines:
    numbers = map(int, l.split('\t'))
    
    for n in numbers:
        for m in numbers:
            if m != n:
                if m%n == 0:
                    checksum += m/n

print checksum


