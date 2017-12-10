#!/usr/bin/python

import sys,re, string

if len(sys.argv) < 2:
    print "No input"
    sys.exit(1)

fname = sys.argv[1]

with open(fname) as f:
        line = f.readline()

ptr = 0
level = 0
score = 0
inside_garbage = False

while ptr < len(line):
    if line[ptr] == '!': 
        ptr += 1
    elif line[ptr] == '<':
        inside_garbage = True
    elif inside_garbage:
        if line[ptr] == '>':
            inside_garbage = False
    elif line[ptr] == '{':
        level += 1
    elif line[ptr] == '}':
        score += level
        level -= 1
    ptr += 1

print "score:",score
