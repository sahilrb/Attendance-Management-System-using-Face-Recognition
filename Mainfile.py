from imutils import paths
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import cv2
import numpy as np
import pickle
import imutils
from tkinter import *
import tkinter.ttk
import os
from datetime import datetime
import mysql.connector
import collect
import train
from tkinter import messagebox
from datetime import date

def register():
    project.destroy()
    global reg
    reg = Tk()
    reg.configure(background="#c0fab8")
    reg.title("Register")
    reg.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(reg, text="Please enter details below", bg="blue").pack()
    Label(reg, text="").pack()
    username_lable = Label(reg, text="Username * ")
    username_lable.pack()
    username_entry = Entry(reg, textvariable=username)
    username_entry.pack()
    password_lable = Label(reg, text="Password * ")
    password_lable.pack()
    password_entry = Entry(reg, textvariable=password, show='*')
    password_entry.pack()
    Label(reg, text="").pack()
    Button(reg, text="Register", width=10, height=1, bg="#fdb5c4", command = register_user).pack()
    
def register_user():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance")
    cursor = db.cursor()
    username_info = username.get()
    password_info = password.get()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    '''file = open(username_info,"w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()'''
    try:
        cursor.execute("""INSERT INTO signup(user_name,password) VALUES("{}", "{}")""".format(username_info, password_info))
        db.commit()
        Label(reg, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        login1()
    except:
        used()
        
    #cursor.execute("""INSERT INTO signup(user_name,password) VALUES("{}", "{}")""".format(username_info, password_info))
    #db.commit()
    #db.close()
    
def used():
    reg.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="Username Taken!!! Try With anotherone").pack()
    Label(text="").pack()
    Button(project, text="Register", bg="#fdb5c4",command=register).pack()

