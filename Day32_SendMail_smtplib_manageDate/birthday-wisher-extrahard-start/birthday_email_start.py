##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

SENDER_MAIL = "zaharaza7889@gmail.com"
SENDER_PASSWORD = "8QfTFzeNFP4"

# 2. Check if today matches a birthday in the birthdays.csv
now_datetime = dt.datetime.now()
current_month = now_datetime.month
current_day = now_datetime.day

# get birthday info from csv file with pandas
birthday_file = pd.read_csv(
    "birthdays.csv")
birthday_dict = birthday_file.to_dict(orient="records")

# check birthday and get name & email address
for birthday in birthday_dict:
    if birthday["month"] == current_month and birthday["day"] == current_day:
        rec_name = birthday["name"]
        rec_email = birthday["email"]

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        random_letter = random.choice(letters)
        with open(
                f"letter_templates/{random_letter}",
                "r") as letter_file:
            letter_content = letter_file.readlines()

            if "[NAME]" in letter_content[0]:
                letter_name = letter_content[0].replace("[NAME]", f"{rec_name}")
                # set up letter content
                new_content = letter_name + "".join(letter_content[1:])

                # set up email server
                with smtplib.SMTP("smtp.gmail.com") as mail_connection:
                    mail_connection.starttls()
                    mail_connection.login(user=SENDER_MAIL, password=SENDER_PASSWORD)
                    mail_connection.sendmail(from_addr=SENDER_MAIL,to_addrs=rec_email, msg=f"Subject:Happy Birthday\n\n{new_content}")


# 4. Send the letter generated in step 3 to that person's email address.
