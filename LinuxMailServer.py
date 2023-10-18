# Static Automation Mail Server

import smtplib

from datetime import datetime # For Datetime
from email.mime.text import MIMEText # For msg Email sequense


Sender_Email = "your_email_ID@gmail.com"
Sender_passwrd = "your_thridparty_Passwrd"

Resever_Email = "Example@gmail.com"



subject = "System StartUP Mail"

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


body = f'''Hello,

Greetings of the day.

Your System has been turned ON at {current_datetime} # you can customize body & subject as per your needs

Best Regards
[your_name]'''

msg = MIMEText(body)
msg['From'] = Sender_Email
msg['To'] = Resever_Email
msg['Subject'] = subject


a = smtplib.SMTP('smtp.gmail.com', 587)
a.starttls()
a.login(Sender_Email,Sender_passwrd)
a.sendmail(Sender_Email, Resever_Email,msg.as_string())
a.quit()

print("Email Send Successfully")
