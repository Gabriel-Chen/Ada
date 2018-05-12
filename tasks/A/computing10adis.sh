#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Computing 10A discussion section begins at 10:00 at Mathematical Sciences 6201. " > ./push.txt

mutt -s "Class to Catch" A < push.txt
