import json
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import time
import os
import sys
from subprocess import call

from PIL import Image
from PIL import ImageTk

from tkinter import filedialog

with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

bfsAnswerChoice = [1, 2, 3, 4, 5, 6]

answers = [1, 2, 3, 0, 3, 1, 3, 1, 0, 2]

user_answer = []

indexes = []


def gen():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    global img, labelimage, labelresulttext
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Can Be Better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Work Harder !!")

    global imgquizhome, btnquizhome
    imgquizhome = PhotoImage(file="quizHome.png")
    btnquizhome = Button(
        root,
        image=imgquizhome,
        relief=FLAT,
        border=0,
        command=quizhome
    )
    btnquizhome.place(x=900, y=650)

def quizhome():
    labelimage.destroy()
    labelresulttext.destroy()
    btnquizhome.destroy()
    fp()


def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:

        calc()


def startquiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas", 16),
        width=1000,
        justify="center",
        wraplength=500,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblRules.destroy()
    btnStart.destroy()
    btnStart2.destroy()
    btnStart3.destroy()
    btnStart4.destroy()
    btnStart5.destroy()
    gen()
    startquiz()


# ......................................................................................

def startquiz1():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=500,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

#=====================================================BFS=============================================================#
# ......................................................................................

def startIspressed1():
    labelimage.destroy()
    labeltext.destroy()
    lblRules.destroy()
    btnStart.destroy()
    btnStart2.destroy()
    btnStart3.destroy()
    btnStart4.destroy()
    btnStart5.destroy()

    global imgNext, btnNext
    imgNext = PhotoImage(file="Next.png")
    btnNext = Button(
        root,
        image=imgNext,
        relief=FLAT,
        border=0,
        command=nextIsPressed1,
    )
    btnNext.place(x=900, y=650)  # 1080x720

    global imagelist, photo, canvas
    imagelist = ["BFS1.gif", "BFS2.gif", "BFS3.gif", "BFS4.gif", "BFS5.gif", "BFS6.gif",
                 "BFS7.gif", "BFS8.gif"]

    # extract width and height info
    photo = PhotoImage(file=imagelist[0])
    width = photo.width()
    height = photo.height()
    canvas = Canvas(width=width, height=height)
    canvas.pack()

    # create a list of image objects
    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=imagefile)
        giflist.append(photo)

    # loop through the gif image objects for a while
    for k in range(0, 1000):
        for gif in giflist:
            canvas.delete(ALL)
            canvas.create_image(width / 2.0, height / 2.0, image=gif)
            canvas.update()
            time.sleep(0.1)

    root.mainloop()

# ......................................................................................

def nextIsPressed1():
    btnNext.destroy()
    canvas.destroy()

    global imgBFSGame, labelimgBFSGame
    imgBFSGame = PhotoImage(file="BFSGame.png")
    labelimgBFSGame = Label(
        root,
        image=imgBFSGame,
        background="#ffffff",
    )
    labelimgBFSGame.pack(pady=(40, 0))

    global imgNext1, btnNext1
    imgNext1 = PhotoImage(file="Next.png")
    btnNext1 = Button(
        root,
        image=imgNext,
        relief=FLAT,
        border=0,
        command=nextIsPressed2,
    )
    btnNext1.place(x=900, y=650)

# ......................................................................................

