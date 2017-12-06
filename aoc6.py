#!/usr/bin/python

import sys

cycles = 0
states = []

with open("banks.txt") as f:
       lines = f.read().splitlines()

banks = map(int, lines[0].split('\t'))

while True:
    # If state has been seen previously, break
    if banks in states:
        break

    # Save state of banks
    states.append(list(banks))
    
    # Find biggest value and its position
    value = max(banks)
    index = banks.index(value)
    # Replace with 0
    banks[index] = 0
    
    # Distribute value over banks
    while value > 0:
        index += 1 # Move forward

        if index >= len(banks): # Wrap around
            index = 0

        banks[index] += 1 # Increase value in list
        value -= 1 # Decrease value

    cycles += 1 # Increase cycles

print cycles


