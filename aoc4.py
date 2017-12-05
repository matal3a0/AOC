#!/usr/bin/python

with open("passphrases.txt") as f:
       lines = f.read().splitlines()

valids = 0

for l in lines:
    is_valid=True
    passphrase = []
    passphrase_dupes = []

    for w in l.split(): # Split line into list of words
        passphrase.append(w)

    for p in passphrase: # Check for duplicates
        if p in passphrase_dupes:
            is_valid=False
            break
        else:
            passphrase_dupes.append(p)

    if is_valid:
        valids += 1

print "Valid passwords:",valids

