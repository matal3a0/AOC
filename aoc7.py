#!/usr/bin/python

import sys

class Program:

    def __init__(self, name, weight=0, parent=None):
        self.name = name
        self.weight = weight
        self.parent = parent

    def printProgram(self):
        print "Name:",self.name
        print "Weight:",self.weight
        if not self.parent == None:
            print "Parent: ", self.parent.name
        else:
            print "-"

    def updateParent(self, program):
        self.parent = program


def searchProgram(programs,name):
    for p in programs:
        if p.name == name:
            return p
    return None

def readFile(fname):
    with open(fname) as f:
       return f.read().splitlines()

def parseInput(file):
    lines = readFile(file)
    programs = []
    # Add all programs
    for line in lines:
        words = line.split(' ')
        programs.append(Program(words[0],words[1].translate(None, '()')))
    
    # Update parents
    for line in lines:
        words = line.split(' ')
        if len(words) > 2:
            parent = searchProgram(programs,words[0])
            for c in range(3, len(words)):
                child = searchProgram(programs,words[c].translate(None, ','))
                child.updateParent(parent)

    return programs

def main():
    if len(sys.argv) == 1:
        print "No input"
        sys.exit(1)

    programs = parseInput(sys.argv[1])

    for p in programs:
        if p.parent == None:
            print "Bottom: ",p.name

    
    
if __name__ == '__main__':
    main()


