from tkinter import *
import mysql.connector

from Login import *
from Register import *
#from issue import * 
#from Return import *
#from view import *

'''mydb=mysql.connector.connect(host="localhost",user="root",passwd="Chelsey1#")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists CSCPROJECT2021 ")
mycursor.execute("show databases")
for x in mycursor:
    print(x)
'''

mydb = mysql.connector.connect(host ="localhost",user = "root",passwd = 'Chelsey1#',database='CSCPROJECT2021')
cursor = mydb.cursor()

window=Tk()
window.title("Perfect Match Matrimony")

greet = Label(window, font = ('arial', 30, 'bold'),bg="DodgerBlue2", text = "Welcome to Perfect Match Matrimony!")
greet.grid(row = 0,columnspan = 3)

loginbtn=Button(window,text="Login",command=userLogin,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
loginbtn.grid(row=3,columnspan=3)

registerbtn=Button(window,text="Register",command=userReg,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
registerbtn.grid(row=5,columnspan=3)
'''
issuebtn=Button(window,text="Issue Books",command=issueBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
issuebtn.grid(row=7,columnspan=3)

returnbtn=Button(window,text="Return Books",command=returnBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
returnbtn.grid(row=9,columnspan=3)

viewbtn=Button(window,text="View Books",command=viewBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
viewbtn.grid(row=11,columnspan=3)'''

greet = Label(window, font = ('arial', 15, 'bold'), text = "Thank you")
greet.grid(row = 13,columnspan = 3)

window.mainloop()
