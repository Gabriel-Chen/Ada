#!/bin/sh

URL='http://www.accuweather.com/en/us/berkeley-ca/94704/weather-forecast/332044'

NOW=$(date +"%H")

time=$(echo "Hello! This is Ada. Now is $NOW o'clock. ")

weather=$(wget -q -O- "$URL" | awk -F\" '/acm_RecentLocationsCarousel\.push/{print "The weather for "$2" now looks like "$4". "}'| head -1)

temperature=$(wget -q -O- "$URL" | awk -F\' '/acm_RecentLocationsCarousel\.push/{print "Temperature is about "$10" degrees Fahrenheit. Time to have some rest! "}' | head -1)

bash ~/speech/speech.sh $time
bash ~/speech/speech.sh $weather
bash ~/speech/speech.sh $temperature
