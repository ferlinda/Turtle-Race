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

### warna turtles ###

le="red"
gen="blue"
da="green"

hideturtle() #Agar pointer turtlenya hilang

### Membuat lapangan balap ###

penup() 
goto(-(x/2),-(y-200)) #Supaya berada di tengah
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
ba.color(le)
ba.shape("turtle")

ba.penup()
ba.goto(-(x/2)+25, 180)
ba.pendown()

bi=Turtle()
bi.color(gen)
bi.shape("turtle")

bi.penup()
bi.goto(-(x/2)+25, 150) 
bi.pendown()

bu=Turtle()
bu.color(da)
bu.shape("turtle")

bu.penup()
bu.goto(-(x/2)+25, 120) 
bu.pendown()

## Meminta pilihan user ##

print("Daftar warna dari atas ke bawah: le-gen-da")
print("\nPasang Taruhan")
print("Player 1")
usrone_first=input("1: ")
usrone_second=input("2: ")
usrone_third=input("3: ")
bet1=int(input("Bet: "))
print("Player 2")
usrtwo_first=input("1: ")
usrtwo_second=input("2: ")
usrtwo_third=input("3: ")
bet2=int(input("Bet: "))

### Mengatur jalannya turtle ###

while (ba.xcor()<=goal) and (bi.xcor()<=goal) and (bu.xcor()<=goal):
	ba.forward(randint(5,15))
	bi.forward(randint(5,15))
	bu.forward(randint(5,15))

end=time.time() #Perhitungan waktu selesai

### Output Pemenang ###

goto(0,(y/2)) #Agar di bawah

nilai1=0
nilai2=0

if ba.xcor()>x/2-10:
	pencolor(le)
	first="le"
	if bi.xcor()>bu.xcor():
		second="gen"
		third="da"
		turtle.write("Juara 1 = le; Juara 2 = gen; Juara 3: da", True, align="center", font=("arial", "12", "bold"))
	else:
		second="da"
		third="gen"
		turtle.write("Juara 1 = le; Juara 2 = da; Juara 3: gen", True, align="center", font=("arial", "12", "bold"))
elif bi.xcor()>x/2-10:
	pencolor(gen)
	first="gen"
	if ba.xcor()>bu.xcor():
		second="le"
		third="da"
		turtle.write("Juara 1 = gen; Juara 2 = le; Juara 3: da", True, align="center", font=("arial", "12", "bold"))
	else:
		second="da"
		third="le"
		turtle.write("Juara 1 = gen; Juara 2 = da; Juara 3: le", True, align="center", font=("arial", "12", "bold"))
elif bu.xcor()>x/2-10:
	pencolor(da)
	first=da
	if ba.xcor()>bi.xcor():
		second="le"
		third="gen"
		turtle.write("Juara 1 = da; Juara 2 = le; Juara 3: gen", True, align="center", font=("arial", "12", "bold"))
	else:
		second="gen"
		third="le"
		turtle.write("Juara 1 = da; Juara 2 = gen; Juara 3: le", True, align="center", font=("arial", "12", "bold"))

### Perhitungan Nilai ###	
	
if usrone_first==first:
	nilai1+=1
if usrone_second==second:
	nilai1+=1
if usrone_third==third:
	nilai1+=1
if usrtwo_first==first:
	nilai2+=1
if usrtwo_second==second:
	nilai2+=1
if usrtwo_third==third:
	nilai2+=1
			

goto(0,(y/2)-20) # agar di bawah pemenang
pencolor("black")
if nilai1>nilai2:
	turtle.write("Player 1 menang", True, align="center", font=("arial", "10", "bold"))
elif nilai1<nilai2:
	turtle.write("Player 2 menang", True, align="center", font=("arial", "10", "bold"))
else:
	turtle.write("Draw", True, align="center", font=("arial", "10", "bold"))

if nilai1>nilai2:
	bet1+=bet2
	bet2=0
elif nilai1<nilai2:
	bet2+=bet1
	bet1=0
	
print("Saldo Player 1 :", str(bet1))
print("Saldo Player 2 :", str(bet2))