def nextIsPressed2():
    btnNext1.destroy()
    labelimgBFSGame.destroy()

    global bfsq1, labelbfsq1
    bfsq1 = PhotoImage(file="bq1.png")
    labelbfsq1 = Label(
        root,
        image=bfsq1,
        background="#ffffff",
    )
    labelbfsq1.pack(pady=(40, 0))

    #........................................................

    global node1, node2, node3, node4, node5, node6
    global node1value, node2value, node3value, node4value, node5value, node6value
    global node1entry, node2entry, node3entry, node4entry,node5entry, node6entry

    # Text for our form
    node1 = Label(root, text="Node 1", background="#ffffff")
    node2 = Label(root, text="Node 2", background="#ffffff")
    node3 = Label(root, text="Node 3", background="#ffffff")
    node4 = Label(root, text="Node 4", background="#ffffff")
    node5 = Label(root, text="Node 5", background="#ffffff")
    node6 = Label(root, text="Node 6", background="#ffffff")

    # Pack text for our form
    node1.place(x=500, y=470)
    node2.place(x=500, y=495)
    node3.place(x=500, y=520)
    node4.place(x=500, y=545)
    node5.place(x=500, y=570)
    node6.place(x=500, y=595)

    # Tkinter variable for storing entries
    node1value = StringVar()
    node2value = StringVar()
    node3value = StringVar()
    node4value = StringVar()
    node5value = StringVar()
    node6value = StringVar()

    # Entries for our form
    node1entry = Entry(root, textvariable=node1value)
    node2entry = Entry(root, textvariable=node2value)
    node3entry = Entry(root, textvariable=node3value)
    node4entry = Entry(root, textvariable=node4value)
    node5entry = Entry(root, textvariable=node5value)
    node6entry = Entry(root, textvariable=node6value)

    # Packing the Entries
    node1entry.place(x=580, y=470)
    node2entry.place(x=580, y=495)
    node3entry.place(x=580, y=520)
    node4entry.place(x=580, y=545)
    node5entry.place(x=580, y=570)
    node6entry.place(x=580, y=595)

    # ........................................................
    global imgNext3, btnNext3
    imgNext3 = PhotoImage(file="Next.png")
    btnNext3 = Button(
        root,
        image=imgNext3,
        relief=FLAT,
        border=0,
        command = getvals
    )
    btnNext3.place(x=900, y=650)

# ......................................................................................


def getvals():
    j = (node1value.get(), node2value.get(), node3value.get(), node4value.get(), node5value.get(), node6value.get())
    answer = ('1', '2', '3', '4', '6', '5')

    if (j == answer):
        fnbfsq2()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')

# ......................................................................................

def fnbfsq2():
    labelbfsq1.destroy()
    btnNext3.destroy()
    node1entry.destroy()
    node2entry.destroy()
    node3entry.destroy()
    node4entry.destroy()
    node5entry.destroy()
    node6entry.destroy()

    global bfsq2, labelbfsq2
    bfsq2 = PhotoImage(file="bq2.png")
    labelbfsq2 = Label(
        root,
        image=bfsq2,
        background="#ffffff",
    )
    labelbfsq2.pack(pady=(40, 0))

    global node1value2, node2value2, node3value2, node4value2, node5value2, node6value2
    global node1entry2, node2entry2, node3entry2, node4entry2, node5entry2, node6entry2

    # Tkinter variable for storing entries
    node1value2 = StringVar()
    node2value2 = StringVar()
    node3value2 = StringVar()
    node4value2 = StringVar()
    node5value2 = StringVar()
    node6value2 = StringVar()

    # Entries for our form
    node1entry2 = Entry(root, textvariable=node1value2)
    node2entry2 = Entry(root, textvariable=node2value2)
    node3entry2 = Entry(root, textvariable=node3value2)
    node4entry2 = Entry(root, textvariable=node4value2)
    node5entry2 = Entry(root, textvariable=node5value2)
    node6entry2 = Entry(root, textvariable=node6value2)

    # Packing the Entries
    node1entry2.place(x=580, y=470)
    node2entry2.place(x=580, y=495)
    node3entry2.place(x=580, y=520)
    node4entry2.place(x=580, y=545)
    node5entry2.place(x=580, y=570)
    node6entry2.place(x=580, y=595)

    #........................................................

    global imgNext4, btnNext4
    imgNext4 = PhotoImage(file="Next.png")
    btnNext4 = Button(
        root,
        image=imgNext4,
        relief=FLAT,
        border=0,
        command=getvals2
    )
    btnNext4.place(x=900, y=650)

# ......................................................................................

def getvals2():
    j = (node1value2.get(), node2value2.get(), node3value2.get(), node4value2.get(), node5value2.get(), node6value2.get())
    answer = ('1', '5', '6', '3', '2', '4')

    if (j == answer):
        fnbfsq3()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')

# ......................................................................................

