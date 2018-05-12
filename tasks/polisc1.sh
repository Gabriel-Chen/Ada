#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Polisci 1 begins at 9:30 untill 12:20 in BCC 423. " > ./push.txt

mutt -s "Class to Catch" me < push.txt
