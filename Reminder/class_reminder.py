#!/usr/bin/python3
import json
import datetime
import subprocess
import holidays
from keys import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_class (data, date, class_list):
    count = 0
    for c in data['classes']:
        for d in data['classes'][c]['date']:
            if d == date:
                class_list.append(c + " at " + data['classes'][c]['time'])
                count += 1
    return count

def get_post (class_num, class_list, now):
    post = "Good morning! This is Ada. Today is " + now.strftime('%c') + ". "
    us_holidays = holidays.UnitedStates()
    today = datetime.date.today()
    if today in us_holidays:
        return post + "Today is" + us_holidays.get(str(today)) + ". Happy holiday! "
    if class_num == 0:
        return post + "You have no classes today, enjoy your day! "
    post += "You will have " + str(class_num) + " classes today, they are " + ', '.join(class_list) + ". Have a wonderful day! "
    return post

def push_message (file_name, who):
    data = json.load(open(file_name))
    now = datetime.datetime.now()
    class_list = list()
    class_num = get_class(data, now.strftime('%a'), class_list)
    post = get_post(class_num, class_list, now)
    msg = MIMEMultipart()
    msg['From'] = gmail_name
    to_list = [my_phone]
    if who == 'love':
        to_list,append(love_phone)
    msg['Subject'] = "Classes for Today"
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
    push_message('class.json', 'me')
    push_message('class_a.json', 'love')
