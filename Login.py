from tkinter import *
from tkinter import messagebox
import mysql.connector

def loginUser():

    global username
    global password
    #global author

    busername=username.get()
    bpassword=password.get()
    #bauthor=author.get()
    
    mydb = mysql.connector.connect(host ="localhost",user = "root",password = 'Chelsey1#',database='CSCPROJECT2021')
    cursor = mydb.cursor()
    
    print(busername,end='--')
    print(bpassword,end='--')
    #print(bauthor,end='--')
    print("Login")

    sqlquery= "insert into USER values('" + busername +"','"+bpassword+"','YES');"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo("Login Successful")
    except:
        messagebox.showinfo("User Not Found")
    window=Tk()
    window.destroy()

def userLogin():

    global username
    global password
    #global author

    window=Tk()
    window.title('Perfect Match Matrimony')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "Login")
    greet.grid(row = 0,columnspan = 3)

    #----------id-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter username: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)

    username=Entry(window,width=5,font =('arial', 15, 'bold'))
    username.grid(row=2,column=3)

    #----------title-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Password: ")
    L.grid(row = 4, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)

    password=Entry(window,width=5,font =('arial', 15, 'bold'))
    password.grid(row=4,column=3)

       
    submitbtn=Button(window,text="Submit",command=loginUser,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("LOGIN")
    pass