def fnbfsq3():
    labelbfsq2.destroy()
    btnNext4.destroy()
    node1entry2.destroy()
    node2entry2.destroy()
    node3entry2.destroy()
    node4entry2.destroy()
    node5entry2.destroy()
    node6entry2.destroy()

    global bfsq3, labelbfsq3
    bfsq3 = PhotoImage(file="bq3.png")
    labelbfsq3 = Label(
        root,
        image=bfsq3,
        background="#ffffff",
    )
    labelbfsq3.pack(pady=(40, 0))

    global node1value3, node2value3, node3value3, node4value3, node5value3, node6value3
    global node1entry3, node2entry3, node3entry3, node4entry3, node5entry3, node6entry3

    # Tkinter variable for storing entries
    node1value3 = StringVar()
    node2value3 = StringVar()
    node3value3 = StringVar()
    node4value3 = StringVar()
    node5value3 = StringVar()
    node6value3 = StringVar()

    # Entries for our form
    node1entry3 = Entry(root, textvariable=node1value3)
    node2entry3 = Entry(root, textvariable=node2value3)
    node3entry3 = Entry(root, textvariable=node3value3)
    node4entry3 = Entry(root, textvariable=node4value3)
    node5entry3 = Entry(root, textvariable=node5value3)
    node6entry3 = Entry(root, textvariable=node6value3)

    # Packing the Entries
    node1entry3.place(x=580, y=470)
    node2entry3.place(x=580, y=495)
    node3entry3.place(x=580, y=520)
    node4entry3.place(x=580, y=545)
    node5entry3.place(x=580, y=570)
    node6entry3.place(x=580, y=595)
    #........................................................

    global imgNext5, btnNext5
    imgNext5 = PhotoImage(file="Next.png")
    btnNext5 = Button(
        root,
        image=imgNext5,
        relief=FLAT,
        border=0,
        command=getvals3
    )
    btnNext5.place(x=900, y=650)


# ......................................................................................

def getvals3():
    j = (node1value3.get(), node2value3.get(), node3value3.get(), node4value3.get(), node5value3.get(),
         node6value3.get())
    answer = ('3', '1', '5', '2', '4', '6')

    if (j == answer):
        welldonebfs()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')


# ......................................................................................

def welldonebfs():
    btnNext5.destroy()
    labelbfsq3.destroy()
    node1entry3.destroy()
    node2entry3.destroy()
    node3entry3.destroy()
    node4entry3.destroy()
    node5entry3.destroy()
    node6entry3.destroy()
    node1.destroy()
    node2.destroy()
    node3.destroy()
    node4.destroy()
    node5.destroy()
    node6.destroy()

    global imgBFSend, labelimgBFSend
    imgBFSend = PhotoImage(file="BFSend.png")
    labelimgBFSend = Label(
        root,
        image=imgBFSend,
        background="#ffffff",
    )
    labelimgBFSend.pack(pady=(40, 0))

    global imgbfsHome, btnbfsHome
    imgbfsHome = PhotoImage(file="bfsHome.png")
    btnbfsHome = Button(
        root,
        image=imgbfsHome,
        relief=FLAT,
        border=0,
        command=bfsHome
    )
    btnbfsHome.place(x=900, y=650)


def bfsHome():
    labelimgBFSend.destroy()
    btnbfsHome.destroy()
    fp()


#=====================================================DFS=============================================================#
# ......................................................................................
def startIspressed2():
    labelimage.destroy()
    labeltext.destroy()
    lblRules.destroy()
    btnStart.destroy()
    btnStart2.destroy()
    btnStart3.destroy()
    btnStart4.destroy()
    btnStart5.destroy()

    global imgNext, btnNext
    imgNext = PhotoImage(file="NextDark.png")
    btnNext = Button(
        root,
        image=imgNext,
        relief=FLAT,
        border=0,
        command=nextIsPressed3,
    )
    btnNext.place(x=900, y=650)

    global imagelist, photo, canvas
    imagelist = ["DFS1.gif", "DFS2.gif", "DFS3.gif", "DFS4.gif", "DFS5.gif", "DFS6.gif",
                 "DFS7.gif", "DFS8.gif", "DFS9.gif", "DFS10.gif", "DFS11.gif"]

    # extract width and height info
    photo = PhotoImage(file=imagelist[0])
    width = photo.width()
    height = photo.height()
    canvas = Canvas(width=width, height=height)
    canvas.pack()

    # create a list of image objects
    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=imagefile)
        giflist.append(photo)

    # loop through the gif image objects for a while
    for k in range(0, 1000):
        for gif in giflist:
            canvas.create_image(width / 2.0, height / 2.0, image=gif)
            canvas.update()
            time.sleep(0.1)

    root.mainloop()

# ......................................................................................

