#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Computing 10A lecture section begins at 10:00 at Mathematical Sciences 5200. " > ./push.txt

mutt -s "Class to Catch" A < push.txt
