import datetime as dt
import random
import smtplib

sender_mail = "zaharaza7889@gmail.com"
sender_password = "8QfTFzeNFP4"
recipient = "edward.lunch88@yahoo.com"


current_time = dt.datetime.now()

# read file and set quotes
with open("/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day31_SendMail_smtplib_manageDate/quotes.txt",
          "r") as quote_file:
    quote = quote_file.readlines()
    daily_quote = random.choice(quote).strip()
    print(daily_quote)

# set up the email sever and send quote in Weds
with smtplib.SMTP("smtp.gmail.com") as mail_connection:
    mail_connection.starttls()
    mail_connection.login(user=sender_mail, password=sender_password)
    if current_time.weekday() == 2:
        mail_connection.sendmail(from_addr=sender_mail, to_addrs=recipient,
                                 msg=f"Subject:Daily Motivation\n\n{daily_quote}")

