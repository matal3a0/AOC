#!/usr/bin/python
import sys,time

def parseInput(fname):
    with open(fname) as f:
       lines = f.read().splitlines()

    paths = [] 
    for line in lines:
        paths.append(list(line))

    return paths

def turn(paths, x, y, d):
    #boy this is ugly!
    if d == 's' or d == 'n':
        #turn east or west
        try:
            if paths[y][x+1] != ' ':
                return 'e'
            else:
                return 'w'
        except IndexError:
            return 'w'
    else:
        #turn north or south
        try:
            if paths[y+1][x] != ' ':
                return 's'
            else:
                return 'n'
        except IndexError:
            return 'n'

def main():
    if len(sys.argv) == 1:
        print "No input"
        sys.exit(1)

    paths = parseInput(sys.argv[1])        
    d = 's'
    steps = 0
    x = paths[0].index('|')
    y = 0

    while True:
        if paths[y][x] == ' ':
            print "Steps:",steps
            break
        elif paths[y][x].isalpha():
            print paths[y][x],
        if d == 's':
            y += 1
        elif d == 'n':
            y -= 1
        elif d == 'w':
            x -= 1
        elif d == 'e':
            x += 1

        if paths[y][x] == '+':
            d = turn(paths, x, y, d)
        steps += 1
    


if __name__ == '__main__':
    main()