def nextIsPressed3():
    btnNext.destroy()
    canvas.destroy()

    global imgDFSGame, labelimgDFSGame
    imgDFSGame = PhotoImage(file="DFSGame.png")
    labelimgDFSGame = Label(
        root,
        image=imgDFSGame,
        background="#ffffff",
    )
    labelimgDFSGame.pack()

    global imgNext3, btnNext3
    imgNext3 = PhotoImage(file="NextDark.png")
    btnNext3 = Button(
        root,
        image=imgNext3,
        relief=FLAT,
        border=0,
        command=nextIsPressed4,
    )
    btnNext3.place(x=900, y=650)

# ......................................................................................

def nextIsPressed4():
    btnNext3.destroy()
    labelimgDFSGame.destroy()

    global dfsq1, labeldfsq1
    dfsq1 = PhotoImage(file="dq1.png")
    labeldfsq1 = Label(
        root,
        image=dfsq1,
        background="#ffffff",
    )
    labeldfsq1.pack(pady=(40, 0))

    # ........................................................

    global node14, node24, node34, node44, node54, node64
    global node1value4, node2value4, node3value4, node4value4, node5value4, node6value4
    global node1entry4, node2entry4, node3entry4, node4entry4, node5entry4, node6entry4

    # Text for our form
    node14 = Label(root, text="Node 1", background="#ffffff")
    node24 = Label(root, text="Node 2", background="#ffffff")
    node34 = Label(root, text="Node 3", background="#ffffff")
    node44 = Label(root, text="Node 4", background="#ffffff")
    node54 = Label(root, text="Node 5", background="#ffffff")
    node64 = Label(root, text="Node 6", background="#ffffff")

    # Pack text for our form
    node14.place(x=500, y=470)
    node24.place(x=500, y=495)
    node34.place(x=500, y=520)
    node44.place(x=500, y=545)
    node54.place(x=500, y=570)
    node64.place(x=500, y=595)

    # Tkinter variable for storing entries
    node1value4 = StringVar()
    node2value4 = StringVar()
    node3value4 = StringVar()
    node4value4 = StringVar()
    node5value4 = StringVar()
    node6value4 = StringVar()

    # Entries for our form
    node1entry4 = Entry(root, textvariable=node1value4)
    node2entry4 = Entry(root, textvariable=node2value4)
    node3entry4 = Entry(root, textvariable=node3value4)
    node4entry4 = Entry(root, textvariable=node4value4)
    node5entry4 = Entry(root, textvariable=node5value4)
    node6entry4 = Entry(root, textvariable=node6value4)

    # Packing the Entries
    node1entry4.place(x=580, y=470)
    node2entry4.place(x=580, y=495)
    node3entry4.place(x=580, y=520)
    node4entry4.place(x=580, y=545)
    node5entry4.place(x=580, y=570)
    node6entry4.place(x=580, y=595)

    # ........................................................
    global imgNextDark4, btnNextDark4
    imgNextDark4 = PhotoImage(file="NextDark.png")
    btnNextDark4= Button(
        root,
        image=imgNextDark4,
        relief=FLAT,
        border=0,
        command=getvals4
    )
    btnNextDark4.place(x=900, y=650)


# ......................................................................................


def getvals4():
    j = (node1value4.get(), node2value4.get(), node3value4.get(), node4value4.get(), node5value4.get(),
         node6value4.get())
    answer = ('1', '2', '4', '3', '6', '5')

    if (j == answer):
        fndfsq2()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')


# ......................................................................................

