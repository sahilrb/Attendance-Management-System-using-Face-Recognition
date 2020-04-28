from imutils import paths
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import cv2
import numpy as np
import pickle
import imutils
from tkinter import *
import tkinter.ttk as ttk
import os
from datetime import datetime
import mysql.connector
import collect
import train
from tkinter import messagebox
from datetime import date
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="database")
cursor = db.cursor()

def registerf():
    project.destroy()
    global reg
    reg = Tk()
    global email
    global username
    global password
    email = StringVar()
    username = StringVar()
    password = StringVar()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
       
    reg.geometry("600x474+381+170")
    reg.minsize(120, 1)
    reg.maxsize(1362, 741)
    reg.resizable(1, 1)
    reg.title("New reglevel")
    reg.configure(background="#fc9485")
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\login.png"
    global _img110
    _img110 = PhotoImage(file=photo_location)
    Button1 = Button(reg,activebackground="#ececec",activeforeground="#000000",background="#d9fcb6",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img110,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=164, width=607)
    
    Entry1 = Entry(reg,textvariable=username,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry1.place(relx=0.5, rely=0.464,height=34, relwidth=0.257)
    Entry1.delete(0, END)
    
    Entry2 = Entry(reg,textvariable=email,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry2.place(relx=0.5, rely=0.57,height=34, relwidth=0.257)
    Entry2.delete(0, END)
   
    Entry3 = Entry(reg,textvariable=password,show='*',background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry3.place(relx=0.5, rely=0.675,height=34, relwidth=0.257)
    Entry3.delete(0, END)
    
    Label1 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Email''')
    Label1.place(relx=0.283, rely=0.57, height=34, width=94)
    
    Label2 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Name''')
    Label2.place(relx=0.283, rely=0.464, height=34, width=94)
   
    Label3 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Password''')
    Label3.place(relx=0.283, rely=0.675, height=34, width=94)
   
    Button2 = Button(reg,command = register_userf,activebackground="#ececec",activeforeground="#000000",background="#e1e100",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Register''')
    Button2.place(relx=0.333, rely=0.844, height=34, width=97)
   
    Button3 = Button(reg,command=mainscreen1,activebackground="#ececec",activeforeground="#000000",background="#e1e100",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button3.place(relx=0.55, rely=0.844, height=34, width=97)

def register_userf():
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()

    try:
        cursor.execute("""INSERT INTO faculty(name,email,password) VALUES("{}", "{}","{}")""".format(username_info,email_info,password_info))
        db.commit()
        Label(reg, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        login1f()
    except:
        usedf()

def registers():
    project.destroy()
    global reg
    reg = Tk()
    global email1
    global username1
    global password1
    global roll1
    global section
    global year
    email1= StringVar()
    username1= StringVar()
    password1= StringVar()
    roll1 = StringVar()
    section = StringVar()
    year = StringVar()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    
    reg.geometry("696x548+322+112")
    reg.minsize(120, 1)
    reg.maxsize(1362, 741)
    reg.resizable(1, 1)
    reg.title("Student Login")
    reg.configure(background="#fc9485")
        
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\login.png"
    global _img220
    _img220 = PhotoImage(file=photo_location)    
    Button1 = Button(reg,activebackground="#ececec",activeforeground="#000000",background="#d9fcb6",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img220,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=164, width=697)
    
    Entry1 = Entry(reg,textvariable=roll1,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry1.place(relx=0.503, rely=0.42,height=34, relwidth=0.221)
    Entry1.delete(0, END)
    
    Entry2 = Entry(reg,textvariable=email1,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry2.place(relx=0.503, rely=0.511,height=34, relwidth=0.221)
    Entry2.delete(0, END)
   
    Entry3 = Entry(reg,textvariable=section,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry3.place(relx=0.503, rely=0.602,height=34, relwidth=0.221)
    Entry3.delete(0, END)
   
    Label1 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Email''')
    Label1.place(relx=0.273, rely=0.511, height=39, width=109)
    
    Label2 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Name''')
    Label2.place(relx=0.273, rely=0.328, height=39, width=109)
   
    Label3 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Password''')
    Label3.place(relx=0.273, rely=0.785, height=39, width=110)
       
    Button2 = Button(reg,command=register_users,activebackground="#ececec",activeforeground="#000000",background="#e1e100",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Register''')
    Button2.place(relx=0.432, rely=0.912, height=34, width=97)
   
    Button3 = Button(reg,command=mainscreen1,activebackground="#ececec",activeforeground="#000000",background="#e1e100",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button3.place(relx=0.632, rely=0.912, height=34, width=97)
    
    Button4 = Button(reg,command=add,activebackground="#ececec",activeforeground="#000000",background="#e1e100",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add Courses''')
    Button4.place(relx=0.232, rely=0.912, height=34, width=97)
   
    Label4 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Section''')
    Label4.place(relx=0.273, rely=0.602, height=38, width=113)

    Label5 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Year''')
    Label5.place(relx=0.273, rely=0.693, height=38, width=113)
       
    Label6 = Label(reg,background="#fcc4b6",disabledforeground="#a3a3a3",foreground="#000000",text='''Roll_No''')
    Label6.place(relx=0.273, rely=0.42, height=38, width=112)
   
    Entry4 = Entry(reg,textvariable=year,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry4.place(relx=0.503, rely=0.693,height=38, relwidth=0.221)
    Entry4.delete(0, END)
      
    Entry5 = Entry(reg,textvariable=username1,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry5.place(relx=0.503, rely=0.328,height=38, relwidth=0.221)
    Entry5.delete(0, END)
    
    Entry6 = Entry(reg,textvariable=password1,show='*',background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry6.place(relx=0.503, rely=0.785,height=38, relwidth=0.221)
    Entry6.delete(0, END)

    
def add():
    global top
    top = Toplevel()
    global co1
    co1 = IntVar()
    global co2
    co2 = IntVar()
    global co3
    co3 = IntVar()
    global co4
    co4 = IntVar()
    global co5
    co5 = IntVar()
    global co6
    co6 = IntVar()
    global co7
    co7 = IntVar()
    global co8
    co8 = IntVar()
    global co9
    co9 = IntVar()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    
    top.geometry("726x522+338+113")
    top.minsize(120, 1)
    top.maxsize(1362, 741)
    top.resizable(1, 1)
    top.title("Courses")
    top.configure(background="#48ff76")
    
    Checkbutton1 = Checkbutton(top)
    Checkbutton1.place(relx=0.317, rely=0.728, relheight=0.052, relwidth=0.157)
    Checkbutton1.configure(activebackground="#ececec")
    Checkbutton1.configure(activeforeground="#000000")
    Checkbutton1.configure(background="#f8ebba")
    Checkbutton1.configure(disabledforeground="#a3a3a3")
    Checkbutton1.configure(foreground="#000000")
    Checkbutton1.configure(highlightbackground="#d9d9d9")
    Checkbutton1.configure(highlightcolor="black")
    Checkbutton1.configure(justify='left')
    Checkbutton1.configure(text='''2cs301(DSA)''')
    Checkbutton1.configure(variable=co1)
    
    Checkbutton2 = Checkbutton(top)
    Checkbutton2.place(relx=0.317, rely=0.46, relheight=0.071, relwidth=0.15)
    Checkbutton2.configure(activebackground="#ececec")
    Checkbutton2.configure(activeforeground="#000000")
    Checkbutton2.configure(background="#f8ebba")
    Checkbutton2.configure(disabledforeground="#a3a3a3")
    Checkbutton2.configure(foreground="#000000")
    Checkbutton2.configure(highlightbackground="#d9d9d9")
    Checkbutton2.configure(highlightcolor="black")
    Checkbutton2.configure(justify='left')
    Checkbutton2.configure(text='''2cs304(DM)''')
    Checkbutton2.configure(variable=co2)

    Checkbutton3 = Checkbutton(top)
    Checkbutton3.place(relx=0.317, rely=0.556, relheight=0.052, relwidth=0.158)
    Checkbutton3.configure(activebackground="#ececec")
    Checkbutton3.configure(activeforeground="#000000")
    Checkbutton3.configure(background="#f8ebba")
    Checkbutton3.configure(disabledforeground="#a3a3a3")
    Checkbutton3.configure(foreground="#000000")
    Checkbutton3.configure(highlightbackground="#d9d9d9")
    Checkbutton3.configure(highlightcolor="black")
    Checkbutton3.configure(justify='left')
    Checkbutton3.configure(text='''2cs404(DBMS)''')
    Checkbutton3.configure(variable=co3)
 
    Checkbutton4 = Checkbutton(top)
    Checkbutton4.place(relx=0.523, rely=0.728, relheight=0.044, relwidth=0.157)
    Checkbutton4.configure(activebackground="#ececec")
    Checkbutton4.configure(activeforeground="#000000")
    Checkbutton4.configure(background="#f8ebba")
    Checkbutton4.configure(disabledforeground="#a3a3a3")
    Checkbutton4.configure(foreground="#000000")
    Checkbutton4.configure(highlightbackground="#d9d9d9")
    Checkbutton4.configure(highlightcolor="black")
    Checkbutton4.configure(justify='left')
    Checkbutton4.configure(text='''2cs403(OS)''')
    Checkbutton4.configure(variable=co4)
        
    Checkbutton5 = Checkbutton(top)
    Checkbutton5.place(relx=0.523, rely=0.46, relheight=0.063, relwidth=0.167)
    Checkbutton5.configure(activebackground="#ececec")
    Checkbutton5.configure(activeforeground="#000000")
    Checkbutton5.configure(background="#f8ebba")
    Checkbutton5.configure(disabledforeground="#a3a3a3")
    Checkbutton5.configure(foreground="#000000")
    Checkbutton5.configure(highlightbackground="#d9d9d9")
    Checkbutton5.configure(highlightcolor="black")
    Checkbutton5.configure(justify='left')
    Checkbutton5.configure(text='''2cs302(OOP)''')
    Checkbutton5.configure(variable=co5)
                
    Checkbutton6 = Checkbutton(top)
    Checkbutton6.place(relx=0.413, rely=0.824, relheight=0.063, relwidth=0.153)
    Checkbutton6.configure(activebackground="#ececec")
    Checkbutton6.configure(activeforeground="#000000")
    Checkbutton6.configure(background="#f8ebba")
    Checkbutton6.configure(disabledforeground="#a3a3a3")
    Checkbutton6.configure(foreground="#000000")
    Checkbutton6.configure(highlightbackground="#d9d9d9")
    Checkbutton6.configure(highlightcolor="black")
    Checkbutton6.configure(justify='left')
    Checkbutton6.configure(text='''2cs402(PSC)''')
    Checkbutton6.configure(variable=co6)
    
    Checkbutton7 = Checkbutton(top)
    Checkbutton7.place(relx=0.523, rely=0.632, relheight=0.056, relwidth=0.168)
    Checkbutton7.configure(activebackground="#ececec")
    Checkbutton7.configure(activeforeground="#000000")
    Checkbutton7.configure(background="#f8ebba")
    Checkbutton7.configure(disabledforeground="#a3a3a3")
    Checkbutton7.configure(foreground="#000000")
    Checkbutton7.configure(highlightbackground="#d9d9d9")
    Checkbutton7.configure(highlightcolor="black")
    Checkbutton7.configure(justify='left')
    Checkbutton7.configure(text='''2cs303(DE)''')
    Checkbutton7.configure(variable=co7)
   
    Checkbutton8 = Checkbutton(top)
    Checkbutton8.place(relx=0.317, rely=0.632, relheight=0.063, relwidth=0.152)
    Checkbutton8.configure(activebackground="#ececec")
    Checkbutton8.configure(activeforeground="#000000")
    Checkbutton8.configure(background="#f8ebba")
    Checkbutton8.configure(disabledforeground="#a3a3a3")
    Checkbutton8.configure(foreground="#000000")
    Checkbutton8.configure(highlightbackground="#d9d9d9")
    Checkbutton8.configure(highlightcolor="black")
    Checkbutton8.configure(justify='left')
    Checkbutton8.configure(text='''2cs405(PS)''')
    Checkbutton8.configure(variable=co8)
   
    Checkbutton9 = Checkbutton(top)
    Checkbutton9.place(relx=0.523, rely=0.556, relheight=0.044, relwidth=0.168)
    Checkbutton9.configure(activebackground="#ececec")
    Checkbutton9.configure(activeforeground="#000000")
    Checkbutton9.configure(background="#f8ebba")
    Checkbutton9.configure(disabledforeground="#a3a3a3")
    Checkbutton9.configure(foreground="#000000")
    Checkbutton9.configure(highlightbackground="#d9d9d9")
    Checkbutton9.configure(highlightcolor="black")
    Checkbutton9.configure(justify='left')
    Checkbutton9.configure(text='''2cs401(CA)''')
    Checkbutton9.configure(variable=co9)
   
    Button1 = Button(top)
    Button1.place(relx=0.0, rely=0.0, height=180, width=727)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#fdb5c7")
    Button1.configure(borderwidth="0")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\course.png"
    global _img1000
    _img1000 = PhotoImage(file=photo_location)
    Button1.configure(image=_img1000)
    Button1.configure(pady="0")
    Button1.configure(text='''Button''')
   
    Label1 = Label(top)
    Label1.place(relx=0.262, rely=0.345, height=32, width=355)
    Label1.configure(background="#bbbb00")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''Check all courses that you want to take and press add button''')
   
    Button2 = Button(top,command=add1)
    Button2.place(relx=0.427, rely=0.92, height=32, width=97)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#ffff00")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Add''')


def add1():
    messagebox.showinfo('Courses','Courses added successfully')
    top.destroy()
    roll21=roll1.get()
    c1=co1.get()
    c2=co2.get()
    c3=co3.get()
    c4=co4.get()
    c5=co5.get()
    c6=co6.get()
    c7=co7.get()
    c8=co8.get()
    c9=co9.get()
    #cursor.execute("""INSERT INTO sample(name,roll_no) VALUES("{}", "{}")""".format(name1,new_student))
    if c1 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs301")""".format(roll21))
        db.commit()
    if c2 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs304")""".format(roll21))
        db.commit()
    if c3 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs404")""".format(roll21))
        db.commit()
    if c4 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs403")""".format(roll21))
        db.commit()
    if c5 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs302")""".format(roll21))
        db.commit()
    if c6 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs402")""".format(roll21))
        db.commit()
    if c7 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs303")""".format(roll21))
        db.commit()
    if c8 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs405")""".format(roll21))
        db.commit()
    if c9 == 1:
        cursor.execute("""insert into takes(roll_no,course_code) values("{}","2cs401")""".format(roll21))
        db.commit()

    
