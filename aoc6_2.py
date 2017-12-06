#!/usr/bin/python

import sys

cycles = 0
states = []
states_cycles = []

with open("banks_full.txt") as f:
       lines = f.read().splitlines()

banks = map(int, lines[0].split('\t'))

while True:
    # If state has been seen previously, break
    if banks in states:
        print "Found %s (cycle %d) again at cycle %d. Difference: %d" % ( banks, states.index(banks), cycles, cycles-states.index(banks) )
        break

    # Save state of banks
    states.append(list(banks))
    states_cycles.append(cycles)
    
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