def fndfsq2():
    labeldfsq1.destroy()
    btnNextDark4.destroy()
    node1entry4.destroy()
    node2entry4.destroy()
    node3entry4.destroy()
    node4entry4.destroy()
    node5entry4.destroy()
    node6entry4.destroy()

    global dfsq2, labeldfsq2
    dfsq2 = PhotoImage(file="dq2.png")
    labeldfsq2 = Label(
        root,
        image=dfsq2,
        background="#ffffff",
    )
    labeldfsq2.pack(pady=(40, 0))

    global node1value5, node2value5, node3value5, node4value5, node5value5, node6value5
    global node1entry5, node2entry5, node3entry5, node4entry5, node5entry5, node6entry5

    # Tkinter variable for storing entries
    node1value5 = StringVar()
    node2value5 = StringVar()
    node3value5 = StringVar()
    node4value5 = StringVar()
    node5value5 = StringVar()
    node6value5 = StringVar()

    # Entries for our form
    node1entry5 = Entry(root, textvariable=node1value5)
    node2entry5 = Entry(root, textvariable=node2value5)
    node3entry5 = Entry(root, textvariable=node3value5)
    node4entry5 = Entry(root, textvariable=node4value5)
    node5entry5 = Entry(root, textvariable=node5value5)
    node6entry5 = Entry(root, textvariable=node6value5)

    # Packing the Entries
    node1entry5.place(x=580, y=470)
    node2entry5.place(x=580, y=495)
    node3entry5.place(x=580, y=520)
    node4entry5.place(x=580, y=545)
    node5entry5.place(x=580, y=570)
    node6entry5.place(x=580, y=595)

    # ........................................................

    global imgNextDark5, btnNextDark5
    imgNextDark5 = PhotoImage(file="NextDark.png")
    btnNextDark5 = Button(
        root,
        image=imgNextDark5,
        relief=FLAT,
        border=0,
        command=getvals5
    )
    btnNextDark5.place(x=900, y=650)


# ......................................................................................

def getvals5():
    j = (node1value5.get(), node2value5.get(), node3value5.get(), node4value5.get(), node5value5.get(),
         node6value5.get())
    answer = ('1', '5', '3', '2', '4', '6')

    if (j == answer):
        fndfsq3()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')


# ......................................................................................

def fndfsq3():
    labeldfsq2.destroy()
    btnNextDark5.destroy()
    node1entry5.destroy()
    node2entry5.destroy()
    node3entry5.destroy()
    node4entry5.destroy()
    node5entry5.destroy()
    node6entry5.destroy()

    global dfsq3, labeldfsq3
    dfsq3 = PhotoImage(file="dq3.png")
    labeldfsq3 = Label(
        root,
        image=dfsq3,
        background="#ffffff",
    )
    labeldfsq3.pack(pady=(40, 0))

    global node1value6, node2value6, node3value6, node4value6, node5value6, node6value6
    global node1entry6, node2entry6, node3entry6, node4entry6, node5entry6, node6entry6

    # Tkinter variable for storing entries
    node1value6 = StringVar()
    node2value6 = StringVar()
    node3value6 = StringVar()
    node4value6 = StringVar()
    node5value6 = StringVar()
    node6value6 = StringVar()

    # Entries for our form
    node1entry6 = Entry(root, textvariable=node1value6)
    node2entry6 = Entry(root, textvariable=node2value6)
    node3entry6 = Entry(root, textvariable=node3value6)
    node4entry6 = Entry(root, textvariable=node4value6)
    node5entry6 = Entry(root, textvariable=node5value6)
    node6entry6 = Entry(root, textvariable=node6value6)

    # Packing the Entries
    node1entry6.place(x=580, y=470)
    node2entry6.place(x=580, y=495)
    node3entry6.place(x=580, y=520)
    node4entry6.place(x=580, y=545)
    node5entry6.place(x=580, y=570)
    node6entry6.place(x=580, y=595)

    # ........................................................
    global imgNextDark6, btnNextDark6
    imgNextDark6 = PhotoImage(file="NextDark.png")
    btnNextDark6 = Button(
        root,
        image=imgNextDark6,
        relief=FLAT,
        border=0,
        command=getvals6
    )
    btnNextDark6.place(x=900, y=650)


# ......................................................................................

def getvals6():
    j = (node1value6.get(), node2value6.get(), node3value6.get(), node4value6.get(), node5value6.get(),
         node6value6.get())
    answer = ('3', '1', '2', '4', '6', '5')

    if (j == answer):
        welldonedfs()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')


# ......................................................................................

def welldonedfs():
    btnNextDark6.destroy()
    labeldfsq3.destroy()
    node14.destroy()
    node24.destroy()
    node34.destroy()
    node44.destroy()
    node54.destroy()
    node64.destroy()
    node1entry6.destroy()
    node2entry6.destroy()
    node3entry6.destroy()
    node4entry6.destroy()
    node5entry6.destroy()
    node6entry6.destroy()

    global imgDFSend, labelimgDFSend
    imgDFSend = PhotoImage(file="DFSend.png")
    labelimgDFSend = Label(
        root,
        image=imgDFSend,
        background="#ffffff",
    )
    labelimgDFSend.pack(pady=(40, 0))

    global imgdfshome, btndfshome
    imgdfshome = PhotoImage(file="dfsHome.png")
    btndfshome = Button(
        root,
        image=imgdfshome,
        relief=FLAT,
        border=0,
        command=dfsHome
    )
    btndfshome.place(x=900, y=650)


