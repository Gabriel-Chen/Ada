#!/usr/bin/python3
import json
import datetime
import subprocess

def get_class (data, date, class_list):
    count = 0
    for c in data['classes']:
        for d in data['classes'][c]['date']:
            if d == date:
                class_list.append(c + " at " + data['classes'][c]['time'])
                count += 1
    return count

def get_post (class_num, class_list):
    now = datetime.datetime.now()
    post = "Good morning! This is Ada. Today is " + now.strftime('%c') + ". "
    if class_num == 0:
        return post + "You have now classes today, enjoy your day! "
    post += "You will have " + str(class_num) + " classes today, they are " + ', '.join(class_list) + ". Have a wonderful day! "
    return post

def push_message (file_name):
    data = json.load(open(file_name))
    now = datetime.datetime.now()
    class_list = list()
    class_num = get_class(data, now.strftime('%a'), class_list)
    post = get_post(class_num, class_list)
    bash_command = "echo " + post + " | mutt -s 'Classes for Today' me"
    subprocess.Popen(bash_command, shell=True)
    return True
    

if __name__ == "__main__":
    push_message('class.json')
    push_message('class_a.json')