def register_users():
    username_info = username1.get()
    password_info = password1.get()
    section_info = section.get()
    email_info = email1.get()
    roll_info = roll1.get()
    year_info = year.get()

    try:
        cursor.execute("""INSERT INTO student(name,roll_no,email,password,section,year) VALUES("{}", "{}","{}","{}", "{}","{}")""".format(username_info,roll_info,email_info,password_info,section_info,year_info))
        db.commit()
        Label(reg, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        login1s()
    except:
        useds()

def useds():
    reg.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="Email address already registered").pack()
    Label(text="").pack()
    Button(project, text="Register", bg="#fdb5c4",command=registers).pack()
        
def usedf():
    reg.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="Email address already registered").pack()
    Label(text="").pack()
    Button(project, text="Register", bg="#fdb5c4",command=registerf).pack()

def login1s():
    reg.destroy()
    global log
    log = Tk()
    log.configure(background="#c0fab8")
    log.title("Login Student")
    log.geometry("300x250")
    Label(log, text="Please enter details below to login").pack()
    Label(log, text="").pack()

    global username_verifys
    global password_verifys

    username_verifys = StringVar()
    password_verifys = StringVar()

    global username_login_entrys
    global password_login_entrys

    Label(log, text="Email * ").pack()
    username_login_entrys = Entry(log, textvariable=username_verifys)
    username_login_entrys.pack()
    Label(log, text="").pack()
    Label(log, text="Password * ").pack()
    password_login_entrys = Entry(log, textvariable=password_verifys, show= '*')
    password_login_entrys.pack()
    Label(log, text="").pack()
    Button(log, text="Login", width=10, height=1,bg="#fdb5c4", command = login_verifys).pack()