def dfsHome():
    labelimgDFSend.destroy()
    btndfshome.destroy()
    fp()

# ......................................................................................
#=====================================================Linear Search====================================================#

def startIspressed3():
    labelimage.destroy()
    labeltext.destroy()
    lblRules.destroy()
    btnStart.destroy()
    btnStart2.destroy()
    btnStart3.destroy()
    btnStart4.destroy()
    btnStart5.destroy()

    global imgNextLinear, btnNextlinear
    imgNextLinear = PhotoImage(file="NextLinear.png")
    btnNextlinear = Button(
        root,
        image=imgNextLinear,
        relief=FLAT,
        border=0,
        command=nextIsPressed5
    )
    btnNextlinear.place(x=900, y=650)  # 1080x720

    global imagelist, photo, canvas
    imagelist = ["LinearIntro1.gif", "LinearIntro2.gif", "LinearIntro3.gif", "LinearIntro4.gif", "LinearIntro5.gif",
                 "LinearIntro6.gif", "LinearIntro7.gif", "LinearIntro8.gif", "LinearIntro9.gif", "LinearIntro10.gif"]

    # extract width and height info
    photo = PhotoImage(file=imagelist[0])
    width = photo.width()
    height = photo.height()
    canvas = Canvas(width=width, height=height)
    canvas.pack()

    # create a list of image objects
    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=imagefile)
        giflist.append(photo)

    # loop through the gif image objects for a while
    for k in range(0, 1000):
        for gif in giflist:
            canvas.create_image(width / 2.0, height / 2.0, image=gif)
            canvas.update()
            time.sleep(0.5)

    root.mainloop()

# ......................................................................................

def nextIsPressed5():
    btnNextlinear.destroy()
    canvas.destroy()

    global imgLinearGame, labelimgLinearGame
    imgLinearGame = PhotoImage(file="LinearSearchGame.png")
    labelimgLinearGame = Label(
        root,
        image=imgLinearGame,
        background="#ffffff",
    )
    labelimgLinearGame.pack()

    global imgNextLinear5, btnNextLinear5
    imgNextLinear5 = PhotoImage(file="NextLinear.png")
    btnNextLinear5 = Button(
        root,
        image=imgNextLinear5,
        relief=FLAT,
        border=0,
        command=run,
    )
    btnNextLinear5.place(x=900, y=650)

    global imgLinearHome, btnLinearHome
    imgLinearHome = PhotoImage(file="LinearHome.png")
    btnLinearHome = Button(
        root,
        image=imgLinearHome,
        relief=FLAT,
        border=0,
        command=linearHome,
    )
    btnLinearHome.place(x=20, y=650)

# ......................................................................................

def run():
    call(["python", "linearSearch.py"])

def linearHome():
    labelimgLinearGame.destroy()
    btnNextLinear5.destroy()
    btnLinearHome.destroy()
    fp()


#=====================================================Binary Search====================================================#
# ......................................................................................

def startIspressed4():
    labelimage.destroy()
    labeltext.destroy()
    lblRules.destroy()
    btnStart.destroy()
    btnStart2.destroy()
    btnStart3.destroy()
    btnStart4.destroy()
    btnStart5.destroy()

    global imgNextBinary, btnNextBinary
    imgNextBinary = PhotoImage(file="NextBinary.png")
    btnNextBinary = Button(
        root,
        image=imgNextBinary,
        relief=FLAT,
        border=0,
        command=nextIsPressed6
    )
    btnNextBinary.place(x=900, y=650)  # 1080x720

    global imagelist, photo, canvas
    imagelist = ["BinaryIntro1.gif", "BinaryIntro2.gif", "BinaryIntro3.gif", "BinaryIntro4.gif", "BinaryIntro5.gif",
                 "BinaryIntro6.gif", "BinaryIntro7.gif", "BinaryIntro8.gif", "BinaryIntro9.gif", "BinaryIntro10.gif",
                 "BinaryIntro11.gif", "BinaryIntro12.gif", "BinaryIntro13.gif", "BinaryIntro14.gif", "BinaryIntro15.gif",
                 "BinaryIntro16.gif", "BinaryIntro17.gif", "BinaryIntro18.gif", "BinaryIntro19.gif"]

    # extract width and height info
    photo = PhotoImage(file=imagelist[0])
    width = photo.width()
    height = photo.height()
    canvas = Canvas(width=width, height=height)
    canvas.pack()

    # create a list of image objects
    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=imagefile)
        giflist.append(photo)

    # loop through the gif image objects for a while
    for k in range(0, 1000):
        for gif in giflist:
            canvas.create_image(width / 2.0, height / 2.0, image=gif)
            canvas.update()
            time.sleep(0.7)

    root.mainloop()

