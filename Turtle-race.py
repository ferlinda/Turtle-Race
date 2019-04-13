from turtle import *
import turtle
from random import randint
import random
from random import choice
import time

x=650
B=20
A=25
y=(A*2)+(B*3)
goal=x/2-10

### warna random ###

colors1=["blue", "black", "brown", "cyan"]
colors2=["red", "yellow", "sandybrown", "orange"]
colors3=["magenta", "purple", "pink", "rosybrown"]
colors4=["beige", "turquoise", "green", "moccasin"]

baa=random.choice(colors1)
bii=random.choice(colors2)
buu=random.choice(colors3)
bee=random.choice(colors4)

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

## Meminta pilihan user ##

print("Daftar warna dari atas ke bawah")
print(baa)
print(bii)
print(buu)
print(bee)
print("\nPasang Taruhan")
usrone=input("Pilihan User 1: ")
usrtwo=input("Pilihan User 2: ")

### Mengatur jalannya turtle ###

while (ba.xcor()<=goal) and (bi.xcor()<=goal) and (bu.xcor()<=goal) and (be.xcor()<=goal):
	ba.forward(randint(4,15))
	bi.forward(randint(4,15))
	bu.forward(randint(4,15))
	be.forward(randint(4,15))

end=time.time() #Perhitungan waktu selesai

### Output Pemenang ###

goto(0,-(y/2)-30) #Agar di bawah

if ba.xcor()>x/2-10:
	pencolor(baa)
	turtle.write("The winner of the race is: "+baa+"!", True, align="center", font=("arial", "12", "bold"))
	winner=baa
elif bi.xcor()>x/2-10:
	pencolor(bii)
	turtle.write("The winner of the race is: "+bii+"!", True, align="center", font=("arial", "12", "bold"))
	winner=bii
elif bu.xcor()>x/2-10:
	pencolor(buu)
	turtle.write("The winner of the race is: "+buu+"!", True, align="center", font=("arial", "12", "bold"))
	winner=buu
else:
	pencolor(bee)
	turtle.write("The winner of the race is: "+bee+"!", True, align="center", font=("arial", "12", "bold"))
	winner=bee

### Output Waktu ###

goto(0,-(y/2)-50) # agar di bawah pemenang
pencolor("black")
turtle.write("Time elapsed is: "+str(end-start)+" seconds", True, align="center", font=("arial", "10", "bold"))

goto(0,-(y/2)-70) # agar di bawah pemenang
pencolor(winner)
if winner==usrone:
	turtle.write("User 1 menang", True, align="center", font=("arial", "10", "bold"))
elif winner==usrtwo:
	turtle.write("User 2 menang", True, align="center", font=("arial", "10", "bold"))
else:
	turtle.write("Draw", True, align="center", font=("arial", "10", "bold"))

