# API endpoint: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?q=Wollongong,AU&appid=5fa9175a8ba42a6ae43248850cae0f5f
# API key: 5fa9175a8ba42a6ae43248850cae0f5f
# City: Wollongong, AU / Nanchong, CN
'''
问候逻辑存在问题，无法自动问候
日出日落天晴逻辑
下雨逻辑
满月逻辑
'''

# onecall https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
import os
from twilio.rest import Client
import requests
from datetime import datetime
import random

# set up weather api
api_key = os.environ.get("OWM_API_KEY")
api_param_2518 = {
    "lat": -37.913263,
    "lon": 145.132297,
    # "lat": -34.383862,
    # "lon": 150.902817,
    "exclude": "current,minutely",
    "units": "metric",
    "appid": api_key
}

# set up sms API
account_sid = os.environ.get("OWM_SID")
auth_token = os.environ.get("OWM_token")

# request API
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=api_param_2518)

# GET data from API
weather_data = response.json()
daily_dataset = weather_data["daily"]

# weather dictionary
weather_dict = {
    "5": "有雨🌧",
    "3": "小雨🌧",
    "2": "有雷🌩",
    "6": "小雪🌨",
    "9": "多云🌥",
    "800": "晴☀️"
}

# set up
location = ""
if api_param_2518.get("lat") <= -35:
    location = "墨尔本"
elif api_param_2518.get("lat") > -35:
    location = "卧龙岗"

greetting = f"{location}天气\n可爱小相❤️，小高提醒您\n"

greetting2 = ["请小相记得好好吃饭哦🥰", "对着可爱小相一个大啾咪😘", "天冷，注意保暖💚️"]
greet = greetting2[random.randint(0, 2)]


def weather_code(weather_data):
    '''
    input weather data in list format
    return the weather id and  what it represents
    '''
    weather = weather_data["weather"]
    weather_id = weather[0]["id"]
    if weather_id > 800:
        return weather_dict.get('9')
    elif weather_id == 800:
        return weather_dict.get('800')
    else:
        weather_start = str(weather_id)[0]
        return weather_dict.get(weather_start), weather_start


def weather(weather_list):
    '''
    :param weather_list: should be a list such as daily_dataset[0], daily_dataset[1]
    :return: a weather report
    '''
    # weather_list = daily_dataset[0]
    daily_temp = weather_list["temp"]
    min_temp = daily_temp["min"]
    max_temp = daily_temp["max"]
    weather_feel = weather_list["feels_like"]["day"]
    # weather_uvi = weather_list["uvi"]
    weather_id = weather_code(weather_list)
    if len(weather_id) == 2:
        rain_report = "如果出门请记得带伞哦～🌂"
        weather_report = f"{weather_id[0]}\n最低温度:{min_temp}ºC\n最高温度:{max_temp}ºC\n体感温度:{weather_feel}ºC\n{rain_report}\n"
    else:
        weather_report = f"{weather_id}\n最低温度:{min_temp}ºC\n最高温度:{max_temp}ºC\n体感温度:{weather_feel}ºC\n"

    return weather_report


def moon_report(weather_list):
    daily_sunrise = weather_list["sunrise"]
    sunrise_report = f"日出时间: {datetime.fromtimestamp(daily_sunrise).strftime('%H:%M')}"
    daily_sunset = weather_list["sunset"]
    sunset_report = f"日落时间: {datetime.fromtimestamp(daily_sunset).strftime('%H:%M')}"
    daily_moon = weather_list["moon_phase"]
    if daily_moon == 0.5:
        phase_report = "今天满月诶，考虑一起观月嘛？"
        moon_rise = weather_list["moonrise"]
        moonrise_report = f"月出时间: {datetime.fromtimestamp(moon_rise).strftime('%H:%M')}"
        return sunrise_report + sunset_report + phase_report + moonrise_report
    else:
        return sunrise_report + " " + sunset_report


# print("Today",weather(daily_dataset[0]))
# moon_report(daily_dataset[0])
# print("-----------------")
# print("Tomorrow",weather(daily_dataset[1]))
# moon_report(daily_dataset[1])


client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=f"\n{greetting}今日, {weather(daily_dataset[0])}" + f"{moon_report(daily_dataset[0])}\n  \n明日, {weather(daily_dataset[1])}" + f"{moon_report(daily_dataset[1])}\n{greet}",
    from_='+12173873623',
    to=os.environ.get("Xin_tel")
    # to="+61493422067"
)
