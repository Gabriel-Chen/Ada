#!/bin/sh

NOW=$(date +"%T")

echo "Now is $NOW. You will have Philo 1 begins at 13:30 untill 14:45 in BCC 423. " > ./push.txt

mutt -s "Class to Catch" me < push.txt
