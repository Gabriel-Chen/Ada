#!/bin/sh

URL='http://www.accuweather.com/en/us/berkeley-ca/94704/weather-forecast/332044'

NOW=$(date +"%M pass %H o'clock, %h %d, %Y")
WeekNum=$(date +"%w")

morning=$(echo "Good morning! This is Ada. Now is $NOW, time to get up! ")

class=$(echo "There is no class today, enjoy your weekend!")

if [ $WeekNum -eq $(expr 1) ]
then 
	class=$(echo "Today is Monday, you will have one class to catch which is computer science 25. ")
fi

if [ $WeekNum -eq $(expr 2) ]
then
	class=$(echo "Today is Tuesday, you will have two classes to catch which are philosophy 1 and Math 3B. ")
fi

if [ $WeekNum -eq $(expr 3) ]
then
	class=$(echo "Today is Wednesday, you will have one class to catch which is computer science 25. ")
fi

if [ $WeekNum -eq $(expr 4) ]
then
	class=$(echo "Today is Thursday, you will have three classes to catch which are political science 1, philosophy 1, and math 3B. ")
fi

if [ $WeekNum -eq $(expr 5) ]
then 
	class=$(echo "Today is Friday, you have no class today! ")
fi

weather=$(wget -q -O- "$URL" | awk -F\" '/acm_RecentLocationsCarousel\.push/{print "The weather today for "$2" is : "$4". "}'| head -1)

temperature=$(wget -q -O- "$URL" | awk -F\' '/acm_RecentLocationsCarousel\.push/{print "Temperature is about "$10" degrees Fahrenheit. I hope you would have a wonderful day! "}' | head -1)

bash ~/speech/speech.sh $morning
bash ~/speech/speech.sh $class
bash ~/speech/speech.sh $weather
bash ~/speech/speech.sh $temperature
