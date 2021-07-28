from tkinter import *
from tkinter import messagebox
import mysql.connector

def regUser():

    global name
    global gender
    global age
    global nationality
    global Hobby1
    global Hobby2
    global Hobby3
    global email
    global username
    global password


    bname=name.get()
    bgender=gender.get()
    bage=age.get()
    bnationality=nationality.get()
    bHobby1=Hobby1.get()
    bHobby2=Hobby2.get()
    bHobby3=Hobby3.get()
    bemail=email.get()
    busername=username.get()
    bpassword=password.get()
    
    
    mydb = mysql.connector.connect(host ="localhost",user = "root",password = 'Chelsey1#',database='CSCPROJECT2021')
    cursor = mydb.cursor()
    
    print(bname,end='--')
    print(bgender,end='--')
    print(bage,end='--')
    print(bnationality,end='--')
    print(bHobby1,end='--')
    print(bHobby2,end='--')
    print(bHobby3,end='--')
    print(bemail,end='--')
    print(busername,end='--')
    print(bpassword,end='--')
    print("Register Now")
    
    #sqlquery= "insert into USER values('" + bname +"','"+bgender+"','" + bage +"','" + bnationality +"','" + bHobby1 +"','" + bHobby2 +"','" + bHobby3 +"','" + bemail +"','" + busername +"','" + bpassword +"','YES');"
    sqlquery="INSERT INTO USER VALUES ('{}','{}',{},'{}','{}','{}','{}','{}','{}','{}')".format(bname,bgender,bage,bnationality,bHobby1,bHobby2,bHobby3,bemail,busername,bpassword);
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        mydb.commit()
        messagebox.showinfo("New Profile Created!")
    except:
        messagebox.showinfo("Something went wrong!")
    window=Tk()
    window.destroy()

def userReg():

    global name
    global gender
    global age
    global nationality
    global Hobby1
    global Hobby2
    global Hobby3
    global email
    global username
    global password

    window=Tk()
    window.title('Perfect Match Matrimony')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "Register Now")
    greet.grid(row = 0,columnspan = 3)
    
    #----------name-------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter name: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)

    name=Entry(window,width=5,font =('arial', 15, 'bold'))
    name.grid(row=2,column=3)
    
    #----------gender-------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter gender: ")
    L.grid(row = 4, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)

    gender=Entry(window,width=5,font =('arial', 15, 'bold'))
    gender.grid(row=4,column=3)
    
    #----------age-------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter age: ")
    L.grid(row = 6, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 6, column = 2)

    age=Entry(window,width=5,font =('arial', 15, 'bold'))
    age.grid(row=6,column=3)
    
    
    #----------nationality------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter nationality: ")
    L.grid(row = 8, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 8, column = 2)

    nationality=Entry(window,width=5,font =('arial', 15, 'bold'))
    nationality.grid(row=8,column=3)
    
    #----------Hobby1------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Hobby1: ")
    L.grid(row = 10, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 10, column = 2)

    Hobby1=Entry(window,width=5,font =('arial', 15, 'bold'))
    Hobby1.grid(row=10,column=3)
    
    #----------Hobby2------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Hobby2: ")
    L.grid(row = 12, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 12, column = 2)

    Hobby2=Entry(window,width=5,font =('arial', 15, 'bold'))
    Hobby2.grid(row=12,column=3)
    
    #----------Hobby3------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Hobby3: ")
    L.grid(row = 14, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 14, column = 2)

    Hobby3=Entry(window,width=5,font =('arial', 15, 'bold'))
    Hobby3.grid(row=14,column=3)
    
    #----------email------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter email: ")
    L.grid(row = 16, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 16, column = 2)

    email=Entry(window,width=5,font =('arial', 15, 'bold'))
    email.grid(row=16,column=3)
    
    #----------username------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter username: ")
    L.grid(row = 18, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 18, column = 2)

    username=Entry(window,width=5,font =('arial', 15, 'bold'))
    username.grid(row=18,column=3)
    
    #----------password------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter password: ")
    L.grid(row = 20, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 20, column = 2)

    password=Entry(window,width=5,font =('arial', 15, 'bold'))
    password.grid(row=20,column=3)
    
    submitbtn=Button(window,text="Submit",command=regUser,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=22,columnspan=3)
        
    print("REGISTER")
    pass
    

    


