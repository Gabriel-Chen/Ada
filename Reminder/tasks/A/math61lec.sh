#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Math 61 lecture section begins at 12:00 at Dodd Hall 147. " > ./push.txt

mutt -s "Class to Catch" A < push.txt
