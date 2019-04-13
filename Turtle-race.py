from turtle import *
import turtle
from random import randint
import random
from random import choice
import time

x=int(input("Masukkan panjang lapangan antara 200-1200:"))
B=20
A=25
y=(A*2)+(B*3)
goal=x/2-10


if 200<=x<=1200:

    ### warna random ###
    
    colors1=["blue", "black", "brown", "cyan"]
    colors2=["red", "yellow", "sandybrown", "orange"]
    colors3=["magenta", "purple", "pink", "rosybrown"]
    colors4=["beige", "turquoise", "green", "moccasin"]
    
    baa=random.choice(colors1)
    bii=random.choice(colors2)
    buu=random.choice(colors3)
    bee=random.choice(colors4)

    ### nama unik ###
    
    first_names1=("Dilan", "Milea", "1990", "Jangan")
    last_names1=("Rindu", "Berat", "Aku", "Saja")
    first_names2=("John", "Joe", "Joy", "Jonathan")
    last_names2=("Brown", "White", "Black", "Gray")
    first_names3=("Hana", "Bunga", "Flower", "Grass")
    last_names3=("Johnson", "Mikaelson", "Anderson", "Greyson")
    first_names4=("Altair", "Orion", "Antares", "Alva")
    last_names4=("Zeta", "Iota", "Upsilon", "Rho")

    la=random.choice(first_names1)+" "+random.choice(last_names1)
    li=random.choice(first_names2)+" "+random.choice(last_names2)
    lu=random.choice(first_names3)+" "+random.choice(last_names3)
    le=random.choice(first_names4)+" "+random.choice(last_names4)

    hideturtle() #Agar pointer turtlenya hilang

    ### Membuat lapangan balap ###

    penup() 
    goto(-(x/2),-(y/2)) #Supaya berada di tengah
    pendown()
    pencolor("black")
    forward(x)
    left(90)
    forward(y)
    left(90)
    forward(x)
    left(90)
    forward(y)
    penup()

    start=time.time() #Perhitungan elapsed time dimulai

    ba=Turtle()
    ba.color(baa)
    ba.shape("turtle")

    ba.penup()
    ba.goto(-(x/2)+25, 30) #koordinat untuk turtle kuning
    ba.pendown()

    bi=Turtle()
    bi.color(bii)
    bi.shape("turtle")

    bi.penup()
    bi.goto(-(x/2)+25, 10) #koordinat turtle hijau di bawa kuning 25pxl
    bi.pendown()

    bu=Turtle()
    bu.color(buu)
    bu.shape("turtle")

    bu.penup()
    bu.goto(-(x/2)+25, -10) #koordinar biru, jarak 25pxl
    bu.pendown()

    be=Turtle()
    be.color(bee)
    be.shape("turtle")

    be.penup()
    be.goto(-(x/2)+25, -30) #koordinat merah, jarak 25pxl
    be.pendown()

    ### Mengatur jalannya turtle ###

    while (ba.xcor()<=goal) and (bi.xcor()<=goal) and (bu.xcor()<=goal) and (be.xcor()<=goal):
        ba.forward(randint(1,15))
        ba.right(randint(-8,8))
        bi.forward(randint(1,15))
        bi.right(randint(-8,8))
        bu.forward(randint(1,15))
        bu.right(randint(-8,8))
        be.forward(randint(1,15))
        be.right(randint(-8,8))
        if ba.ycor()>=50:               #Jika melebihi batas lapangan 
            ba.right(randint(10,50))
            ba.forward(randint(1,15))
        elif ba.ycor()<=-50:
            ba.left(randint(10,50))
            ba.forward(randint(1,15))
        if bi.ycor()>=50:
            bi.right(randint(10,50))
            bi.forward(randint(1,15))
        elif bi.ycor()<=-50:
            bi.left(randint(10,50))
            bi.forward(randint(1,15))
        if bu.ycor()>=50:
            bu.right(randint(10,50))
            bu.forward(randint(1,15))
        elif bu.ycor()<=-50:
            bu.left(randint(10,50))
            bu.forward(randint(1,15))
        if be.ycor()>=50:
            be.right(randint(10,50))
            be.forward(randint(1,15))
        elif be.ycor()<=-50:
            be.left(randint(10,50))
            be.forward(randint(1,15))

    end=time.time() #Perhitungan waktu selesai

    ### Output Pemenang ###

    goto(0,-(y/2)-30) #Agar di bawah

    if ba.xcor()>x/2-10:
        pencolor(baa)
        turtle.write("The winner of the race is: "+la+"!", True, align="center", font=("arial", "12", "bold"))
    elif bi.xcor()>x/2-10:
        pencolor(bii)
        turtle.write("The winner of the race is: "+li+"!", True, align="center", font=("arial", "12", "bold"))
    elif bu.xcor()>x/2-10:
        pencolor(buu)
        turtle.write("The winner of the race is: "+lu+"!", True, align="center", font=("arial", "12", "bold"))
    else:
        pencolor(bee)
        turtle.write("The winner of the race is: "+le+"!", True, align="center", font=("arial", "12", "bold"))

    ### Output Waktu ###

    goto(0,-(y/2)-50) # agar di bawah pemenang
    pencolor("black")
    turtle.write("Time elapsed is: "+str(end-start)+" seconds", True, align="center", font=("arial", "10", "bold"))

else:
    print("Input yang Anda masukkan salah.") #Jika tidak diantara 200-1200
