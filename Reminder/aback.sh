#!/bin/sh

NOW=$(date +%"c")
DATE=$(date +%"d")
count=$(expr 10 - $DATE)

echo "Now is $NOW . A is going to come back in $count days. " > ./push.txt

mutt -s "A Coming Back" me < push.txt
