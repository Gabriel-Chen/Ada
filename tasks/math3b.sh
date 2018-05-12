#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Math 3B begins at 15:00 untill 17:15 in Suit 2. " > ./push.txt

mutt -s "Class to Catch" me < push.txt
