#!/usr/bin/python

instructions = []

with open("instructions.txt") as f:
       lines = f.read().splitlines()

for l in lines:
    instructions.append(int(l))

pos = 0
steps = 0
while True:
    steps += 1
    from_pos = pos
    jump = instructions[pos]
    pos = pos + jump
    if pos >= len(instructions): # If outside instructions
        break
    
    if jump >= 3:
        instructions[from_pos] -= 1
    else:
        instructions[from_pos] += 1



print "Steps: ",steps    

