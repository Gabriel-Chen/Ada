# Ada - an engine powered by love

This project means to help my girlfriend and I get through college without a messy time scheduel. It includes two parts for now which are `remingder` and `weather` and runs currently on a Raspberry Pi with `crontab`.

## Weather

Every morning at 6:30, the `weather_push.py` file will run automatically and retrive weather data from the internet and parse the pure html data into dictionary data type using BeautifulSoup. Then the weather narrative will be pulled out for that day using regular expression and sent out as a SMS message using mutt.

The final look we receive on our phone will look like this: 

![ada-weather](https://i.imgur.com/FKvfoTV.png)

## Reminder

Everyday, the `class_reminder.py` file will be run during the morning to remind us what classes we have today and what time are they. The classes information of the whole semester / quater is saved into two files as `class.json` and `class_a.json`, and the data is going to be loaded into python dictionary while using. The data get filtered and eventually sent out as SMS message using mutt.

The final look we receive on our phone will look likt this:

![ada-reminder](https://i.imgur.com/5cMFTpy.png)
