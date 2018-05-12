#!/bin/python3
import re
import subprocess
from bs4 import BeautifulSoup

def get_source_data(city, address):
    #data = open(city, 'w')
    bash_command = "curl -o " + city + " " + address
    subprocess.Popen(bash_command, shell=True)
    #data.close()

def parse_html (source):
    weather_source = open(source, 'r')
    return BeautifulSoup(weather_source, 'html.parser')

def get_weather_narrative (data):
    d = data.find_all('td', {'class' : 'description'})
    return re.search(r'\stitle="(.*?)\"', str(d[0]))

def push_message (city):
    weather_data = parse_html(city)
    narrative = get_weather_narrative(weather_data).group(1)
    bash_command = "echo " + "\"" + narrative + "\"" + " | mutt -s 'weather' me"
    subprocess.Popen(bash_command, shell=True)


if __name__ == "__main__":
    get_source_data('la', 'https://weather.com/weather/5day/l/USCA0638:1:US')
    get_source_data('berkeley', 'https://weather.com/weather/5day/l/USCA0087:1:US')
    push_message('la')
    push_message('berkeley')
