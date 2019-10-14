# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:15:31 2019

@author: Sarvesh
"""
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import database as db
import scrap as scrappy


e_mail='Email OF Sender'
pwd='Password'


def send_mail():
    scrappy.scrappy()
    f=open('news.txt','r',encoding='utf-8')
    a=f.read()



    names=db.dbsel()

    s = smtplib.SMTP(host='smtp.gmail.com',port=587)
    s.starttls()
    s.login(e_mail, pwd)

    for name in names:
        msg = MIMEMultipart()


        message = a

        msg['From']=e_mail
        msg['To']=name
        msg['Subject']="Newsletter"


        msg.attach(MIMEText(message, 'plain'))


        s.send_message(msg)

        del msg
    s.close()
