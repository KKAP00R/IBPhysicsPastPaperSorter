#IMPORTING NECESSARY LIBRARIES
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import Tk
from array import *
import os
import time
import PyPDF2
import tkinter.font as tkFont
from tkinter import ttk
from ttkthemes import themed_tk as theme

#DEFINING IMPORTANT FUNCTIONS WHICH THE BUTTONS WOULD PERFORM
def browsefn():
    global file_name
    window1.destroy()
    file_name = filedialog.askopenfilename(initialdir = "/", title = "SELECT A FILE", filetypes = (("PDF","*.pdf*"), ("ALL FILES", "*.*")))
    print(file_name)
    global window2
    window2 = tk.Tk()
    window2.title("USER INPUTS NEEDED")
    window2.geometry("500x200")
    Label(window2, text='Enter the Type of Paper (1 for SL and 2 for HL)').grid(row=0) 
    Label(window2, text = 'Year of this Paper').grid(row = 1)
    Label(window2, text = "NUMBER OF QUESTIONS").grid(row = 2)
    Label(window2, text = "ENTER 1 for May and 2 for Nov. version").grid(row = 3)
    Label(window2, text = "ENTER 1 for Timezone 1 and 2 for Timezone 2").grid(row = 4)
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    entry1 = Entry(window2) 
    entry2 = Entry(window2)
    entry3 = Entry(window2)
    entry4 = Entry(window2)
    entry5 = Entry(window2)
    entry1.grid(row = 0, column = 1) 
    entry2.grid(row = 1, column = 1)
    entry3.grid(row = 2, column = 1)
    entry4.grid(row = 3, column = 1)
    entry5.grid(row = 4, column = 1)
    done = Button(window2, text = "SAVE", width = 20, command = savefn)
    done.grid(row = 5, column = 1)
    exitbutton = Button(window2, text = "EXIT", width = 20, command = window2.destroy)
    exitbutton.grid(row = 6, column = 1)
    window2.mainloop()
#CHECKED ABOVE - BROWSEFN HAS NO ISSUES.
def savefn():
    global s1
    global s2
    global s3
    global s4
    global s5
    s1 = entry1.get()
    s2 = entry2.get()
    s3 = entry3.get()
    s4 = entry4.get()
    s5 = entry5.get()
    print(s1)
    print(s2)
    if s3 == '8':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn8()
    elif s3== '9':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn9()
    elif s3 == '10':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn10()
    elif s3 == '11':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn11()
    elif s3 == '12':
        if s4 == '2':
            s2 = int(s2) + 15
            s2 = str(s2)
        if s5 == '2':
            s2 = int(s2) + 30
            s2 = str(s2)
        fn12()
    else:
        print("ERROR IN PAPER TYPE")
