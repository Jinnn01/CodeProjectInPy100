import requests
from datetime import datetime
import smtplib
import time

sender_mail = "zaharaza7889@gmail.com"
sender_password = "8QfTFzeNFP4"
recipient = "edward.lunch88@yahoo.com"

MY_LAT = 31.230391
MY_LONG = 121.473701
# MY_LAT = -10.5716
# MY_LONG = -130.7525

# Your position is within +5 or -5 degrees of the ISS position.
def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude, iss_latitude)

    if abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])+8-24
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])+8
    print(sunrise, sunset)

    time_now = datetime.now().hour
    print(time_now)
    if sunrise > time_now or time_now > sunset:
        return True

# senf an email if the issoverhead and time is less than sunset
while True:
    time.sleep(60)
    if is_night() and check_pos():
        # set up email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_mail,password=sender_password)
            connection.sendmail(from_addr=sender_mail,to_addrs=sender_mail,msg="Subject:Issoverhead \n\n Hey! Look up!")



# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
