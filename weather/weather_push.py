#!/usr/bin/python3
import re
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from keys import *

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

def get_post (city, who):
    weather_data = parse_html(city)
    narrative = get_weather_narrative(weather_data).group(1)
    if who == 'love':
        return "Hey my babe, the weather today for " + city + " looks like " + narrative + " Hope you would have a wonderful day! "
    return "Morning! This is Ada, the weather today for " + city + " looks like " + narrative + " Hope you would have a wonderful day! "

def push_message (city, who):
    post = get_post(city, who)
    msg = MIMEMultipart()
    msg['From'] = gmail_name
    to_list = [my_phone]
    if who == 'love':
        to_list,append(love_phone)
        msg['Subject'] = "Morning My Babe!"
    else:
        msg['Subject'] = "Good Morning!"
    msg.attach(MIMEText(post, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_name, gmail_pass)
    for to in to_list:
        msg['To'] = to
        server.sendmail(gmail_name, msg['To'], msg.as_string())
    server.quit()
    return True

if __name__ == "__main__":
    get_source_data('LA', 'https://weather.com/weather/5day/l/USCA0638:1:US')
    get_source_data('Berkeley', 'https://weather.com/weather/5day/l/USCA0087:1:US')
    push_message('LA', 'love')
    push_message('Berkeley', 'me')
