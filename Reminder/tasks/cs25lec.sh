#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW . You will have Compsci 25 lecture begins at 9:00 untill 11:50 in BCC 226. " > ./push.txt

mutt -s "Class to Catch" me < push.txt
