# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:06:59 2019

@author: Sarvesh
"""

import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user="root",passwd="pass@123",database="sdl")
mycursor = mydb.cursor()


def dbin(u_name,u_email):

    insert="insert into users(name,email) values(%s,%s)"
    name=[(u_name,u_email)]
    mycursor.executemany(insert,name)
    mydb.commit()


umails = []
def dbsel():
    usmail="select email from users"
    mycursor.execute(usmail)
    for mail in mycursor:
        umails.append(mail[0])

    return umails

def res():
    res="delete from users where email like '%@%'"
    mycursor.execute(res)
    mydb.commit()

def update(email,name):
    update ='update users set email= %s where name =%s'
    upname = [(email,name)]
    mycursor.executemany(update,upname)
    mydb.commit()

def delete(name,email):
    dele ='delete from users where name=%s AND email=%s'
    delname=[(name,email)]
    mycursor.executemany(dele,delname)
    mydb.commit()
