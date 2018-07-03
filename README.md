# Ada - An Engine Powered by Love
![build](https://img.shields.io/travis/Gabriel-Chen/Ada.svg?longCache=true&style=flat-square) ![license](https://img.shields.io/badge/license-MIT-blue.svg?longCache=true&style=flat-square) ![download](https://img.shields.io/github/downloads/gabriel-chen/ada/total.svg?longCache=true&style=flat-square)

This project initially means to help my girlfriend and I get through college without a messy time scheduel. It includes two parts for now which are `reminder` and `weather` and runs currently on a Raspberry Pi with `crontab`. This project can be used as a personal reminder on a running server (such as Raspberry Pi ).

## Weather

Every morning at 6:30, the `weather_push.py` file will run automatically and retrive weather data from the internet and parse the pure html data into dictionary data type using BeautifulSoup. Then the weather narrative will be pulled out for that day using regular expression and sent out as a SMS message.

Since the messages for us should be different, the final look she receive on her phone will look like this: 

![ada-weather-love](https://i.imgur.com/AkEAD6g.png)

And the message I will receive on my device look like this:

![ada-weather-me](https://i.imgur.com/dUqK55k.png)

## Reminder

Everyday, the `class_reminder.py` file will be run during the morning to remind us what classes we have today and what time are they. The classes information of the whole semester / quater is saved into two files as `class.json` and `class_a.json`, and the data is going to be loaded into python dictionary while using. The data get filtered and eventually sent out as SMS message.

The final look we receive on our phone will look likt this:

![ada-reminder](https://i.imgur.com/ONKtAmw.png)

When you have no class for a day, the message will be like this:

![ada-reminder-no-class](https://i.imgur.com/RJVfgCd.png)

Also, if a day is a holidy in the U.S., all the classes are going to be ignored and the message also changes:

![ada-reminder-holiday](https://i.imgur.com/YQJo5wQ.png)

## Getting Start

This tool can also be modified and used on your demand. First, you should have a local file called `keys.py`  under both feature‘s directory to store all the keys for sending out messages. The content of `keys.py` should be like bellow:

```bash
gmail_name = "Your Gmail Address"
gmail_pass = "Your Gmail Password"
my_phone = "Your Phone Number as Email Address Format"
love_phone = "Same Format Like Above for The One You Would Like to Remind"
```

For more about what you should do with the email address of a phone number, read [this post](https://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/). Also, in order to closely inspect the result we get for the person you are going to remind, you will also get the same message at the same time when he/she gets the message.

## More Attention

### More Locations for Weather Pulling

For the weather source, I get it from [this website](https://weather.com) with `curl`. Right now it is getting weather narrartive for both Berkeley and Los Angeles by default, but you can change which city’s weather you would like to push in `weather_push.py`.

```python
get_source_data('LA', 'https://weather.com/weather/5day/l/USCA0638:1:US')
get_source_data('Berkeley', 'https://weather.com/weather/5day/l/USCA0087:1:US')
```

By changing the `url` in the `get_source_data` function‘s parameter.

### Classes List for Reminder

In the `reminder` feature, the list of all classes is stored in a `json` file. For example, below is the list for my classes in the `class.json` file.

```json
{
	"classes" : {
		"Math 104" : {
			"date" : ["Mon", "Wed", "Fri"],
			"time" : "8:00 - 9:00"
		},

		"EE 16B" : {
			"date" : ["Tue", "Thu"],
			"time" : "17:00 - 18:30"
		},

		"CS 70" : {
			"date" : ["Tue", "Thu"],
			"time" : "12:30 - 14:00"
		}
	}
}

```

As long as you are familar with `json` data type, you are good to go with modifying this file to make it work for you.