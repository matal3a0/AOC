#!/usr/bin/python

import sys

def readfile(fname):
    with open(fname) as f:
        return f.readline().split(',')

def spin(s,x):
    for i in range(0, x):
        s = s[-1] + s[:-1]
    return s

def exchange(s,a,b):
    tmpa = s[a]
    tmpb = s[b]
    s = s.replace(s[a],'x')
    s = s.replace(s[b],'y')
    s = s.replace(s[a],tmpb)
    s = s.replace(s[b], tmpa)
    return s

def partner(s,a,b):
    s = s.replace(a,'x')
    s = s.replace(b,'y')
    s = s.replace('x', b)
    s = s.replace('y', a)
    return s

def main():
    if len(sys.argv) == 1:
        print "No input"
        sys.exit(1)


    programs = 'abcdefghijklmnop'

    instructions = readfile(sys.argv[1])

    for i in instructions:
        if i[0] == 'x':
            print i, i.split('/')[0].replace('x','')
            programs = exchange(programs, int(i.split('/')[0].replace('x','')), int(i.split('/')[1]))
        if i[0] == 'p':
            programs = partner(programs, i[1], i[3])
        if i[0] == 's':
            #programs = spin(i[0].split('/')[1])
            print i
            programs = spin(programs, int(i.split('s')[1]))

    print programs
if __name__ == '__main__':
    main()
