#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Econ 11 discussion section begins at 16:00 at Bunche HAll 3211. " > ./push.txt

mutt -s "Class to Catch" A < push.txt
