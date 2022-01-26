# import smtplib
#
# sender_mail = "zaharaza7889@gmail.com"
# sender_password = "8QfTFzeNFP4"
# recipient = "edward.lunch88@yahoo.com"
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=sender_mail, password=sender_password)
#     connection.sendmail(from_addr=sender_mail, to_addrs=recipient,
#                         msg="Subject:Hello\n\nThere is the content of a message.")

import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(day_of_week)
print(now)
print(year)

# set our own datetime
date_of_birth = dt.datetime(year=1996, month=12, day=1)
print(date_of_birth)
