import os
import smtplib
from socket import gaierror
from email.mime.text import MIMEText
import PySimpleGUI as sg
from dotenv import load_dotenv
load_dotenv()

sg.theme('DarkAmber')	# Add a touch of color
layout = [  [sg.Text('To continue please log in')],
            [sg.Text('Usermame', size=(15, 1)), sg.InputText(os.getenv('MAIL_USERNAME'), key='Username')],
            [sg.Text('Password', size=(15, 1)), sg.InputText(os.getenv('MAIL_PASSWORD'), key='Password', password_char='*')],
            [sg.Button('Ok')] ]

window = sg.Window('Window Title', layout)

event, values = window.read()  
print('Username: ', values['Username'])
print('Password: ', values['Password'])
gmail_user = values['Username']
gmail_password = values['Password']
window.close()

everything_ok = True

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))
    everything_ok = False
    sg.Popup('Game over!', 'You better check your creds!')

if everything_ok:
    sg.Popup(f'Welcome {gmail_user}!', 'Now you can send a message here!')

    layout = [  [sg.Text('Enter text you want send to yourself')],
            [sg.Text('Receiver:', size=(8, 1)), sg.InputText(os.getenv('SENDTO'), key='Receiver', size=(25,1))],
            [sg.Text('Subject:', size=(8, 1)), sg.InputText('', key='Subject', size=(25,1))],
            [sg.Text('Body: ', size=(8, 1)), sg.InputText('', key='Body')],
            [sg.Submit(), sg.Button('Exit')] ]

    window = sg.Window('Just send it', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):	# if user closes window or clicks cancel
            break
        print('Subject: ', values['Subject'])
        print('Body: ', values['Body'])

        fromx = gmail_user
        to  = values['Receiver']
        msg = MIMEText(values['Body'])
        msg['Subject'] = values['Subject']
        msg['From'] = fromx
        msg['To'] = to
        
        try:
            server.sendmail(fromx, to, msg.as_string())
            server.close()

            print('Email sent!')
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
        
        sg.Popup('Sent!', 'Message sent!')
        window['Subject']('')
        window['Body']('')
        

    window.close()



