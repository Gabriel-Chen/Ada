#!/usr/bin/python3
import json
import datetime
import subprocess

def get_class (data, date, class_list):
    count = 0
    for c in data['classes']:
        for d in data['classes'][c]['date']:
            if d == date:
                class_list.append(c)
                count += 1
    return count

def get_post (class_num, class_list):
    post = "You will have " + str(class_num) + " classes today, and they are " + ', and '.join(class_list)
    return post

def push_message ():
    data = json.load(open('class.json'))
    now = datetime.datetime.now()
    class_list = list()
    class_num = get_class(data, now.strftime('%a'), class_list)
    post = get_post(class_num, class_list)
    bash_command = "echo " + post + " | mutt -s 'Classes for Today' me"
    subprocess.Popen(bash_command, shell=True)
    return True
    

if __name__ == "__main__":
    push_message()