# ......................................................................................

def nextIsPressed6():
    btnNextBinary.destroy()
    canvas.destroy()

    global imgBinaryGame, labelimgBinaryGame
    imgBinaryGame = PhotoImage(file="BinarySearchGame.png")
    labelimgBinaryGame = Label(
        root,
        image=imgBinaryGame,
        background="#ffffff",
    )
    labelimgBinaryGame.pack()

    global imgNextBinary6, btnNextBinary6
    imgNextBinary6 = PhotoImage(file="NextBinary.png")
    btnNextBinary6 = Button(
        root,
        image=imgNextBinary6,
        relief=FLAT,
        border=0,
        command=fnbinaryq1,
    )
    btnNextBinary6.place(x=900, y=650)

# ......................................................................................


def fnbinaryq1():
    labelimgBinaryGame.destroy()
    btnNextBinary6.destroy()

    global binaryq1, labeldbinaryq1
    binaryq1 = PhotoImage(file="binaryq1.png")
    labeldbinaryq1 = Label(
        root,
        image=binaryq1,
        background="#ffffff",
    )
    labeldbinaryq1.pack(pady=(40, 0))

    global field1, field1value, field1entry

    field1 = Label(root, text="Enter Number", background="#ffffff")
    field1.place(x=400, y=500)
    field1value = StringVar()
    field1entry = Entry(root, textvariable=field1value)
    field1entry.place(x=500, y=500)

    global imgNextBinary7, btnNextBinary7
    imgNextBinary7 = PhotoImage(file="NextBinary.png")
    btnNextBinary7 = Button(
        root,
        image=imgNextBinary7,
        relief=FLAT,
        border=0,
        command=getvals7
    )
    btnNextBinary7.place(x=900, y=650)


# ......................................................................................

def getvals7():
    answer = ('4', '2', '3')

    if(answer[root.count1] == field1value.get()):
        messagebox._show('Yay!', 'You have entered the correct answer. Enter the next number!')
        root.count1 += 1
        if(field1value.get() == '3'):
            fnbinaryq2()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')

# ......................................................................................

def fnbinaryq2():
    field1.destroy()
    field1entry.destroy()
    btnNextBinary7.destroy()
    labeldbinaryq1.destroy()

    global binaryq2, labeldbinaryq2
    binaryq2 = PhotoImage(file="binaryq2.png")
    labeldbinaryq2 = Label(
        root,
        image=binaryq2,
        background="#ffffff",
    )
    labeldbinaryq2.pack(pady=(40, 0))

    global field2, field2value, field2entry

    field2 = Label(root, text="Enter Number", background="#ffffff")
    field2.place(x=400, y=500)
    field2value = StringVar()
    field2entry = Entry(root, textvariable=field2value)
    field2entry.place(x=500, y=500)

    global imgNextBinary8, btnNextBinary8
    imgNextBinary8 = PhotoImage(file="NextBinary.png")
    btnNextBinary8 = Button(
        root,
        image=imgNextBinary8,
        relief=FLAT,
        border=0,
        command=getvals8
    )
    btnNextBinary8.place(x=900, y=650)


# ......................................................................................

def getvals8():
    answer = ('4', '6', '7')

    if(answer[root.count2] == field2value.get()):
        messagebox._show('Yay!', 'You have entered the correct answer. Enter the next number!')
        root.count2 += 1
        if(field2value.get() == '7'):
            fnbinaryq3()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')

# ......................................................................................