def login1():
    reg.destroy()
    global log
    log = Tk()
    log.configure(background="#c0fab8")
    log.title("Login")
    log.geometry("300x250")
    Label(log, text="Please enter details below to login").pack()
    Label(log, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(log, text="Username * ").pack()
    username_login_entry = Entry(log, textvariable=username_verify)
    username_login_entry.pack()
    Label(log, text="").pack()
    Label(log, text="Password * ").pack()
    password_login_entry = Entry(log, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(log, text="").pack()
    Button(log, text="Login", width=10, height=1,bg="#fdb5c4", command = login_verify).pack()
    
def login():
    project.destroy()
    global log
    log = Tk()
    log.configure(background="#c0fab8")
    log.title("Login")
    log.geometry("300x250")
    Label(log, text="Please enter details below to login").pack()
    Label(log, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(log, text="Username * ").pack()
    username_login_entry = Entry(log, textvariable=username_verify)
    username_login_entry.pack()
    Label(log, text="").pack()
    Label(log, text="Password * ").pack()
    password_login_entry = Entry(log, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(log, text="").pack()
    Button(log, text="Login", width=10, height=1,bg="#fdb5c4", command = login_verify).pack()
    
def login_verify():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance")
    cursor = db.cursor()
    global username1
    username1 = username_verify.get()
    global password1
    password1 = password_verify.get()

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    cursor.execute("(SELECT * FROM signup WHERE user_name LIKE %s)", (username1,))
    flag1=0
    for i in cursor:
        if username1 in list(i):
            cursor.execute("(SELECT * FROM signup WHERE user_name LIKE %s)", (username1,))
            for j in cursor:
                if password1 in list(j):
                    login_sucess()
                    flag1 = 1
                    break
                else:
                    password_not_recognised()
                    flag1 = 1
    if flag1 == 0:
        user_not_found()
        
    

    '''list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()
'''

def take():
    try:
        new_student=roll.get()
        name1=name.get()
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="attendance")
        cursor = db.cursor()
        cursor.execute("""insert into student(roll_no,name) values("{}","{}")""".format(new_student,name1))
        db.commit()
        collect.take(new_student)
        messagebox.showinfo('Adding new student','Student added successfully')
    except:
        messagebox.showinfo('Student already exist','Student already exist')
        project.destroy()
        new1()
        
    
def login_sucess():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Success")
    project.geometry("150x100")
    Label(project, text="Login Success").pack()
    Label(text="").pack()
    Button(project, text="Go to main window",bg="#fdb5c4", command=att).pack()
    
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
    
            
    Button3 = Button(project,command=att,activebackground="#ececec",activeforeground="#000000",background="#fbc6b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
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
    
            
    Button3 = Button(project,command=att,activebackground="#ececec",activeforeground="#000000",background="#fbc6b7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
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
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance")
    cursor = db.cursor()

    for roll_no in dic:
        if(dic[roll_no]>=100):
            present.append(roll_no)
    code1=code.get()        
    if "unknown" in present: 
        present.remove("unknown")    
    time = str(date.today())
    for i in present:
        cursor.execute("""insert into faculty(roll_no,course,date) values("{}","{}","{}")""".format(i, code1 , time))
        db.commit()
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
    Label1.place(relx=0.2, rely=0.622, height=31, width=130)
    
    global code
    code = StringVar()
    Entry1 = Entry(project,textvariable=code,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry1.place(relx=0.433, rely=0.622,height=30, relwidth=0.29)
    Entry1.delete(0, END)
   
    Button2 = Button(project,command=took1,activebackground="#ececec",activeforeground="#000000",background="#fcb6ce",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Take Attandance''')
    Button2.place(relx=0.233, rely=0.756, height=24, width=120)
        
    Button3 = Button(project,command=att,activebackground="#ececec",activeforeground="#000000",background="#fcb6ce",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button3.place(relx=0.467, rely=0.756, height=24, width=76)
    project.mainloop()
    
def show2():
    project.destroy()
    global top
    top=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    
    top.geometry("1345x637+-1+36")
    top.minsize(120, 1)
    top.maxsize(1362, 741)
    top.resizable(1, 1)
    top.title("New Toplevel")
    top.configure(background="#d9d9d9")
    
    Listbox1 = Listbox(top)
    Listbox1.place(relx=-0.001, rely=0.0, relheight=0.961, relwidth=1.001)
    Listbox1.configure(background="white")
    Listbox1.configure(disabledforeground="#a3a3a3")
    Listbox1.configure(font="TkFixedFont")
    Listbox1.configure(foreground="#000000")
            
    Listbox1.delete(0,END)
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance")
    cursor = db.cursor()
    roll10=code1.get()
    cursor.execute("create table faculty_new as select * from faculty where course like %s", (roll10,))
    cursor.execute("select roll_no,date,count(*) from faculty_new group by roll_no")
    Listbox1.insert(END,"Name")
    Listbox1.insert(END,"1)roll_no      2)Date        3)Total attendance in this course")
    Listbox1.insert(END," ")
    Listbox1.insert(END," ")
    a=cursor.fetchall()
    for i in a:
        cursor.execute("select name from student where roll_no like %s", (i[0],))
        b=cursor.fetchall()
        for j in b:
            Listbox1.insert(END,j)
        Listbox1.insert(END,i)
        Listbox1.insert(END," ")
    cursor.execute("DROP TABLE faculty_new")
    db.commit()
    Button1 = Button(top,command=show,activebackground="#ececec",activeforeground="#000000",background="#fcc8b6",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button1.place(relx=0.483, rely=0.958, height=24, width=86)
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
    
    top.geometry("1345x637+-1+36")
    top.minsize(120, 1)
    top.maxsize(1362, 741)
    top.resizable(1, 1)
    top.title("New Toplevel")
    top.configure(background="#d9d9d9")
    
    Listbox1 = Listbox(top)
    Listbox1.place(relx=-0.001, rely=0.0, relheight=0.961, relwidth=1.001)
    Listbox1.configure(background="white")
    Listbox1.configure(disabledforeground="#a3a3a3")
    Listbox1.configure(font="TkFixedFont")
    Listbox1.configure(foreground="#000000")
    Listbox1.delete(0,END)
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance")
    cursor = db.cursor()
    roll10=roll1.get()
    Listbox1.insert(END,"1)Course          2)Date          3)Total attendance in this course")
    Listbox1.insert(END," ")
    Listbox1.insert(END," ")
    cursor.execute("select name from student where roll_no like %s", (roll10,))
    b=cursor.fetchall()
    Listbox1.insert(END,"Name")
    Listbox1.insert(END,b)
    Listbox1.insert(END," ")
    Listbox1.insert(END,"Attendance")
    cursor.execute("create table faculty_new as select * from faculty where roll_no like %s",(roll10,))
    cursor.execute("select course,date,count(*) from faculty_new group by course")
    a=cursor.fetchall()
    for i in a:
        Listbox1.insert(END,i)
    cursor.execute("DROP TABLE faculty_new")
    db.commit()
    Button1 = Button(top,command=show,activebackground="#ececec",activeforeground="#000000",background="#fcc8b6",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button1.place(relx=0.483, rely=0.958, height=24, width=86)
    top.mainloop()
    
def show():    
    top.destroy()
    global project
    project=Tk()
    
    
    _bgcolor = '#c0fab8'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#c0fab8' # X11 color: 'gray85'
    _ana1color = '#c0fab8' # X11 color: 'gray85'
    _ana2color = '#c0fab8' # Closest X11 color: 'gray92'
    
    project.geometry("1351x658+0+306")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Attandance")
    project.configure(background="#c4f8ba")
    
    
    global roll1
    global code1
    roll1 = StringVar()
    code1 = StringVar()
    
    Entry1 = Entry(project,textvariable=roll1,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry1.place(relx=0.111, rely=0.25,height=30, relwidth=0.114)
    Entry1.delete(0, END)
    
    
    Entry2 = Entry(project,textvariable=code1,background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")
    Entry2.place(relx=0.681, rely=0.25,height=30, relwidth=0.114)
    Entry2.delete(0, END)
    
    
    
    
    photo_location = "C:\\Users\\SHIVAM\\Desktop\\check.png"
    global _img0
    _img0 = PhotoImage(file=photo_location)
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#c4f8ba",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img0,pady="0",text='''Button''')
    Button1.place(relx=-0.008, rely=0.0, height=160, width=1347)
    

    Label1 = Label(project,background="#feb4c7",disabledforeground="#a3a3a3",foreground="#000000",text='''Enter Roll No''')
    Label1.place(relx=0.022, rely=0.25, height=33, width=104)
   
    Label2 = Label(project,background="#feb4c7",disabledforeground="#a3a3a3",foreground="#000000",text='''Course Code''')
    Label2.place(relx=0.592, rely=0.25, height=30, width=102)
    
    Button2 = Button(project,command=show1,activebackground="#ececec",activeforeground="#000000",background="#eac8e3",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Show''')
    Button2.place(relx=0.244, rely=0.25, height=31, width=97)
   
    Button3 = Button(project,command=show2,activebackground="#ececec",activeforeground="#000000",background="#eac8e3",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Show''')
    Button3.place(relx=0.814, rely=0.25, height=31, width=97)
                
    Button4 = Button(project,command=att,activebackground="#ececec",activeforeground="#000000",background="#b6b66b",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''')
    Button4.place(relx=0.466, rely=0.951, height=31, width=97)
    project.mainloop()
    
def att():
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
    
def password_not_recognised():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="Invalid Password!!!").pack()
    Label(text="").pack()
    Button(project, text="Try again",bg="#fdb5c4", command=login).pack()
    
def user_not_found():
    log.destroy()
    global project
    project = Tk()
    project.configure(background="#c0fab8")
    project.title("Oops...")
    project.geometry("300x250")
    Label(project, text="User Not Found").pack()
    Label(text="").pack()
    Button(project, text="Register", bg="#fdb5c4",command=register).pack()
    
def mainscreen():
    global project
    project=Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
    project.geometry("600x450+351+151")
    project.minsize(120, 1)
    project.maxsize(1362, 741)
    project.resizable(1, 1)
    project.title("Login")
    project.configure(background="#fdb5c4")

    photo_location = "C:\\Users\\SHIVAM\\Desktop\\login.png"
    global _img0
    _img0 = PhotoImage(file=photo_location)
    Button1 = Button(project,activebackground="#ececec",activeforeground="#000000",background="#c0fab8",borderwidth="0",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",image=_img0,pady="0",text='''Button''')
    Button1.place(relx=0.0, rely=0.0, height=224, width=606)
    
    Button2 = Button(project,command=register,activebackground="#ececec",activeforeground="#000000",background="#ffff00",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Register''')
    Button2.place(relx=0.517, rely=0.6, height=34, width=123)
   
    Button3 = Button(project,command=destroy1,activebackground="#ececec",activeforeground="#000000",background="#bbc9f7",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Exit''')
    Button3.place(relx=0.417, rely=0.733, height=24, width=79)
   
    Button4 = Button(project,command = login,activebackground="#ececec",activeforeground="#000000",background="#ffff00",disabledforeground="#a3a3a3",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Login''')
    Button4.place(relx=0.25, rely=0.6, height=34, width=121)
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