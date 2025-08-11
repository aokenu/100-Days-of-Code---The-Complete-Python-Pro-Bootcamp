import smtplib
import ssl
from email.mime.text import MIMEText


with open("message.txt", "r", encoding="utf-8") as f:
    message = f.read()

smtp_server = "smtp.gmail.com"
port = 587
my_email = "datadotng@gmail.com"
password = "bjlvycgbqgtzkoek"
msg = MIMEText(message, "plain", "utf-8")
msg["Subject"] = "Hallo aus meiner Python-App"



connection = smtplib.SMTP(smtp_server, port)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="chibuikeokenu@gmail.com", msg=msg.as_string())
connection.close()
