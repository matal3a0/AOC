#!/usr/bin/python

def isAnagram(a,b):
    return sorted(a) == sorted(b)
    
def main():
    with open("passphrases_full.txt") as f:
       lines = f.read().splitlines()

    valids = 0

    for l in lines:
        valid = True
        passphrase = []
        perms = []

        for w in l.split(): # Split line into list of words
            passphrase.append(w)

        for i in range(0, len(passphrase)):
            # Compare to rest of words
            for j in range(i+1, len(passphrase)):
                if isAnagram(passphrase[i], passphrase[j]):
                    valid = False
                    break
        if valid:
            valids += 1
            

    print "Valids:",valids

if __name__ == '__main__':
    main()