#CHECKED ABOVE - SAVEFN HAS NO ISSUES.
def fn12():
    global window3
    j = 12
    i = 1
    window3 = tk.Tk()
    window3.title("USER INPUTS FOR MCQ")
    window3.geometry("800x600")
    while i<=j:
        Label(window3, text = "ENTER TOPIC OF Q" + str(i) + " ----->").grid(row = +i, column = 0)
        Label(window3, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION ----->").grid(row = +i, column = 2)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global e12
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    global p12
    e1 = Entry(window3)
    e1.grid(row = 1, column = 1)
    e2 = Entry(window3)
    e2.grid(row = 2, column = 1)
    e3 = Entry(window3)
    e3.grid(row = 3, column = 1)
    e4 = Entry(window3)
    e4.grid(row = 4, column = 1)
    e5 = Entry(window3)
    e5.grid(row = 5, column = 1)
    e6 = Entry(window3)
    e6.grid(row = 6, column = 1)
    e7 = Entry(window3)
    e7.grid(row = 7, column = 1)
    e8 = Entry(window3)
    e8.grid(row = 8, column = 1)
    e9 = Entry(window3)
    e9.grid(row = 9, column = 1)
    e10 = Entry(window3)
    e10.grid(row = 10, column = 1)
    e11 = Entry(window3)
    e11.grid(row = 11, column = 1)
    e12 = Entry(window3)
    e12.grid(row = 12, column = 1)
    p1 = Entry(window3)
    p1.grid(row = 1, column = 3)
    p2 = Entry(window3)
    p2.grid(row = 2, column = 3)
    p3 = Entry(window3)
    p3.grid(row = 3, column = 3)
    p4 = Entry(window3)
    p4.grid(row = 4, column = 3)
    p5 = Entry(window3)
    p5.grid(row = 5, column = 3)
    p6 = Entry(window3)
    p6.grid(row = 6, column = 3)
    p7 = Entry(window3)
    p7.grid(row = 7, column = 3)
    p8 = Entry(window3)
    p8.grid(row = 8, column = 3)
    p9 = Entry(window3)
    p9.grid(row = 9, column = 3)
    p10 = Entry(window3)
    p10.grid(row = 10, column = 3)
    p11 = Entry(window3)
    p11.grid(row = 11, column = 3)
    p12 = Entry(window3)
    p12.grid(row = 12, column = 3)
    save = Button(window3, text = "SAVE + QUIT", width = 20, command = savedata12)  
    save.grid(row = 13, column = 1)
    Label(window3, text = "Note: 1. When entering multiple topics").grid(row = 14, column = 0) 
    Label(window3, text = "seperate both with a double space").grid(row = 15, column = 0)
    Label(window3, text = "2. When entering the PDF beginning page").grid(row = 16, column = 0)
    Label(window3, text = "Enter the page at the top, but subtract 1 from it").grid(row = 17, column = 0)
    Label(window3, text = "So, if the page number at top is 2").grid(row = 18, column = 0) 
    Label(window3, text = "enter the beginning page as 1").grid(row = 19, column = 0)
#FN12 HAS NO ISSUES
def fn11():
    global window3
    j = 11
    i = 1
    window3 = tk.Tk()
    window3.title("USER INPUTS FOR MCQ")
    window3.geometry("800x600")
    while i<=j:
        Label(window3, text = "ENTER TOPIC OF Q" + str(i) + " ----->").grid(row = +i, column = 0)
        Label(window3, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION ----->").grid(row = +i, column = 2)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    e1 = Entry(window3)
    e1.grid(row = 1, column = 1)
    e2 = Entry(window3)
    e2.grid(row = 2, column = 1)
    e3 = Entry(window3)
    e3.grid(row = 3, column = 1)
    e4 = Entry(window3)
    e4.grid(row = 4, column = 1)
    e5 = Entry(window3)
    e5.grid(row = 5, column = 1)
    e6 = Entry(window3)
    e6.grid(row = 6, column = 1)
    e7 = Entry(window3)
    e7.grid(row = 7, column = 1)
    e8 = Entry(window3)
    e8.grid(row = 8, column = 1)
    e9 = Entry(window3)
    e9.grid(row = 9, column = 1)
    e10 = Entry(window3)
    e10.grid(row = 10, column = 1)
    e11 = Entry(window3)
    e11.grid(row = 11, column = 1)
    p1 = Entry(window3)
    p1.grid(row = 1, column = 3)
    p2 = Entry(window3)
    p2.grid(row = 2, column = 3)
    p3 = Entry(window3)
    p3.grid(row = 3, column = 3)
    p4 = Entry(window3)
    p4.grid(row = 4, column = 3)
    p5 = Entry(window3)
    p5.grid(row = 5, column = 3)
    p6 = Entry(window3)
    p6.grid(row = 6, column = 3)
    p7 = Entry(window3)
    p7.grid(row = 7, column = 3)
    p8 = Entry(window3)
    p8.grid(row = 8, column = 3)
    p9 = Entry(window3)
    p9.grid(row = 9, column = 3)
    p10 = Entry(window3)
    p10.grid(row = 10, column = 3)
    p11 = Entry(window3)
    p11.grid(row = 11, column = 3)
    save = Button(window3, text = "SAVE + QUIT", width = 20, command = savedata11)  
    save.grid(row = 12, column = 1)
    Label(window3, text = "Note: 1. When entering multiple topics").grid(row = 13, column = 0) 
    Label(window3, text = "seperate both with a space").grid(row = 14, column = 0)
    Label(window3, text = "2. When entering the PDF baginning page").grid(row = 15, column = 0)
    Label(window3, text = "Enter the page at the top, but subtract 1 from it").grid(row = 16, column = 0)
    Label(window3, text = "So, if the page number at top is 2").grid(row = 17, column = 0) 
    Label(window3, text = "enter the beginning page as 1").grid(row = 18, column = 0)
#FN11 HAS NO ISSUES
def fn10():
    global window3
    j = 10
    i = 1
    window3 = tk.Tk()
    window3.title("USER INPUTS FOR MCQ")
    window3.geometry("800x600")
    while i<=j:
        Label(window3, text = "ENTER TOPIC OF Q" + str(i) + " ----->").grid(row = +i, column = 0)
        Label(window3, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION ----->").grid(row = +i, column = 2)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    e1 = Entry(window3)
    e1.grid(row = 1, column = 1)
    e2 = Entry(window3)
    e2.grid(row = 2, column = 1)
    e3 = Entry(window3)
    e3.grid(row = 3, column = 1)
    e4 = Entry(window3)
    e4.grid(row = 4, column = 1)
    e5 = Entry(window3)
    e5.grid(row = 5, column = 1)
    e6 = Entry(window3)
    e6.grid(row = 6, column = 1)
    e7 = Entry(window3)
    e7.grid(row = 7, column = 1)
    e8 = Entry(window3)
    e8.grid(row = 8, column = 1)
    e9 = Entry(window3)
    e9.grid(row = 9, column = 1)
    e10 = Entry(window3)
    e10.grid(row = 10, column = 1)
    p1 = Entry(window3)
    p1.grid(row = 1, column = 3)
    p2 = Entry(window3)
    p2.grid(row = 2, column = 3)
    p3 = Entry(window3)
    p3.grid(row = 3, column = 3)
    p4 = Entry(window3)
    p4.grid(row = 4, column = 3)
    p5 = Entry(window3)
    p5.grid(row = 5, column = 3)
    p6 = Entry(window3)
    p6.grid(row = 6, column = 3)
    p7 = Entry(window3)
    p7.grid(row = 7, column = 3)
    p8 = Entry(window3)
    p8.grid(row = 8, column = 3)
    p9 = Entry(window3)
    p9.grid(row = 9, column = 3)
    p10 = Entry(window3)
    p10.grid(row = 10, column = 3)
    save = Button(window3, text = "SAVE + QUIT", width = 20, command = savedata10)  
    save.grid(row = 11, column = 1)
    Label(window3, text = "Note: 1. When entering multiple topics").grid(row = 12, column = 0) 
    Label(window3, text = "seperate both with a space").grid(row = 13, column = 0)
    Label(window3, text = "2. When entering the PDF baginning page").grid(row = 14, column = 0)
    Label(window3, text = "Enter the page at the top, but subtract 1 from it").grid(row = 15, column = 0)
    Label(window3, text = "So, if the page number at top is 2").grid(row = 16, column = 0) 
    Label(window3, text = "enter the beginning page as 1").grid(row = 17, column = 0)
#FN10 HAS NO ISSUES
def fn9():
    global window3
    j = 9
    i = 1
    window3 = tk.Tk()
    window3.title("USER INPUTS FOR MCQ")
    window3.geometry("800x600")
    while i<=j:
        Label(window3, text = "ENTER TOPIC OF QUESTION" + str(i) + " ----->").grid(row = +i, column = 0)
        Label(window3, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION ----->").grid(row = +i, column = 2)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    e1 = Entry(window3)
    e1.grid(row = 1, column = 1)
    e2 = Entry(window3)
    e2.grid(row = 2, column = 1)
    e3 = Entry(window3)
    e3.grid(row = 3, column = 1)
    e4 = Entry(window3)
    e4.grid(row = 4, column = 1)
    e5 = Entry(window3)
    e5.grid(row = 5, column = 1)
    e6 = Entry(window3)
    e6.grid(row = 6, column = 1)
    e7 = Entry(window3)
    e7.grid(row = 7, column = 1)
    e8 = Entry(window3)
    e8.grid(row = 8, column = 1)
    e9 = Entry(window3)
    e9.grid(row = 9, column = 1)
    p1 = Entry(window3)
    p1.grid(row = 1, column = 3)
    p2 = Entry(window3)
    p2.grid(row = 2, column = 3)
    p3 = Entry(window3)
    p3.grid(row = 3, column = 3)
    p4 = Entry(window3)
    p4.grid(row = 4, column = 3)
    p5 = Entry(window3)
    p5.grid(row = 5, column = 3)
    p6 = Entry(window3)
    p6.grid(row = 6, column = 3)
    p7 = Entry(window3)
    p7.grid(row = 7, column = 3)
    p8 = Entry(window3)
    p8.grid(row = 8, column = 3)
    p9 = Entry(window3)
    p9.grid(row = 9, column = 3)
    save = Button(window3, text = "SAVE + QUIT", width = 20, command = savedata9)  
    save.grid(row = 10, column = 1)
    Label(window3, text = "Note: 1. When entering multiple topics").grid(row = 11, column = 0) 
    Label(window3, text = "seperate both with a space").grid(row = 12, column = 0)
    Label(window3, text = "2. When entering the PDF baginning page").grid(row = 13, column = 0)
    Label(window3, text = "Enter the page at the top, but subtract 1 from it").grid(row = 14, column = 0)
    Label(window3, text = "So, if the page number at top is 2").grid(row = 15, column = 0) 
    Label(window3, text = "enter the beginning page as 1").grid(row = 16, column = 0)
#FN9 HAS NO ISSUES
def fn8():
    global window3
    j = 8
    i = 1
    window3 = tk.Tk()
    window3.title("USER INPUTS FOR MCQ")
    window3.geometry("800x600")
    while i<=j:
        Label(window3, text = "ENTER TOPIC OF Q" + str(i) + " ----->").grid(row = +i, column = 0)
        Label(window3, text = "ENTER PAGE OF THE BEGINNING OF THE QUESTION ----->").grid(row = +i, column = 2)
        i+=1
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    e1 = Entry(window3)
    e1.grid(row = 1, column = 1)
    e2 = Entry(window3)
    e2.grid(row = 2, column = 1)
    e3 = Entry(window3)
    e3.grid(row = 3, column = 1)
    e4 = Entry(window3)
    e4.grid(row = 4, column = 1)
    e5 = Entry(window3)
    e5.grid(row = 5, column = 1)
    e6 = Entry(window3)
    e6.grid(row = 6, column = 1)
    e7 = Entry(window3)
    e7.grid(row = 7, column = 1)
    e8 = Entry(window3)
    e8.grid(row = 8, column = 1)
    p1 = Entry(window3)
    p1.grid(row = 1, column = 3)
    p2 = Entry(window3)
    p2.grid(row = 2, column = 3)
    p3 = Entry(window3)
    p3.grid(row = 3, column = 3)
    p4 = Entry(window3)
    p4.grid(row = 4, column = 3)
    p5 = Entry(window3)
    p5.grid(row = 5, column = 3)
    p6 = Entry(window3)
    p6.grid(row = 6, column = 3)
    p7 = Entry(window3)
    p7.grid(row = 7, column = 3)
    p8 = Entry(window3)
    p8.grid(row = 8, column = 3)
    save = Button(window3, text = "SAVE + QUIT", width = 20, command = savedata8)  
    save.grid(row = 9, column = 1)
    Label(window3, text = "Note: 1. When entering multiple topics").grid(row = 10, column = 0) 
    Label(window3, text = "seperate both with a double space").grid(row = 11, column = 0)
    Label(window3, text = "2. When entering the PDF beginning page").grid(row = 12, column = 0)
    Label(window3, text = "Enter the page at the top, but subtract 1 from it").grid(row = 13, column = 0)
    Label(window3, text = "So, if the page number at top is 2").grid(row = 14, column = 0) 
    Label(window3, text = "enter the beginning page as 1").grid(row = 15, column = 0)
#FN8 HAS NO ISSUES
def savedata11():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    string9 = e9.get()
    string10 = e10.get()
    string11 = e11.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    if string9 == '1':
        string9 = '1 '
    if string10 == '1':
        string10 = '1 '
    if string11 == '1':
        string11 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    page9 = p9.get()
    page10 = p10.get()
    page11 = p11.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("9.  " + string9 + "\n")
    f.write(" 9P. " + page9 + "\n")
    f.write("10.  " + string10 + "\n")
    f.write(" 10P. " + page10 + "\n")
    f.write("11.  " + string11 + "\n")
    f.write(" 11P. " + page11 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
    window3.destroy()
#CHECKED - SAVEDATA11 HAS NO ISSUES
def savedata8():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
#CHECKED - SAVEDATA8 HAS NO ISSUES
def savedata12():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    string9 = e9.get()
    string10 = e10.get()
    string11 = e11.get()
    string12 = e12.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    if string9 == '1':
        string9 = '1 '
    if string10 == '1':
        string10 = '1 '
    if string11 == '1':
        string11 = '1 '
    if string12 == '1':
        string12 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    page9 = p9.get()
    page10 = p10.get()
    page11 = p11.get()
    page12 = p12.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("9.  " + string9 + "\n")
    f.write(" 9P. " + page9 + "\n")
    f.write("10.  " + string10 + "\n")
    f.write(" 10P. " + page10 + "\n")
    f.write("11.  " + string11 + "\n")
    f.write(" 11P. " + page11 + "\n")
    f.write("12.  " + string12 + "\n")
    f.write(" 12P. " + page12 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
def savedata10():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    string9 = e9.get()
    string10 = e10.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    if string9 == '1':
        string9 = '1 '
    if string10 == '1':
        string10 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    page9 = p9.get()
    page10 = p10.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("9.  " + string9 + "\n")
    f.write(" 9P. " + page9 + "\n")
    f.write("10.  " + string10 + "\n")
    f.write(" 10P. " + page10 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
    window3.destroy()
#CHECKED SAVEDATA10 HAS NO ISSUES
def savedata9():
    string1 = e1.get()
    string2 = e2.get()
    string3 = e3.get()
    string4 = e4.get()
    string5 = e5.get()
    string6 = e6.get()
    string7 = e7.get()
    string8 = e8.get()
    string9 = e9.get()
    if string1 == '1':
        string1 = '1 '
    if string2 == '1':
        string2 = '1 '
    if string3 == '1':
        string3 = '1 '
    if string4 == '1':
        string4 = '1 '
    if string5 == '1':
        string5 = '1 '
    if string6 == '1':
        string6 = '1 '
    if string7 == '1':
        string7 = '1 '
    if string8 == '1':
        string8 = '1 '
    if string9 == '1':
        string9 = '1 '
    page1 = p1.get()
    page2 = p2.get()
    page3 = p3.get()
    page4 = p4.get()
    page5 = p5.get()
    page6 = p6.get()
    page7 = p7.get()
    page8 = p8.get()
    page9 = p9.get()
    path = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(s1)
    name = os.path.join(path, s2 + ".txt")
    f = open(name, "w+")
    f.write("1.  " + string1 + "\n")
    f.write(" 1P. " + page1 + "\n")
    f.write("2.  " + string2 + "\n")
    f.write(" 2P. " + page2 + "\n")
    f.write("3.  " + string3 + "\n")
    f.write(" 3P. " + page3 + "\n")
    f.write("4.  " + string4 + "\n")
    f.write(" 4P. " + page4 + "\n")
    f.write("5.  " + string5 + "\n")
    f.write(" 5P. " + page5 + "\n")
    f.write("6.  " + string6 + "\n")
    f.write(" 6P. " + page6 + "\n")
    f.write("7.  " + string7 + "\n")
    f.write(" 7P. " + page7 + "\n")
    f.write("8.  " + string8 + "\n")
    f.write(" 8P. " + page8 + "\n")
    f.write("9.  " + string9 + "\n")
    f.write(" 9P. " + page9 + "\n")
    f.write("path:" + file_name + "\n")
    f.write("total:" + str(s3))
    window3.destroy()
#CHECKED SAVEDATA9 HAS NO ISSUES
def choice():
    global window5
    window5 = tk.Tk()
    window5.title("USER CHOICE")
    window5.geometry("500x300")
    Label(window5, text = "ENTER THE TOPIC YOU WANT QUESTIONS FROM").grid(row = 0)
    Label(window5, text = "ENTER 1 for SL and 2 for HL").grid(row = 1)
    Label(window5, text = "IF ENTERING 2 TOPICS FOR SEARCH, DOUBLE SPACE BETWEEN THEM").grid(row = 3)
    global input1
    global input2
    input1 = Entry(window5)
    input2 = Entry(window5)
    input1.grid(row = 0, column = 1)
    input2.grid(row = 1, column = 1)
    next1 = Button(window5, text = "SEARCH", width = 20, command = choiceprocess1)
    next1.grid(row = 2, column = 1)
    window5.mainloop()
def choiceprocess1():
    global choice1
    global choice2
    choice1 = input1.get()
    choice2 = input2.get()
    print(choice1)
    print(choice2)
    choiceprocess2()
    window5.destroy()
def choiceprocess2():
    if choice2 == '1':
        global path_file1
        path_file1 = "C:/Users/Ajit/Desktop/PROGRAMS/1"
        presortfunction1()
    elif choice2 == '2':
        global path_file2
        path_file2 = "C:/Users/Ajit/Desktop/PROGRAMS/2"
        presortfunction1()
def presortfunction1():
    path_file2 = "C:/Users/Ajit/Desktop/PROGRAMS/" + str(choice2)
    global arr
    global z1
    global reqcon
    global recqon
    global retcon
    global k
    global name_full
    global a
    global b
    global d
    global l
    global finalarr
    global totalquestions
    d = []
    b = []
    a = []
    arr = []
    finalarr =[]
    l = -1
    k = 10
    if choice1 == '1':
        choice = " " + choice1 + " "
    else:
        choice = "  " + choice1
    while k<=80:
        name_file = "20" + str(k)
        name_full = os.path.join(path_file2, name_file + ".txt")
        x = os.path.isfile(name_full)
        k+=1
        if x == True:
            arr.append(name_file)
            y = open(name_full, 'r')
            content = y.readlines()
            for con in content:
                sel = con.find("  ")
                sel2 = sel-3
                if con[sel2] != "P":
                    if choice in con:
                        sel3 = con.find('.')
                        reqcon = con[0:sel3]
                        arr.append(reqcon)
                        recqon = int(reqcon) + 1
                        retcon = recqon + 1
                        totaldetection()
                        l+=1
                        presortfunction2()
                        presortfunction4()
                        presortfunction3()
                        
        elif x == False:
            print("FILE NOT FOUND " + name_file)
    print(arr)
    print("THIS IS"  + str(a))
    print("THIS IS " + str(b))
    searchfn()
    print("THIS IS: " + str(c))
    print(len(arr))
    print(d)
    fileremover()
def totaldetection():
    global totalquestions
    searterm = "total:"
    k2 = open(name_full, 'r')
    linecon = k2.readlines()
    for line in linecon:
        findit = line.find(str(searterm))
        if findit != -1:
            ind = line.index(":")
            k3 = len(line)
            totalquestions = line[(ind+1):(k3)]
            totalquestions = int(totalquestions)
            print(totalquestions)
def presortfunction2():
    term_search = " " + str(reqcon) + "P"
    y2 = open(name_full, 'r')
    linecon = y2.readlines()
    for line in linecon:
        findit = line.find(str(term_search))
        if findit != -1:
            sel4 = line.index('.')
            y3 = len(line)
            printcon = line[(sel4+2):(y3-1)]
            a.append(printcon)
def presortfunction3():
    t = totalquestions + 1
    searchterm = " " + str(recqon) + "P"
    notsearch = " " + str(t) + "P"
    y4 = open(name_full, 'r')
    linecon = y4.readlines()
    for line in linecon:
        findit = line.find(str(searchterm))
        if findit != -1:
            sel4 = line.index('.')
            y5 = len(line)
            printcon = line[(sel4+2):(y5-1)]
            b.append(printcon)
        elif searchterm == notsearch:
            print(l)
            path = d[l]
            pdfFileObject = open(path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
            totalpages = pdfReader.getNumPages()
            b.append(totalpages)
            break
def searchfn():
    global c
    global o
    c = []
    o = 0
    sl = 2010
    while (sl<=2080):
        hl = str(sl)
        for terms in arr:
            if terms == hl:
                jl = arr.index(hl)
                print("SUCCESS")
                c.append(jl)
                o+=1
        sl+=1
    c.append(len(arr))
    finalsortfunction()
def presortfunction4():
    global pathcon
    term_of_search = "path:"
    y6 = open(name_full, 'r')
    linecon = y6.readlines()
    for line in linecon:
        findterm = line.find(str(term_of_search))
        if findterm != -1:
            sel4 = line.index(":")
            y7 = len(line)
            printcon = line[(sel4+1):(y7-1)]
            pathcon = str(printcon)
            print(pathcon)
            d.append(pathcon)
def finalsortfunction():
    global r1
    global r2
    global newval
    global oldval
    global m
    m = 0
    p = 0
    q = 1
    z = 0
    f = 0
    oldval = 0
    while q<=o:
        x1 = c[p]
        x2 = c[q]
        x = x2-x1
        x = x - 1
        f = f + x
        newval = d
        while z<f:
            r1 = a[z]
            r2 = b[z]
            z+=1
            print(r1)
            print(r2)
            print(f)
            print( )
            pdfextraction()
            m+=1
        p+=1
        q+=1
        oldval = f
def pdfextraction():
    print(m)
    path = d[m]
    pdfFileObject = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    start = int(r1)
    end = int(r2)
    pdfWriter = PyPDF2.PdfFileWriter()
    if m<len(b):
        file_output = "OUTPUT" + str(m) + ".pdf"
        path_input = d[m]
        pdfFileObject = open(path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        for page in range (start, end):
            pdfWriter.addPage(pdfReader.getPage(page))
        with open(file_output, "wb") as f:
            pdfWriter.write(f)
        finalarr.append(file_output)
    pdfmerger2()
def pdfmerger2():
    path_final = "C:/Users/Ajit/Desktop/PROGRAMS/IB"
    output_file = 'TOPIC' + str(choice1) + " QUESTIONS LOADED.pdf"
    output_final = os.path.join(path_final, output_file)
    print(finalarr)
    pdfMerger = PyPDF2.PdfFileMerger()
    for pdf in finalarr: 
        pdfMerger.append(pdf) 
    with open(output_final, 'wb') as f: 
        pdfMerger.write(f)
        pdfMerger.close()
def fileremover():
    for s in finalarr:
        os.remove(s)
window1 = theme.ThemedTk()
window1.get_themes()
window1.set_theme("plastik")
window1.title("TASK")
window1.geometry("400x400")
myFONT = tkFont.Font(family = "Century Gothic", size = 12, weight = "bold")
browse = ttk.Button(window1, text = "LOAD", width = 40, command = browsefn)
browse.pack()
access = ttk.Button(window1, text = "ACCESS", width = 40, command = choice)
access.pack()
escape = ttk.Button(window1, text = "EXIT", width = 20, command = window1.destroy)
escape.pack()
window1.mainloop()