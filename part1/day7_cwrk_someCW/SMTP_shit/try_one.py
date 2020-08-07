import os
import smtplib
from socket import gaierror
from dotenv import load_dotenv
load_dotenv()

gmail_user = os.getenv('MAIL_USERNAME')
gmail_password = os.getenv('MAIL_PASSWORD')

sent_from = gmail_user
to = [os.getenv('SENDTO')]
subject = 'Not that important message'
body = "Hey, what's up buddy?\n\n- You'r seem upset a bit, what is on your mind brah?"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except (gaierror, ConnectionRefusedError):
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))

