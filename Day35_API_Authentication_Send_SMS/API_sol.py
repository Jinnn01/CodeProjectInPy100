import requests
from twilio.rest import Client
from datetime import datetime
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
api_param_2518 = {
    "lat":-34.383862,
    "lon":150.902817,
    "exclude": "current,minutely",
    "units": "metric",
    "appid": api_key
}


# set up sms API
account_sid = os.environ.get("OWM_SID")
auth_token = os.environ.get("OWM_token")

# daily
response = requests.get(url=OWM_Endpoint, params=api_param_2518)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
weather_slice = weather_data["hourly"][:12]
def whether_rain():
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            return True

if whether_rain():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="In Towradgi \n It is going to rain, please bring an umbrella🌂",
        from_='+12173873623',
        to= os.environ.get("Xin_tel")
    )

    print(message.status)

