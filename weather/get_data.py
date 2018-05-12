#!/bin/python3
import re
import subprocess
from bs4 import BeautifulSoup

def parse_html (source):
    weather_source = open(source, 'r')
    return BeautifulSoup(weather_source, 'html.parser')

def get_weather_narrative (data):
    d = data.find_all('td', {'class' : 'description'})
    return re.search(r'\stitle="(.*?)\"', str(d[0]))

def push_message (city):
    weather_data = parse_html(city)
    narrative = get_weather_narrative(weather_data).group(1)
    bash_command = "echo " + narrative + " | mutt -s 'weather' 5105206239@mms.cricketwireless.net"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


if __name__ == "__main__":
    push_message('la')
    push_message('berkeley')
