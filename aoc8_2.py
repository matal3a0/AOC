#!/usr/bin/python

import sys

def readFile(fname):
    with open(fname) as f:
       return f.read().splitlines()

def compare(a, b, op):
    if op == "<":
        return a < b
    elif op == ">":
        return a > b
    elif op == "==":
        return a == b
    elif op == ">=":
        return a >= b
    elif op == "<=":
        return a <= b
    elif op == "!=":
        return a != b
    else:
        return "Unknown operation:",op

def calcchange(a,b,op):
    if op == "inc":
        return a+b
    elif op == "dec":
        return a-b
    else:
        return "Unknown operation",op

def position(name, registers):
    for i in range(0, len(registers)):
        if registers[i][0] == name:
            return i
    return -1

def findLargest(registers):
    largest = 0
    for i in range(0, len(registers)):
        if registers[i][1] > largest:
            largest = registers[i][1]
    return largest

def process(instructions):
    registers = []
    change = 0
    highest = 0

    for instruction in instructions:
        i = instruction.split(' ')
        rega = i[0]
        changeop = i[1]
        changeval= int(i[2])
        regb = i[4]
        compop = i[5]
        compval= int(i[6])

        # Find position of register a i registers
        # If not found, append
        posa = position(rega,registers)
        if posa < 0:
            reg = [rega,0]
            registers.append(reg)
            posa = len(registers)-1

        # Same for register b
        posb = position(regb,registers)
        if posb < 0:
            reg = [regb,0]
            registers.append(reg)
            posb = len(registers)-1
       
        # If comparison is True, change value of register a
        if compare(registers[posb][1], compval, compop):
            registers[posa][1] = calcchange(registers[posa][1], changeval, changeop)
            if registers[posa][1] > highest:
                highest = registers[posa][1]

    print "Highest:",highest


def main():
    if len(sys.argv) == 1:
        print "No input"
        sys.exit(1)

    instructions = readFile(sys.argv[1])
    process(instructions)


if __name__ == '__main__':
    main()

