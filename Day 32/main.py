import smtplib
import ssl
from email.mime.text import MIMEText
import random
import datetime as dt

DAY = 1
# Open the txt file containing the quotes
with open("quotes.txt", "r", encoding="utf-8") as f:
    my_text = f.readlines()
    stripped_text = [line.strip() for line in my_text]
    message = random.choice(stripped_text)



# Email setup
smtp_server = "smtp.gmail.com"
port = 587
my_email = "datadotng@gmail.com"
password = "bjlvycgbqgtzkoek"
msg = MIMEText(message, "plain", "utf-8")
msg["Subject"] = "Daily Motivational Quote"
msg["From"] = my_email
msg["To"] = "chibuikeokenu@gmail.com"

# Getting the day of the week
day_of_the_week = dt.datetime.today().weekday()

# conditional statement to send email
if day_of_the_week == DAY:
    with smtplib.SMTP(smtp_server, port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(my_email, ["chibuikeokenu@gmail.com"], msg.as_string())

        print("Email sent successfully")
else:
    print("Today is not the day")






