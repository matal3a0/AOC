#!/usr/bin/python

import sys,math

address = int(sys.argv[1])

# Find square that will fit all numbers 1^2, 3^2, 5^2
sqr_count = 1
sqr = 1
while (sqr < address):
    sqr = math.pow(sqr_count, 2)
    sqr_count += 2
# Move counter back one step
sqr_count -= 2
size = int(math.ceil(sqr_count))  

# Init 2D-array with zeros
memory = [[0 for x in range(size)] for y in range(size)]

# Location of port (1)
port = int(sqr_count/2) 

# Populate array
a = 2 # start with two
posx = port # start at port
posy = port
direction = 'e' # start going east
memory[posy][posx] = 1 # insert 1 at port

# Loop until address
while (a <= address):
    if direction == 'e':
        posx += 1
        if memory[posy+1][posx] == 0:
            direction = 'n'
    elif direction == 'n':
        posy += 1
        if memory[posy][posx-1] == 0:
            direction = 'w'
    elif direction == 'w':
        posx -= 1
        if memory[posy-1][posx] == 0:
            direction = 's'
    elif direction == 's':
        posy -= 1
        if memory[posy][posx+1] == 0:
            direction = 'e'
    memory[posy][posx] = a
    a += 1

    #print "memory[" + str(posy) + "][" + str(posx) + "]"

# Calculate distance
if (posx < port):
    distx = port-posx
else:
    distx = posx-port

if (posy < port):
    disty = port-posy
else:
    disty = posy-port

dist = disty+distx
print "Distance: ", dist


