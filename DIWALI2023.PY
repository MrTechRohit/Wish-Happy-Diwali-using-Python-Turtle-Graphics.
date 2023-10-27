#_________ WELCOME ALL OF YOU ON COMPUTER SOFT SKILLS CHANNEL __________

#........................ WISH HAPPY DIWALI USING PYHON TURTLE GRAPHICS ......................


import turtle
import random
import colorsys

# Turtle Window
wn = turtle.Screen()
wn.setup(800,700)
wn.title("Computer Soft Skills: HAPPY DIWALI")

turtle.bgcolor('lightcyan')
turtle.tracer(2)
t=turtle.Turtle()
t.speed(10)
t.hideturtle()
t.pensize(15)
hue=0.5

#DRAW LETTER
#Draw H

t.color("RED")
t.penup()
t.backward(250)
t.left(90)
t.pendown()
t.forward(100)
t.backward(50)
t.right(90)
t.forward(45)
t.left(90)
t.forward(45)
t.backward(100)
t.right(90)

#Draw A
t.color("blue")
t.penup()
t.forward(30)
t.left(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(180)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)

#draw p
t.color("green")
t.penup()
t.forward(30)
t.left(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(180)

#draw P
t.color("purple")
t.penup()
t.forward(80)
t.left(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(180)

#Draw Y
t.color("orangered")
t.penup()
t.forward(90)
t.left(90)
t.pendown()
t.forward(75)
t.left(90)
t.forward(30)
t.right(90)
t.forward(30)
t.backward(30)
t.right(90)
t.forward(60)
t.left(90)
t.forward(30)
t.right(90)


#Draw D
t.color("orange")
t.penup()
t.goto(170,-150)
t.backward(470)
t.left(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.left(180)

#Draw I
t.color("red")
t.penup()
t.goto(210,-70)
t.backward(430)
t.right(90)
t.pendown()
t.forward(100)
t.left(90)

#Draw W
t.color("green")
t.penup()
t.goto(220,-60)
t.backward(400)
t.right(90)
t.pendown()
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(30)
t.left(90)
t.forward(100)
t.right(90)


#Draw A
t.color("magenta")
t.penup()
t.goto(325,-160)
t.backward(370)
t.left(90)
t.pendown()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.right(90)

#Draw L
t.color("crimson")
t.penup()
t.goto(-340,-60)
t.backward(330)
t.left(90)
t.pendown()
t.forward(100)
t.left(90)
t.forward(50)
t.right(90)

#Draw I
t.color("blue")
t.penup()
t.goto(80,-450)
t.backward(300)
t.left(180)
t.pendown()
t.forward(100)
t.right(90)

#_______________________________________
#draw diya
t.pensize(4)
t.speed(5)
t.pencolor("red")
t.fillcolor("sienna")
t.begin_fill()

t.penup()
t.goto(90,0)
t.pendown()
t.forward(250)
t.left(90)
t.circle(125, -180)
t.end_fill()


#Diya light
t.up()
t.pendown()
t.pensize(2)
t.goto(200,0)
t.pencolor("orange")
t.fillcolor("gold")
t.begin_fill()
t.right(20)
t.forward(-65)
t.right(-20)
t.forward(-30)
t.left(20)
t.forward(-65)

t.right(40)
t.forward(65)
t.right(-20)
t.forward(30)
t.left(20)
t.forward(65)
t.end_fill()

#___________________________________________
#___CRACKERS_______________

for i in range (50):
     x=random.randint(-400,500)
     y=random.randint(-200,450)
     z=random.randint(-300,600)
     t.pensize(1)
     t.penup()
     t.goto(x,y)
     t.pendown()

     size=random.randint(10,100)

     for i in range(36):
          color=colorsys.hsv_to_rgb(hue,1,1)
          t.pencolor(color)
          t.fd(size)
          t.bk(size)
          t.lt(10)
          hue +=0.01

turtle.done()









