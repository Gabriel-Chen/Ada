#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Econ 11 lecture section begins at 14:00 at Broad Art Center 2160E. " > ./push.txt

mutt -s "Class to Catch" A < push.txt
