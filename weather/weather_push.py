#!/usr/bin/python3
import re
import subprocess
from bs4 import BeautifulSoup

def get_source_data(city, address):
    bash_command = "curl -o " + city + " " + address
    subprocess.Popen(bash_command, shell=True)
    return True

def parse_html (source):
    weather_source = open(source, 'r')
    return BeautifulSoup(weather_source, 'html.parser')

def get_weather_narrative (data):
    d = data.find_all('td', {'class' : 'description'})
    return re.search(r'\stitle="(.*?)\"', str(d[0]))

def get_post (city):
    weather_data = parse_html(city)
    narrative = get_weather_narrative(weather_data).group(1)
    data = open(city + "_post", 'w')
    data.write("Hey my babe, the weather today for " + city + " looks like " + narrative + " Hope you would have a wonderful day! ")
    return True

def push_message (city, who):
    get_post(city)
    bash_command = "mutt -s 'Morning My Babe!' " + who + " < " + city + "_post"
    subprocess.Popen(bash_command, shell=True)
    return True

if __name__ == "__main__":
    get_source_data('LA', 'https://weather.com/weather/5day/l/USCA0638:1:US')
    get_source_data('Berkeley', 'https://weather.com/weather/5day/l/USCA0087:1:US')
    push_message('LA', 'love')
    push_message('Berkeley', 'me')
