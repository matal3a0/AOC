#!/usr/bin/python

import sys

checksum = 0

with open("spreadsheet.txt")as f:
       lines = f.read().splitlines()

for l in lines:
    numbers = map(int, l.split('\t'))
    smallest = numbers[0]
    largest = numbers[0]
    
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n

    checksum += (largest - smallest)

print checksum