def fnbinaryq3():
    field2.destroy()
    field2entry.destroy()
    btnNextBinary8.destroy()
    labeldbinaryq2.destroy()

    global binaryq3, labeldbinaryq3
    binaryq3 = PhotoImage(file="binaryq3.png")
    labeldbinaryq3 = Label(
        root,
        image=binaryq3,
        background="#ffffff",
    )
    labeldbinaryq3.pack(pady=(40, 0))

    global field3, field3value, field3entry

    field3 = Label(root, text="Enter Number", background="#ffffff")
    field3.place(x=400, y=500)
    field3value = StringVar()
    field3entry = Entry(root, textvariable=field3value)
    field3entry.place(x=500, y=500)

    global imgNextBinary9, btnNextBinary9
    imgNextBinary9 = PhotoImage(file="NextBinary.png")
    btnNextBinary9 = Button(
        root,
        image=imgNextBinary9,
        relief=FLAT,
        border=0,
        command=getvals9
    )
    btnNextBinary9.place(x=900, y=650)


# ......................................................................................

def getvals9():
    answer = ('4', '2')

    if(answer[root.count3] == field3value.get()):
        messagebox._show('Yay!', 'You have entered the correct answer. Enter the next number!')
        root.count3 += 1
        if(field3value.get() == '2'):
            welldonebinary()
    else:
        messagebox._show('Oops!', 'You have entered the wrong answer. Try again!')

# ......................................................................................

def welldonebinary():
    field3.destroy()
    field3entry.destroy()
    btnNextBinary9.destroy()
    labeldbinaryq3.destroy()

    global imgBinaryend, labelimgBinaryend
    imgBinaryend = PhotoImage(file="Binaryend.png")
    labelimgBinaryend = Label(
        root,
        image=imgBinaryend,
        background="#ffffff",
    )
    labelimgBinaryend.pack(pady=(40, 0))

    global imgbinaryhome, btnbinaryhome
    imgbinaryhome = PhotoImage(file="binaryHome.png")
    btnbinaryhome = Button(
        root,
        image=imgbinaryhome,
        relief=FLAT,
        border=0,
        command=binaryhome
    )
    btnbinaryhome.place(x=900, y=650)


def binaryhome():
    labelimgBinaryend.destroy()
    btnbinaryhome.destroy()
    fp()

# ......................................................................................

def fp():

    global img1, labelimage, labeltext, img2, imgx, imgy, imgq, imgr, btnStart, btnStart2, btnStart3, btnStart4, btnStart5, lblRules
    img1 = PhotoImage(file="controller.png")

    labelimage = Label(
        root,
        image=img1,
        background="#ffffff",
    )
    labelimage.pack(pady=(0, 0))

    labeltext = Label(
        root,
        text="DSGo!",
        font=("Chiller", 24, "bold"),
        background="#ffffff",
    )
    labeltext.pack(pady=(0, 15))

    img2 = PhotoImage(file="Frame.png")
    imgx = PhotoImage(file="LearnBFS.png")
    imgy = PhotoImage(file="LearnDFS.png")
    imgq = PhotoImage(file="LearnLinearSearch.png")
    imgr = PhotoImage(file="LearnBinarySearch.png")

    btnStart = Button(
        root,
        image=img2,
        relief=FLAT,
        border=0,
        command=startIspressed,
    )
    btnStart.pack()

    btnStart2 = Button(
        root,
        image=imgx,
        relief=FLAT,
        border=0,
        command=startIspressed1,
    )
    btnStart2.pack()

    btnStart3 = Button(
        root,
        image=imgy,
        relief=FLAT,
        border=0,
        command=startIspressed2,
    )
    btnStart3.pack()

    btnStart4 = Button(
        root,
        image=imgq,
        relief=FLAT,
        border=0,
        command=startIspressed3,
    )
    btnStart4.pack()

    btnStart5 = Button(
        root,
        image=imgr,
        relief=FLAT,
        border=0,
        command=startIspressed4,
    )
    btnStart5.pack()

    lblRules = Label(
        root,
        text="Let's Learn Some Data Structures",
        width=100,
        font=("Time", 14),
        background="#000000",
        foreground="#ffffff",
    )
    lblRules.pack(pady=(15, 0))

    root.mainloop()

root = tkinter.Tk()
root.title("DSGo!")
root.geometry("1080x720")
root.config(background="#ffffff")
root.resizable(0, 0)
root.count1 = 0
root.count2 = 0
root.count3 = 0
fp()