def login1f():
    reg.destroy()
    global log
    log = Tk()
    log.configure(background="#c0fab8")
    log.title("Login Faculty")
    log.geometry("300x250")
    Label(log, text="Please enter details below to login").pack()
    Label(log, text="").pack()

    global username_verifyf
    global password_verifyf

    username_verifyf = StringVar()
    password_verifyf = StringVar()

    global username_login_entryf
    global password_login_entryf

    Label(log, text="Email * ").pack()
    username_login_entryf = Entry(log, textvariable=username_verifyf)
    username_login_entryf.pack()
    Label(log, text="").pack()
    Label(log, text="Password * ").pack()
    password_login_entryf = Entry(log, textvariable=password_verifyf, show= '*')
    password_login_entryf.pack()
    Label(log, text="").pack()
    Button(log, text="Login", width=10, height=1,bg="#fdb5c4", command = login_verifyf).pack()
    
def logins():
    project.destroy()
    global log
    log = Tk()
    log.configure(background="#c0fab8")
    log.title("Login Student")
    log.geometry("300x250")
    Label(log, text="Please enter details below to login").pack()
    Label(log, text="").pack()

    global username_verifys
    global password_verifys

    username_verifys = StringVar()
    password_verifys = StringVar()

    global username_login_entrys
    global password_login_entrys

    Label(log, text="Email * ").pack()
    username_login_entrys = Entry(log, textvariable=username_verifys)
    username_login_entrys.pack()
    Label(log, text="").pack()
    Label(log, text="Password * ").pack()
    password_login_entrys = Entry(log, textvariable=password_verifys, show= '*')
    password_login_entrys.pack()
    Label(log, text="").pack()
    Button(log, text="Login", width=10, height=1,bg="#fdb5c4", command = login_verifys).pack()

def login_verifys():
    global username11
    username11 = username_verifys.get()
    global password11
    password11 = password_verifys.get()

    username_login_entrys.delete(0, END)
    password_login_entrys.delete(0, END)
    cursor.execute("(SELECT password FROM student WHERE email LIKE %s)", (username11,))
    flag1=0
    for i in cursor:
        if password11 in list(i):
            login_sucesss()
            flag1 = 1
        else:
            password_not_recogniseds()
            flag1 = 1
    if flag1 == 0:
        user_not_founds()
        
def loginf():
    project.destroy()
    global log
    log = Tk()
    log.configure(background="#c0fab8")
    log.title("Login Faculty")
    log.geometry("300x250")
    Label(log, text="Please enter details below to login").pack()
    Label(log, text="").pack()

    global username_verifyf
    global password_verifyf

    username_verifyf = StringVar()
    password_verifyf = StringVar()

    global username_login_entryf
    global password_login_entryf

    Label(log, text="Email * ").pack()
    username_login_entryf = Entry(log, textvariable=username_verifyf)
    username_login_entryf.pack()
    Label(log, text="").pack()
    Label(log, text="Password * ").pack()
    password_login_entryf = Entry(log, textvariable=password_verifyf, show= '*')
    password_login_entryf.pack()
    Label(log, text="").pack()
    Button(log, text="Login", width=10, height=1,bg="#fdb5c4", command = login_verifyf).pack()
    
def login_verifyf():
    global username10
    username10 = username_verifyf.get()
    global password10
    password10 = password_verifyf.get()

    username_login_entryf.delete(0, END)
    password_login_entryf.delete(0, END)
    cursor.execute("(SELECT password FROM faculty WHERE email LIKE %s)", (username10,))
    flag1=0
    for i in cursor:
        if password10 in list(i):
            login_sucessf()
            flag1 = 1
        else:
            password_not_recognisedf()
            flag1 = 1
    if flag1 == 0:
        user_not_foundf()

def take():
    new_student=roll.get()
    name1=name.get()
    flag=0
    cursor.execute("(SELECT roll_no FROM student WHERE roll_no LIKE %s)", (new_student,))
    for i in cursor:
        flag=1
    if flag == 1:
        try:
            cursor.execute("""INSERT INTO sample(name,roll_no) VALUES("{}", "{}")""".format(name1,new_student))
            db.commit()
            collect.take(new_student)
            messagebox.showinfo('Adding new student','Student added successfully')
            
        except:
            messagebox.showinfo('Student already exist','Sample of student already taken!!!')
            project.destroy()
            new1()
    else:
        messagebox.showinfo('Student does not exist','Student does not registered yet!!!')
        project.destroy()
        new1()
    
        
def login_sucesss():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Success")
    project.geometry("150x100")
    Label(project, text="Login Success").pack()
    Label(text="").pack()
    Button(project, text="Go to main window",bg="#fdb5c4", command=atts).pack()

def login_sucessf():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Success")
    project.geometry("150x100")
    Label(project, text="Login Success").pack()
    Label(text="").pack()
    Button(project, text="Go to main window",bg="#fdb5c4", command=attf).pack()
    
def train1():
    messagebox.showinfo('Training data','Training Data Please Wait for 5 Minutes')
    train.train1()
    messagebox.showinfo('Training data','Data trained successfully')

