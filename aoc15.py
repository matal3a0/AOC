#!/usr/bin/python

def gen_a(a):
    fa = 16807
    div = 2147483647
    return (a * fa) % div

def gen_b(b):
    fb = 48271
    div = 2147483647
    return (b * fb) % div


mask = 0xffff
a = 634
b = 301
matches = 0

for i in range(0,40000000):
    a = gen_a(a)
    b = gen_b(b)
    if bin(a & mask) == bin(b & mask):
        matches += 1

print "Matches:",matches
 
