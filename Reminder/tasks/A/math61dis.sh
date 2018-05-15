#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Math 61 discussion section begins at 12:00 at Bunche Hall 3143. " > ./push.txt

mutt -s "Class to Catch" A < push.txt
