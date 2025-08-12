##################### Extra Hard Starting Project ######################
import pandas as pd
import csv
import datetime as dt
import random
import smtplib
import ssl
from email.mime.text import MIMEText


TODAY = 12

# 1. Update the birthdays.csv
with open("birthdays.csv", "r") as file:
    bd_details = file.read()
    print(bd_details)

new_record = [
    ["Mum", "datadotng@gmail.com", 1967, 3, 20],
    ["Dad", "chibuikeokenu@gmail.com", 1954, 8, 12]
]

with open("birthdays.csv", "a", newline="", encoding="utf-8") as update_file:
    update = csv.writer(update_file)
    update.writerows(new_record)
    print(update)

#  Read CSV into DataFrame
df = pd.read_csv("birthdays.csv")

#  Filter to get Dad's row
receiver_info = df[df["name"] == "Dad"].to_dict("records")[0]
name = receiver_info["name"]
email = receiver_info["email"]

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.day


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

letter_file = f"letter_templates/letter_{random.randint(1,3)}.txt"

if today == TODAY:
    with open(letter_file, "r", encoding="utf-8") as f:
        message = f.read()
        message = message.replace("[NAME]", name)
        print(message)


# 4. Send the letter generated in step 3 to that person's email address.

smtp_server = "smtp.gmail.com"
port = 587
my_email = "datadotng@gmail.com"
password = "bjlvycgbqgtzkoek"
msg = MIMEText(message, "plain", "utf-8")
msg["Subject"] = "Birthday Wishes"
msg["From"] = my_email
msg["To"] = "chibuikeokenu@gmail.com"

with smtplib.SMTP(smtp_server, port) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(my_email, ["chibuikeokenu@gmail.com", "austineokenu@gmail.com"], msg.as_string())
    print(f"Email send to {name} successfully")


