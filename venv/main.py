from tkinter import *
import turtle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from copy import copy
#------------------------------------------------------------------------------
def FCFS(Request, Start):
    Sum = 0                     #initialize to 0
    position = Start            #set current position = start
    Order = []                  # creates empty list of name Order
    Order.append(Start)         #adds Start to end of list Order
    for i in Request:           # i is the current element in the list(first loop i = 95)
        Sum += abs(i-position)  # sum = sum + (distance of current position from next position)
        position = i            # set position new position (i)
        Order.append(i)         # Add i to the end of the list Order
    return Order, Sum
#------------------------------------------------------------------------------
def SSTF(Request,Start):
    templist = copy(Request)
    position = Start
    highest = max(templist)
    mindiff=abs(Start-highest)
    j=highest
    templist.sort()
    Order = []
    Order.append(Start)
    Sum = 0
    while len(templist) > 0:
        for i in templist:
                diff= abs(position-i)
                if diff<mindiff:
                    mindiff=diff
                    j=i
        Sum+= abs(position-j)
        position = j
        templist.remove(j)
        Order.append(j)
        mindiff=abs(position-highest)
        j=highest
    return Order, Sum
#------------------------------------------------------------------------------
def SCAN(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i -= 1



    k = Start + 1
    while k < 200:
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum

#------------------------------------------------------------------------------
def CSCAN(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i -= 1

    k = 199
    while k > Start:
        if(k == 199):
            Order.append(k)
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    SortedReq = copy(Order)
    SortedReq.sort()
    for p in range(0,len(Order) - 1):
        if (Order[p] != SortedReq[0]):
            Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def LOOK(Request, Start):
    n = len(Request)                        # Number of Requests
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:                            # Diskhead moving outward from start
        for j in range(0,n):                    #position
            if(Request[j] == i):            # Request found
                Order.append(i)             # Request executed
        i -= 1

    k = Start + 1
    while k < 200:                          # Diskhead moving inward from
        for l in range(0,n):                    #previous position
            if(Request[l] == k):            # Request found
                Order.append(k)             # Request executed
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
    return Order, Sum
#------------------------------------------------------------------------------
def CLOOK(Request, Start):
    n = len(Request)                            # Number of requests
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:                                # Diskhead moving outward from
        for j in range(0,n):                        #start position
            if(Request[j] == i):                # Request found
                Order.append(i)                 # Request executed
        i -= 1

    k = 199
    while k > Start:                            # Diskhead moving inward from
        for l in range(0,n):                        #highest request position
            if(Request[l] == k):                # Request found
                Order.append(k)                 # Request executed
        k -= 1

    Sum = 0
    SortedReq = copy(Order)                     # Creates copy of job order
    SortedReq.sort()                            # Sorts job order from lowest to
    for p in range(0,len(Order) - 1):               #highest
        if (Order[p] != SortedReq[0]):          # Excludes the circular movement
            Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
    return Order, Sum

def graphy(request_arr, start):
    plot_list=[]
    algos=["FCFS","SSTF","SCAN","CSCAN","LOOK","CLOOK"]
    dummy=0
    request=list(request_arr.split(" "))
    request=[int(i) for i in request]
    _,dummy=FCFS(request,start)
    plot_list.append(dummy)
    _,dummy=SSTF(request,start)
    plot_list.append(dummy)
    _,dummy=SCAN(request,start)
    plot_list.append(dummy)
    _,dummy=CSCAN(request,start)
    plot_list.append(dummy)
    _,dummy=LOOK(request,start)
    plot_list.append(dummy)
    _,dummy=CLOOK(request,start)
    plot_list.append(dummy)
    fig = plt.figure()
    fig.suptitle('Total Head Movement Graph', fontsize=14)
    plt.bar(algos, plot_list)
    plt.show()


#------------------------------------------------------------------------------

def Visualise(option, request_arr, start):
    request=list(request_arr.split(" "))
    request=[int(i) for i in request]
    if option == "FCFS":                        # Select and run algorithm
        Order, Sum = FCFS(request, start)
    elif option =="SSTF":
        Order, Sum = SSTF(request, start)
    elif option =="SCAN":
        Order, Sum = SCAN(request, start)
    elif option =="CSCAN":
        Order, Sum = CSCAN(request, start)
    elif option =="LOOK":
        Order, Sum = LOOK(request, start)
    elif option =="CLOOK":
        Order, Sum = CLOOK(request, start)

    import time
    turtle.clearscreen()
    t0 = time.time()
    Disk = turtle.Screen()
    Disk.title(option)
    Disk.bgcolor("white")
    Disk.setworldcoordinates(-5, -20, 210, 10)  # Set turtle window boundaries
    head = turtle.Turtle()
    head.shape("square")
    head.color("black")
    head.turtlesize(.3, .3, 1)
    head.speed(2)
    head.pensize(0)

    head2 = turtle.Turtle()
    head2.shape("circle")
    head2.color("green")
    head2.turtlesize(.3, .3, 1)
    head2.speed(4)
    head2.pensize(0)

    n = len(Order)
    y = -1
    y2=0
    temp_order=[int(i*10) for i in range(0,21)]
    for i in range(0,len(temp_order)):
        head2.goto(temp_order[i], y2)
        head2.stamp()
        head2.write(temp_order[i], False, align="right")


    for i in range(0, n):
        if i == 0:      # No drawing while the diskhead reaches start position
            head.penup()
            head.goto(Order[i], y)
            head.pendown()
            head.stamp()
            head.write(Order[i], False, align="right")
        else:           # Diskhead draws its path to each request
            head.goto(Order[i], y-1)
            head.stamp()
            head.write(Order[i], False, align="right")
            y -= 1
    head.hideturtle()
    head.speed(0)
    head.penup()
    head.goto(100, 5)
    t1 = time.time()


    message1 = "Disk Scheduling Algorithm: " + option
    message2 = "Total Head Movement: " + str(Sum)
    start = "\033[1m"
    end = "\033[0;0m"
    head.write(message1, False, align="center",font=("Century Gothic", 14) )    # Display algorithm used
    head.goto(100,4)
    head.write(message2, False, align="center",font=("Century Gothic", 14))     # Display total movement
    head.goto(100,3)
    head.write("Time taken: "+str(round(t1-t0, 2))+" Seconds", False, align="center",font=("Century Gothic", 14))
    head.pendown
    Disk.exitonclick()
#------------------------------------------------------------------------------
def Main():

    #List of colours
    mainbg="White"
    HeaderBG="Black"
    TextCol="Green"
    eleBG="#f0f0f0"
    #List of Messages
    algo="Choose Algorithm:"
    vals="Enter your values:"
    current="Current position of R/W head:"

    Menu = Tk()
    Menu.title("OS PROJECT")
    Menu.overrideredirect(False)
    Menu.iconbitmap("icon.ico")
    Menu.geometry("811x700+0+0")
    Menu.resizable(False, False)
    Menu.configure(bg='white')
    user_inp=Text(Menu,font=("Century Gothic", 16),width=20,height=1,bg=eleBG,fg=TextCol,bd=0)
    user_inp.grid(row=7, column=0)
    user_inp.config(highlightbackground = "Red",highlightcolor="Red")
    title=Label(Menu, text="Disk Scheduling GUI",anchor=CENTER, bd=12,padx=200, bg="#1A1C20", fg=mainbg, font=("Century Gothic",30), pady=2).grid(row=0)



    # List of options in dropdown menu
    optionlist = ('FCFS', 'SSTF', 'SCAN', 'CSCAN', 'LOOK', 'CLOOK')
    Option = StringVar()
    Start = IntVar()
    Option.set("FCFS")
    L1 = Label(Menu, text = algo,font=("Century Gothic", 16),bg=mainbg,fg=HeaderBG,pady=30)                # Label 1
    L1.grid(row=2,column=0)
    OM = OptionMenu(Menu, Option, *optionlist)                  # Dropdown menu
    OM.grid(row=3, column=0)
    OM.configure(bd = 0,bg=eleBG,fg=TextCol,highlightthickness = 0,padx=12,pady=12,font=("Century Gothic", 12))
    L2 = Label(Menu, text = current,font=("Century Gothic", 16),bg=mainbg,fg=HeaderBG,pady=30)            # Label 2
    L2.grid(row=12, column=0)
    E1 = Entry(Menu, textvariable = Start, bd = 0,fg=TextCol, width = 8,bg=eleBG,justify=CENTER,font=("Century Gothic", 16))   # Textbox
    E1.grid(row=13, column=0,)
    L1 = Label(Menu, text = "",font=("Century Gothic", 16),bg=mainbg,fg=mainbg,pady=5)                # Label 1
    L1.grid(row=14,column=0)
    B1 = Button(Menu,borderwidth=0,padx=20,pady=10,bg=eleBG,fg=TextCol, text = "Visualise",\
    command = lambda:Visualise(Option.get(), user_inp.get(1.0,END), Start.get()),font=("Century Gothic", 12))  # Button
    B1.grid(row=15, column=0)
    L1 = Label(Menu, text = "",font=("Century Gothic", 16),bg=mainbg,fg=mainbg,pady=5)                # Label 1
    L1.grid(row=16,column=0)
    B2 = Button(Menu,borderwidth=0,padx=20,pady=10,bg=eleBG,fg=TextCol, text = " Graph ",\
    command = lambda:graphy(user_inp.get(1.0,END), Start.get()),font=("Century Gothic", 12))  # Button
    B2.grid(row=17, column=0)
    L1 = Label(Menu, text = vals,font=("Century Gothic", 16),bg="white",fg=HeaderBG,pady=30)                # Label 1
    L1.grid(row=5,column=0)
    Menu.mainloop()
Main()

