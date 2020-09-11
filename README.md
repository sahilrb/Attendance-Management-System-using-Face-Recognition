# Python-Project

# Face Recognition Based Attendance System
A Face recognition based Attendance Management project based on python which can mark attendance of those students which are in current camera 
frame and already present in our database. This project uses many python libraries. An sample of images of newly added student is taken and 
by using opencv and some concept of deep learning dataset is trained and when taking attendance system detects indivuals in the video frame. 
Database is updated to mark attendance to students preset. Anyone can check their attendance.

# Requirements
Python 3

OpenCV2

Numpy

Mysql

imutils

scikit-learn

Pickle

Tkinter

# How to run
Download all the files

Make your database as shown in attendance(1).sql file and connect it with python code as shown in MainFile.py

Set path for gui images in MainFile.py as where you put it in your pc

Make one folder names images in which sample of newly added student will be stored

Put all files in one folder only

First run MainFile.py file

First register yourself and then login(as student or as faculty).

If you register as student you have to add courses in which you enrolled. 

If you want to add new student click on add student button(login with faculty id necessary).
Add name and unique roll_no of new student
Press take samples button, this will open your camera and take samples new student

After taking samples you have to train dataset, for that click Train data button, this will take 2-3 minutes(Training data is necessary whenever new student is added)(login with faculty id necessary).

To take attendance click on take attendance button, In opened window add course code for which course you want to take attendance, and press(login with faculty id necessary)
take attendance button, this will open camera and take attendance of those student which are in camera frame and already present in database
Press enter to close camera

To check attendance click on check attendance button, here you can check your attendance roll_no wise and course wise

Here you can also add or delete attendance manually with constrains.(login with faculty id necessary)

Use back button to go to previous window

Note: In some version of python and in some ides, that ide can't release camera so that if you add new student or take another attendance
without rerunning the python file. It may cause some issues in that case you have to rerun the python file.(This issue is completely version
specific and depends on your ide so you may or may not face issue, we can't do anything about it). 

