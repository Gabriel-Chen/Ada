#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Math 115A lecture section begins at 08:00 at MS 5147. " > ./push.txt

mutt -s "Class to Catch" A < push.txt
