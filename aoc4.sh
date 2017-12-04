#!/bin/bash
COUNTER=0

while read LINE; do
  if [ $(echo "$LINE" | tr " " "\n" | sort | uniq -d | wc -l) -eq 0 ]; then
    let COUNTER=COUNTER+1
  fi
done < passwords.txt
echo "Valid: $COUNTER"