def new():
    top.destroy()
    global project
    project=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    
    project.geometry("600x450+382+167")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Add Student")
    project.configure(background="#d9d9d9")
    project.configure(highlightbackground="#d9d9d9")
    project.configure(highlightcolor="black")
    
    
    Label1 = Label(project,activebackground="#f9f9f9",activeforeground="black",background="#b5c4fd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''Student Name''')
    Label1.place(relx=0.133, rely=0.578, height=30, width=124)
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\student.png"
    global _img5
    _img5 = PhotoImage(file=photo_location)
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#c6ece0",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img5,pady="0",text='''Button''')
    Button1.place(relx=-0.017, rely=-0.022, height=230, width=617)
            
    Label2 = Label(project,activebackground="#f9f9f9",activeforeground="black",background="#b5c4fd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''Roll No.''')
    Label2.place(relx=0.133, rely=0.667, height=30, width=124)
            
    Button2 = Button(project,command=take,activebackground="#ececec",activeforeground="#000000",background="#fbc6b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Take Samples''')
    Button2.place(relx=0.283, rely=0.822, height=40, width=147)
    
    
    global name
    global roll
    name = StringVar()
    roll = StringVar()
    
    Entry5 = Entry(project,textvariable=name,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="#c4c4c4",selectforeground="black")
    Entry5.place(relx=0.367, rely=0.578,height=30, relwidth=0.39)    
    
    Entry6 = Entry(project,textvariable=roll,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="#c4c4c4",selectforeground="black")
    Entry6.place(relx=0.367, rely=0.667,height=30, relwidth=0.39)
    
    Entry5.delete(0, END)
    Entry6.delete(0, END)
    
            
    Button3 = Button(project,command=attf,activebackground="#ececec",activeforeground="#000000",background="#fbc6b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button3.place(relx=0.6, rely=0.822, height=34, width=86)
    project.mainloop()

def new1():
    global project
    project=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    
    project.geometry("600x450+382+167")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Add Student")
    project.configure(background="#d9d9d9")
    project.configure(highlightbackground="#d9d9d9")
    project.configure(highlightcolor="black")
    
    
    Label1 = Label(project,activebackground="#f9f9f9",activeforeground="black",background="#b5c4fd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''Student Name''')
    Label1.place(relx=0.133, rely=0.578, height=30, width=124)
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\student.png"
    global _img5
    _img5 = PhotoImage(file=photo_location)
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#c6ece0",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img5,pady="0",text='''Button''')
    Button1.place(relx=-0.017, rely=-0.022, height=230, width=617)
            
    Label2 = Label(project,activebackground="#f9f9f9",activeforeground="black",background="#b5c4fd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''Roll No.''')
    Label2.place(relx=0.133, rely=0.667, height=30, width=124)
            
    Button2 = Button(project,command=take,activebackground="#ececec",activeforeground="#000000",background="#fbc6b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Take Samples''')
    Button2.place(relx=0.283, rely=0.822, height=40, width=147)   
    
    
    global name
    global roll
    name = StringVar()
    roll = StringVar()
    
    Entry5 = Entry(project,textvariable=name,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="#c4c4c4",selectforeground="black")
    Entry5.place(relx=0.367, rely=0.578,height=30, relwidth=0.39)    
    
    Entry6 = Entry(project,textvariable=roll,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="#c4c4c4",selectforeground="black")
    Entry6.place(relx=0.367, rely=0.667,height=30, relwidth=0.39)
    Entry5.delete(0, END)
    Entry6.delete(0, END)
    
            
    Button3 = Button(project,command=attf,activebackground="#ececec",activeforeground="#000000",background="#fbc6b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button3.place(relx=0.6, rely=0.822, height=34, width=86)
    project.mainloop()
    
def took1():
    detector = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt","res10_300x300_ssd_iter_140000.caffemodel")
    embedder = cv2.dnn.readNetFromTorch("openface_nn4.small2.v1.t7")
    recognizer = pickle.loads(open("recognizer.pickle", "rb").read())
    le = pickle.loads(open("le.pickle", "rb").read())

    capture=cv2.VideoCapture(0)
    present=[]
    dic={}
    while(True):
        _,frame=capture.read()
        frame = imutils.resize(frame, width=600)
        (h, w) = frame.shape[:2]

        imageBlob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300),(104.0, 177.0, 123.0), swapRB=False, crop=False)

        detector.setInput(imageBlob)
        detected_faces = detector.forward()
        
        for i in range(0, detected_faces.shape[2]):
            confidence = detected_faces[0, 0, i, 2]
            if confidence > 0.6:
                box = detected_faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                face = frame[startY:endY, startX:endX]
                (fH, fW) = face.shape[:2]
                
                if fW < 20 or fH < 20:
                    continue

                faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,(96, 96), (0, 0, 0), swapRB=True, crop=False)
                embedder.setInput(faceBlob)
                vec = embedder.forward()

                preds = recognizer.predict_proba(vec)[0]
                j = np.argmax(preds)
                proba = preds[j]
                name = le.classes_[j]
                
                if name in dic:
                    dic[name]+=1
                else:
                    dic[name]=1

                text = "{}: {:.2f}%".format(name, proba * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.rectangle(frame, (startX, startY), (endX, endY),(0, 0, 255), 2)
                cv2.putText(frame, text, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

            
        cv2.imshow('Recognizing faces',frame)
        if cv2.waitKey(1)==13:
            break
    
    for roll_no in dic:
        if(dic[roll_no]>=100):
            present.append(roll_no)
    code1=code.get()  
    fname1=fname.get()
    ccode1=ccode.get()
    if "unknown" in present: 
        present.remove("unknown")  
    cursor.execute("(SELECT roll_no FROM takes WHERE course_code LIKE %s)", (code1,))
    r=cursor.fetchall()
    time = str(date.today())
    for i in r:
        if i[0] in present:
            cursor.execute("""insert into attendance(course_code,roll_no,date,status) values("{}","{}","{}","PRESENT")""".format(code1 ,i[0], time))
            db.commit()
        else:
            cursor.execute("""insert into attendance(course_code,roll_no,date,status) values("{}","{}","{}","ABSENT")""".format(code1 ,i[0], time))
            db.commit()
    try:
        cursor.execute("""insert into teaches(fname,course_code,password) values("{}","{}","{}")""".format(fname1,code1,ccode1))
        db.commit()
    except:
        messagebox.showinfo('Attendance ','Password entered at first time is valid password')

    capture.release()
    cv2.destroyAllWindows()
    capture.release()
    cv2.destroyAllWindows()
    messagebox.showinfo('Attendance ','Attendance of all students in the frame is taken')

def recognize():
    top.destroy()
    global project
    project=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
     
    project.geometry("600x450+372+188")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("New projectlevel")
    project.configure(background="#d9d9d9")
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\att.png"
    global _img0
    _img0 = PhotoImage(file=photo_location)
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#d5bbf7",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img0,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=204, width=597)
    
    Label1 = Label(project,background="#00ffff",disabledforeground="#a3a3a3",foreground="#000000",text='''Couse Code''')
    Label1.place(relx=0.2, rely=0.522, height=31, width=130)
    
    Label2 = Label(project,background="#00ffff",disabledforeground="#a3a3a3",foreground="#000000",text='''Faculty Name''')
    Label2.place(relx=0.2, rely=0.622, height=31, width=130)
    
    Label3 = Label(project,background="#00ffff",disabledforeground="#a3a3a3",foreground="#000000",text='''Course Password''')
    Label3.place(relx=0.2, rely=0.722, height=31, width=130)
    
    global code
    code = StringVar()
    global fname
    fname = StringVar()
    global ccode
    ccode = StringVar()
    Entry1 = Entry(project,textvariable=code,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry1.place(relx=0.433, rely=0.522,height=30, relwidth=0.29)
    Entry1.delete(0, END)
    
    Entry2 = Entry(project,textvariable=fname,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry2.place(relx=0.433, rely=0.622,height=30, relwidth=0.29)
    Entry2.delete(0, END)
    
    Entry3 = Entry(project,textvariable=ccode,show='*',background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry3.place(relx=0.433, rely=0.722,height=30, relwidth=0.29)
    Entry3.delete(0, END)
    
    Button2 = Button(project,command=took1,activebackground="#ececec",activeforeground="#000000",background="#fcb6ce",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Take Attandance''')
    Button2.place(relx=0.233, rely=0.856, height=24, width=120)
        
    Button3 = Button(project,command=attf,activebackground="#ececec",activeforeground="#000000",background="#fcb6ce",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button3.place(relx=0.467, rely=0.856, height=24, width=76)
    project.mainloop()

def show3():
    pass1=ccode10.get()
    rol1=roll10.get()
    cod1=code10.get()
    dat1=date10.get()
    cursor.execute("select password from teaches where course_code like %s", (cod1,))
    for i in cursor:
        if pass1 in list(i):
            try:
                cursor.execute("""insert into attendance(roll_no,course_code,date,status) values("{}","{}","{}","PRESENT")""".format(rol1, cod1, dat1))
                messagebox.showinfo('Added ','Attendance of student added successfully')
                db.commit()
            except:
                pass
        else:
            messagebox.showinfo('Wrong ','Wrong Password please try again!!!')
    project.destroy()
    showt()

def show3s():
    messagebox.showinfo('No permission ','You do not have permission to add attendance,you can only check attendance!!!')
    
def show4s():
    messagebox.showinfo('No permission ','You do not have permission to delete attendance,you can only check attendance!!!')  
    
    
    
def show4():
    pass19=ccode10.get()
    rol19=roll10.get()
    cod19=code10.get()
    dat19=date10.get()
    cursor.execute("select password from teaches where course_code like %s", (cod19,))
    for i in cursor:
        if pass19 in list(i):
            try:
                cursor.execute("delete from attendance where course_code like %s and roll_no like %s and date like %s", (cod19, rol19, dat19,))
                messagebox.showinfo('Delete ','Attendance of student delete successfully')
                db.commit()
            except:
                pass
        else:
            messagebox.showinfo('Wrong ','Wrong Password please try again!!!')
    project.destroy()
    showt()
        
        
def show2():
    project.destroy()
    global top
    top=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    
    top.geometry("1176x652+94+95")
    top.minsize(120, 1)
    top.maxsize(1354, 733)
    top.resizable(1, 1)
    top.title("Show2")
    top.configure(background="#c5f1f3")
    
    Label1 = Label(top,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''Click on + button to display more information''')
    Label1.place(relx=0.01, rely=0.01, height=49, width=1200)
    
    Button1 = Button(top,command=show,activebackground="#ececec",activeforeground="#000000",background="#fcc8b6",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button1.place(relx=0.483, rely=0.95, height=24, width=86)
    
    roll0=code9.get()
    tree= ttk.Treeview(top)
    tree["columns"]=("one","two","three","four")
    tree.column("#0", width=20, minwidth=0, stretch=NO)
    tree.column("one", width=150, minwidth=150, stretch=NO)
    tree.column("two", width=200, minwidth=150,stretch=NO)
    tree.column("three", width=150, minwidth=150, stretch=NO)
    tree.column("four", width=150, minwidth=150, stretch=NO)
    tree.heading("#0",text="",anchor=W)
    tree.heading("one", text="",anchor=W)
    tree.heading("two", text="",anchor=W)
    tree.heading("three", text="",anchor=W)
    tree.heading("four", text="",anchor=W)
    cursor.execute("select course_name from course where course_code like %s", (roll0,))
    c=cursor.fetchall()
    cursor.execute("select sem from course where course_code like %s", (roll0,))
    c5=cursor.fetchall()
    tree.insert('','end',values=("Course Name",c[0],"Semester",c5[0]))
    e=5
    cursor.execute("select roll_no from takes where course_code like %s", (roll0,))
    a = cursor.fetchall()
    for i in a:
        cursor.execute("select name from student where roll_no like %s", (i[0],))
        x = cursor.fetchall()
        cursor.execute("select * from attendance where roll_no like %s and course_code like %s", (i[0], roll0))
        a1 = cursor.fetchall()
        cursor.execute("select * from attendance where roll_no like %s and course_code like %s and status like %s", (i[0], roll0, "PRESENT"))
        b1 = cursor.fetchall()
        cursor.execute("select * from attendance where roll_no like %s and course_code like %s and status like %s", (i[0], roll0, "ABSENT"))
        c1 = cursor.fetchall()
        try:
            r=(len(b1)/len(a1))*100
            r1=str(r)+'%'
        except:
            r1="NO Lecture has been taken yet"
        for j in x:
            tree.insert('','end','m'+str(e),values=(x[0],r1))
        tree.insert('m'+str(e),'end',text="",values=("Course_Code","Roll_no","Date","Status"))
        cursor.execute("select * from attendance where roll_no like %s and course_code like %s", (i[0], roll0))
        b = cursor.fetchall()
        for k in b:
            tree.insert('m'+str(e),'end',text="",values=k)
        
        tree.insert('m'+str(e),'end',text="",values=("Total Lecture taken",str(len(a1))))
        
        tree.insert('m'+str(e),'end',text="",values=("Total Present",str(len(b1))))
        
        tree.insert('m'+str(e),'end',text="",values=("Total Absent",str(len(c1))))
        e = e+1
    tree.place(relx=0.01, rely=0.1, height=550, width=1150)
    top.mainloop()
    
def show1():
    project.destroy()
    global top
    top=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    
    top.geometry("1176x652+94+95")
    top.minsize(120, 1)
    top.maxsize(1354, 733)
    top.resizable(1, 1)
    top.title("Show1")
    top.configure(background="#c5f1f3")
    
    Label1 = Label(top,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''Click on + button to display more information''')
    Label1.place(relx=0.01, rely=0.01, height=49, width=1200)
    
    Button1 = Button(top,command=show,activebackground="#ececec",activeforeground="#000000",background="#fcc8b6",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button1.place(relx=0.483, rely=0.95, height=24, width=86)
    
    roll0=roll9.get()
    tree= ttk.Treeview(top)
    tree["columns"]=("one","two","three","four")
    tree.column("#0", width=20, minwidth=0, stretch=NO)
    tree.column("one", width=150, minwidth=150, stretch=NO)
    tree.column("two", width=200, minwidth=150,stretch=NO)
    tree.column("three", width=150, minwidth=150, stretch=NO)
    tree.column("four", width=150, minwidth=150, stretch=NO)
    tree.heading("#0",text="",anchor=W)
    tree.heading("one", text="",anchor=W)
    tree.heading("two", text="",anchor=W)
    tree.heading("three", text="",anchor=W)
    tree.heading("four", text="",anchor=W)
    tree.insert('','end',values=("Student Name","email","year","section"))
    cursor.execute("select email from student where roll_no like %s", (roll0,))
    a2 = cursor.fetchall()
    cursor.execute("select year from student where roll_no like %s", (roll0,))
    b2 = cursor.fetchall()
    cursor.execute("select section from student where roll_no like %s", (roll0,))
    c2 = cursor.fetchall()
    cursor.execute("select name from student where roll_no like %s", (roll0,))
    x = cursor.fetchall()
    
    tree.insert('','end',values=(x[0],a2[0],b2[0],c2[0]))
    e=5
    cursor.execute("select course_code from takes where roll_no like %s", (roll0,))
    a = cursor.fetchall()
    for i in a:
        cursor.execute("select course_name from course where course_code like %s", (i[0],))
        c=cursor.fetchall()
        cursor.execute("select sem from course where course_code like %s", (i[0],))
        c5=cursor.fetchall()
        cursor.execute("select * from attendance where roll_no like %s and course_code like %s", (roll0, i[0]))
        a1 = cursor.fetchall()
        cursor.execute("select * from attendance where roll_no like %s and course_code like %s and status like %s", (roll0, i[0], "PRESENT"))
        b1 = cursor.fetchall()
        cursor.execute("select * from attendance where roll_no like %s and course_code like %s and status like %s", (roll0, i[0], "ABSENT"))
        c1 = cursor.fetchall()
        try:
            r=(len(b1)/len(a1))*100
            r1=str(r)+'%'
        except:
            r1="NO Lecture has been taken yet"
        
        for j in c:
            tree.insert('','end','m'+str(e),values=(c[0],r1,"Semester",c5[0]))
        tree.insert('m'+str(e),'end',text="",values=("Course_Code","Roll_no","Date","Status"))
        cursor.execute("select * from attendance where roll_no like %s and course_code like %s", (roll0, i[0]))
        b = cursor.fetchall()
        for k in b:
            tree.insert('m'+str(e),'end',text="",values=k)
        
        tree.insert('m'+str(e),'end',text="",values=("Total Lecture taken",str(len(a1))))
        
        tree.insert('m'+str(e),'end',text="",values=("Total Present",str(len(b1))))
        
        tree.insert('m'+str(e),'end',text="",values=("Total Absent",str(len(c1))))
        e = e+1
        
    tree.place(relx=0.01, rely=0.1, height=550, width=1150)
    top.mainloop()

    
def showt():    
    global project
    project=Tk()
    global roll9
    global code9
    roll9 = StringVar()
    code9 = StringVar()
    global roll10
    global code10
    roll10 = StringVar()
    code10 = StringVar()
    global date10
    global ccode10
    date10 = StringVar()
    ccode10 = StringVar()
    
    
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'

    project.geometry("809x550+275+116")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Check")
    project.configure(background="#c5f1f3")

    photo_location = "C:\\Users\\SHIVAM\\Desktop\\check.png"
    global _img30
    _img30 = PhotoImage(file=photo_location)   
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#e8f7bb",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img30,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=160, width=807)

    Button2 = Button(project,command=show2,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Show''')
    Button2.place(relx=0.754, rely=0.436, height=30, width=87)

    Label1 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''To update attendance add student roll_no,Course code,Course Password and date and click on add or delete button''')
    Label1.place(relx=0.025, rely=0.527, height=49, width=728)

    Label2 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''Check attendance for your course''')
    Label2.place(relx=0.025, rely=0.418, height=39, width=198)

    Button3 = Button(project,command=show1,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Show''')
    Button3.place(relx=0.754, rely=0.345, height=30, width=87)
    
    Label3 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''Check attendance for your roll_no''')
    Label3.place(relx=0.025, rely=0.327, height=39, width=199)
    
    Button4 = Button(project,command=show3,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add''')
    Button4.place(relx=0.346, rely=0.8, height=30, width=77)
    
    Button5 =Button(project,command=show4,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Delete''')
    Button5.place(relx=0.482, rely=0.8, height=30, width=77)

    Entry1 = Entry(project,textvariable=roll9,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry1.place(relx=0.297, rely=0.345,height=30, relwidth=0.425)
    Entry1.delete(0, END)
    
    Entry2 = Entry(project,textvariable=code9,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry2.place(relx=0.297, rely=0.436,height=30, relwidth=0.425)
    Entry2.delete(0, END)
    
    Entry3 =Entry(project,textvariable=roll10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry3.place(relx=0.222, rely=0.636,height=30, relwidth=0.178)
    Entry3.delete(0, END)
    
    Entry4 = Entry(project,textvariable=code10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry4.place(relx=0.63, rely=0.709,height=30, relwidth=0.19)
    Entry4.delete(0, END)
    
    Entry5 = Entry(project,textvariable=ccode10,show='*',background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry5.place(relx=0.222, rely=0.709,height=30, relwidth=0.178)
    Entry5.delete(0, END)
    
    Entry6 = Entry(project,textvariable=date10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry6.place(relx=0.63, rely=0.636,height=30, relwidth=0.19)
    Entry6.delete(0, END)
    
    Label4 = Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Course_Password''')
    Label4.place(relx=0.062, rely=0.709, height=30, width=113)

    Label5 = Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Date''')
    Label5.place(relx=0.494, rely=0.636, height=31, width=84)

    Label6 =Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Course_Code''')
    Label6.place(relx=0.494, rely=0.709, height=30, width=84)
    
    Label7 =Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Roll_no''')
    Label7.place(relx=0.062, rely=0.636, height=30, width=113)

    Button6 = Button(project,command=attf,activebackground="#ececec",activeforeground="#000000",background="#f2ee53",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button6.place(relx=0.408, rely=0.909, height=40, width=97)
    project.mainloop()


def shows():    
    top.destroy()
    global project
    project=Tk()
    global roll9
    global code9
    roll9 = StringVar()
    code9 = StringVar()
    global roll10
    global code10
    roll10 = StringVar()
    code10 = StringVar()
    global date10
    global ccode10
    date10 = StringVar()
    ccode10 = StringVar()
    
    
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'

    project.geometry("809x550+275+116")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Check")
    project.configure(background="#c5f1f3")

    photo_location = "C:\\Users\\SHIVAM\\Desktop\\check.png"
    global _img30
    _img30 = PhotoImage(file=photo_location)   
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#e8f7bb",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img30,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=160, width=807)

    Button2 = Button(project,command=show2,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Show''')
    Button2.place(relx=0.754, rely=0.436, height=30, width=87)

    Label1 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''To update attendance add student roll_no,Course code,Course Password and date and click on add or delete button''')
    Label1.place(relx=0.025, rely=0.527, height=49, width=728)

    Label2 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''Check attendance for your course''')
    Label2.place(relx=0.025, rely=0.418, height=39, width=198)

    Button3 = Button(project,command=show1,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Show''')
    Button3.place(relx=0.754, rely=0.345, height=30, width=87)
    
    Label3 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''Check attendance for your roll_no''')
    Label3.place(relx=0.025, rely=0.327, height=39, width=199)
    
    Button4 = Button(project,command=show3s,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add''')
    Button4.place(relx=0.346, rely=0.8, height=30, width=77)
    
    Button5 =Button(project,command=show4s,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Delete''')
    Button5.place(relx=0.482, rely=0.8, height=30, width=77)

    Entry1 = Entry(project,textvariable=roll9,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry1.place(relx=0.297, rely=0.345,height=30, relwidth=0.425)
    Entry1.delete(0, END)
    
    Entry2 = Entry(project,textvariable=code9,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry2.place(relx=0.297, rely=0.436,height=30, relwidth=0.425)
    Entry2.delete(0, END)
    
    Entry3 =Entry(project,textvariable=roll10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry3.place(relx=0.222, rely=0.636,height=30, relwidth=0.178)
    Entry3.delete(0, END)
    
    Entry4 = Entry(project,textvariable=code10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry4.place(relx=0.63, rely=0.709,height=30, relwidth=0.19)
    Entry4.delete(0, END)
    
    Entry5 = Entry(project,textvariable=ccode10,show='*',background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry5.place(relx=0.222, rely=0.709,height=30, relwidth=0.178)
    Entry5.delete(0, END)
    
    Entry6 = Entry(project,textvariable=date10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry6.place(relx=0.63, rely=0.636,height=30, relwidth=0.19)
    Entry6.delete(0, END)
    
    Label4 = Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Course_Password''')
    Label4.place(relx=0.062, rely=0.709, height=30, width=113)

    Label5 = Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Date''')
    Label5.place(relx=0.494, rely=0.636, height=31, width=84)

    Label6 =Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Course_Code''')
    Label6.place(relx=0.494, rely=0.709, height=30, width=84)
    
    Label7 =Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Roll_no''')
    Label7.place(relx=0.062, rely=0.636, height=30, width=113)

    Button6 = Button(project,command=atts,activebackground="#ececec",activeforeground="#000000",background="#f2ee53",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button6.place(relx=0.408, rely=0.909, height=40, width=97)
    project.mainloop()
    
    
def show():    
    top.destroy()
    global project
    project=Tk()
    global roll9
    global code9
    roll9 = StringVar()
    code9 = StringVar()
    global roll10
    global code10
    roll10 = StringVar()
    code10 = StringVar()
    global date10
    global ccode10
    date10 = StringVar()
    ccode10 = StringVar()
    
    
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'

    project.geometry("809x550+275+116")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Check")
    project.configure(background="#c5f1f3")

    photo_location = "C:\\Users\\SHIVAM\\Desktop\\check.png"
    global _img30
    _img30 = PhotoImage(file=photo_location)   
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#e8f7bb",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img30,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=160, width=807)

    Button2 = Button(project,command=show2,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Show''')
    Button2.place(relx=0.754, rely=0.436, height=30, width=87)

    Label1 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''To update attendance add student roll_no,Course code,Course Password and date and click on add or delete button''')
    Label1.place(relx=0.025, rely=0.527, height=49, width=728)

    Label2 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''Check attendance for your course''')
    Label2.place(relx=0.025, rely=0.418, height=39, width=198)

    Button3 = Button(project,command=show1,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Show''')
    Button3.place(relx=0.754, rely=0.345, height=30, width=87)
    
    Label3 = Label(project,background="#98fb4f",disabledforeground="#a3a3a3",foreground="#000000",text='''Check attendance for your roll_no''')
    Label3.place(relx=0.025, rely=0.327, height=39, width=199)
    
    Button4 = Button(project,command=show3,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add''')
    Button4.place(relx=0.346, rely=0.8, height=30, width=77)
    
    Button5 =Button(project,command=show4,activebackground="#ececec",activeforeground="#000000",background="#fbc8b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Delete''')
    Button5.place(relx=0.482, rely=0.8, height=30, width=77)

    Entry1 = Entry(project,textvariable=roll9,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry1.place(relx=0.297, rely=0.345,height=30, relwidth=0.425)
    Entry1.delete(0, END)
    
    Entry2 = Entry(project,textvariable=code9,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry2.place(relx=0.297, rely=0.436,height=30, relwidth=0.425)
    Entry2.delete(0, END)
    
    Entry3 =Entry(project,textvariable=roll10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry3.place(relx=0.222, rely=0.636,height=30, relwidth=0.178)
    Entry3.delete(0, END)
    
    Entry4 = Entry(project,textvariable=code10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry4.place(relx=0.63, rely=0.709,height=30, relwidth=0.19)
    Entry4.delete(0, END)
    
    Entry5 = Entry(project,textvariable=ccode10,show='*',background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry5.place(relx=0.222, rely=0.709,height=30, relwidth=0.178)
    Entry5.delete(0, END)
    
    Entry6 = Entry(project,textvariable=date10,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry6.place(relx=0.63, rely=0.636,height=30, relwidth=0.19)
    Entry6.delete(0, END)
    
    Label4 = Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Course_Password''')
    Label4.place(relx=0.062, rely=0.709, height=30, width=113)

    Label5 = Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Date''')
    Label5.place(relx=0.494, rely=0.636, height=31, width=84)

    Label6 =Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Course_Code''')
    Label6.place(relx=0.494, rely=0.709, height=30, width=84)
    
    Label7 =Label(project,background="#c2c864",disabledforeground="#a3a3a3",foreground="#000000",text='''Roll_no''')
    Label7.place(relx=0.062, rely=0.636, height=30, width=113)

    Button6 = Button(project,command=attf,activebackground="#ececec",activeforeground="#000000",background="#f2ee53",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button6.place(relx=0.408, rely=0.909, height=40, width=97)
    project.mainloop()

def attf():
    project.destroy()
    global top
    top=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font11 = "-family {Times New Roman} -size 12"
    font9 = "-family {Times New Roman} -size 24 -slant italic"
    
    top.geometry("821x540+270+131")
    top.minsize(120, 1)
    top.maxsize(1362, 741)
    top.resizable(1, 1)
    top.title("Main Window")
    top.configure(background="#f0edc1")
    
    Label1 = Label(top,activebackground="#f0fde3",activeforeground="#000000",background="#ddf5bc",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Welcome To CampusLynx''')
    Label1.place(relx=0.398, rely=0.0, height=181, width=496)
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\py.png"
    global _img0
    _img0 = PhotoImage(file=photo_location)
    Button1 = Button(top,activebackground="#ffffff",activeforeground="#ffffff",background="#ddf5bc",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img0,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=184, width=367)

   
    Button2 = Button(top,command=new,activebackground="#ececec",activeforeground="#000000",background="#cae7e8",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add New Student''')
    Button2.place(relx=0.024, rely=0.722, height=24, width=134)
        
    Button3 = Button(top,command=recognize,activebackground="#ececec",activeforeground="#000000",background="#cae7e8",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Take attendance''')
    Button3.place(relx=0.536, rely=0.722, height=24, width=128)
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\new1.png"
    global _img1
    _img1 = PhotoImage(file=photo_location)
    Button4 = Button(top,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img1,pady="0",text='''Button''')
    Button4.place(relx=0.012, rely=0.481, height=124, width=167)
        
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\mark.png"
    global _img2
    _img2 = PhotoImage(file=photo_location)
    Button5 = Button(top,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img2,pady="0",text='''Button''')
    Button5.place(relx=0.512, rely=0.5, height=114, width=176)
    
    Button7 =Button(top,command=logout,activebackground="#fae6de",activeforeground="#000000",background="#f2cebf",disabledforeground="#a3a3a3",font=font11,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Logout''')
    Button7.place(relx=0.438, rely=0.87, height=34, width=89)
    
    Button8 = Button(top,command=train1,activebackground="#ececec",activeforeground="#000000",background="#cae7e8",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Train Data''')
    Button8.place(relx=0.28, rely=0.722, height=24, width=125)   
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\train.png"
    global _img3
    _img3 = PhotoImage(file=photo_location)
    Button9 = Button(top,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img3,pady="0",text='''Button''')
    Button9.place(relx=0.256, rely=0.5, height=114, width=181)
       
    Button10 = Button(top,command=show,activebackground="#ececec",activeforeground="#000000",background="#cae7e8",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Check attendance''')
    Button10.place(relx=0.816, rely=0.722, height=24, width=106)
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\data.png"
    global _img4
    _img4 = PhotoImage(file=photo_location)
    Button11 =Button(top,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img4,pady="0",text='''Button''')
    Button11.place(relx=0.767, rely=0.5, height=114, width=171)
    top.mainloop()

def per():
    messagebox.showinfo('No permisssion ','You do not have permission to access this particular field you can only check your attendance')

    
def atts():
    project.destroy()
    global top
    top=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font11 = "-family {Times New Roman} -size 12"
    font9 = "-family {Times New Roman} -size 24 -slant italic"
    
    top.geometry("821x540+270+131")
    top.minsize(120, 1)
    top.maxsize(1362, 741)
    top.resizable(1, 1)
    top.title("Main Window")
    top.configure(background="#f0edc1")
    
    Label1 = Label(top,activebackground="#f0fde3",activeforeground="#000000",background="#ddf5bc",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Welcome To CampusLynx''')
    Label1.place(relx=0.398, rely=0.0, height=181, width=496)
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\py.png"
    global _img0
    _img0 = PhotoImage(file=photo_location)
    Button1 = Button(top,activebackground="#ffffff",activeforeground="#ffffff",background="#ddf5bc",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img0,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=184, width=367)

   
    Button2 = Button(top,command=per,activebackground="#ececec",activeforeground="#000000",background="#cae7e8",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add New Student''')
    Button2.place(relx=0.024, rely=0.722, height=24, width=134)
        
    Button3 = Button(top,command=per,activebackground="#ececec",activeforeground="#000000",background="#cae7e8",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Take attendance''')
    Button3.place(relx=0.536, rely=0.722, height=24, width=128)
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\new1.png"
    global _img1
    _img1 = PhotoImage(file=photo_location)
    Button4 = Button(top,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img1,pady="0",text='''Button''')
    Button4.place(relx=0.012, rely=0.481, height=124, width=167)
        
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\mark.png"
    global _img2
    _img2 = PhotoImage(file=photo_location)
    Button5 = Button(top,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img2,pady="0",text='''Button''')
    Button5.place(relx=0.512, rely=0.5, height=114, width=176)
    
    Button7 =Button(top,command=logout,activebackground="#fae6de",activeforeground="#000000",background="#f2cebf",disabledforeground="#a3a3a3",font=font11,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Logout''')
    Button7.place(relx=0.438, rely=0.87, height=34, width=89)
    
    Button8 = Button(top,command=per,activebackground="#ececec",activeforeground="#000000",background="#cae7e8",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Train Data''')
    Button8.place(relx=0.28, rely=0.722, height=24, width=125)   
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\train.png"
    global _img3
    _img3 = PhotoImage(file=photo_location)
    Button9 = Button(top,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img3,pady="0",text='''Button''')
    Button9.place(relx=0.256, rely=0.5, height=114, width=181)
       
    Button10 = Button(top,command=shows,activebackground="#ececec",activeforeground="#000000",background="#cae7e8",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Check attendance''')
    Button10.place(relx=0.816, rely=0.722, height=24, width=106)
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\data.png"
    global _img4
    _img4 = PhotoImage(file=photo_location)
    Button11 =Button(top,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img4,pady="0",text='''Button''')
    Button11.place(relx=0.767, rely=0.5, height=114, width=171)
    top.mainloop()
    
def password_not_recogniseds():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="Invalid Password!!!").pack()
    Label(text="").pack()
    Button(project, text="Try again",bg="#fdb5c4", command=logins).pack()
    
def password_not_recognisedf():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="Invalid Password!!!").pack()
    Label(text="").pack()
    Button(project, text="Try again",bg="#fdb5c4", command=loginf).pack()
    
def user_not_founds():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="User Not Found").pack()
    Label(text="").pack()
    Button(project, text="Register", bg="#fdb5c4",command=registers).pack()

def user_not_foundf():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="User Not Found").pack()
    Label(text="").pack()
    Button(project, text="Register", bg="#fdb5c4",command=registerf).pack()
    
def mainscreen():
    global project
    project=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
 
    project.geometry("1100x500")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Main")
    project.configure(background="#c1f7bb")
 
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\nirma.png"
    global _img0
    _img0 = PhotoImage(file=photo_location)
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#d6b8fa",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img0,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=500, width=1300)

    Button2 = Button(project,command=logins,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Student Login''')
    Button2.place(relx=0.617, rely=0.489, height=40, width=127)
 
    Button3 = Button(project,command=registerf,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Register Faculty''')
    Button3.place(relx=0.367, rely=0.622, height=40, width=121)
 
    Button4 = Button(project,command=destroy1,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Exit''')
    Button4.place(relx=0.5, rely=0.778, height=40, width=127)
 
    Button5 = Button(project,command=loginf,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Faculty Login''')
    Button5.place(relx=0.367, rely=0.489, height=40, width=117)
 
    Button6 = Button(project,command=registers,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Register Student''')
    Button6.place(relx=0.617, rely=0.622, height=40, width=127)
    project.mainloop()
    
def mainscreen1():
    reg.destroy()
    global project
    project=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
 
    project.geometry("1100x500")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Main")
    project.configure(background="#c1f7bb")
 
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\nirma.png"
    global _img0
    _img0 = PhotoImage(file=photo_location)
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#d6b8fa",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img0,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=500, width=1300)

    Button2 = Button(project,command=logins,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Student Login''')
    Button2.place(relx=0.617, rely=0.489, height=40, width=127)
 
    Button3 = Button(project,command=registerf,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Register Faculty''')
    Button3.place(relx=0.367, rely=0.622, height=40, width=121)
 
    Button4 = Button(project,command=destroy1,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Exit''')
    Button4.place(relx=0.5, rely=0.778, height=40, width=127)
 
    Button5 = Button(project,command=loginf,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Faculty Login''')
    Button5.place(relx=0.367, rely=0.489, height=40, width=117)
 
    Button6 = Button(project,command=registers,activebackground="#ececec",activeforeground="#000000",background="#f4e7bd",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Register Student''')
    Button6.place(relx=0.617, rely=0.622, height=40, width=127)
    project.mainloop()
    
def destroy1():
    project.destroy()
    
def logout():
    top.destroy()
    mainscreen()
    
def main1():
    global project
    project = Tk()
mainscreen()
