#!/usr/bin/python

def generator(x,fx,mod=1):
    div = 2147483647
    while True:
        x = (x * fx) % div
        if x % mod == 0:
            yield x

matches = 0
gen_a = generator(634, 16807, 4)
gen_b = generator(301, 48271, 8)
#gen_a = generator(65, 16807, 4)
#gen_b = generator(8921, 48271, 8)

for i in range(0,5000000):
    if gen_a.next() & 0xffff == gen_b.next() & 0xffff: 
        matches += 1

print "Matches:",matches
 
