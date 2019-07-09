import random
import turtle
from turtle import Turtle
import time

#Windows
win=turtle.Screen()
t=turtle.Pen()
t.forward(10)
win.title("TURTLE RACE")
win.bgcolor("forestgreen")
turtle.color("white")
turtle.speed()
turtle.penup()
turtle.setpos(-140,200)
turtle.write("TURTLE RACE", font=('Arial', 30))
turtle.pendown()

#Turtle 1
turtle1=Turtle()
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,100)
turtle1.pendown()



#Turtle 2
turtle2=Turtle()
turtle2.color("red")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,50)
turtle2.pendown()


#Turtle 3
turtle3=Turtle()
turtle3.color("blue")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,0)
turtle3.pendown()

#Turtle 4
turtle4=Turtle()
turtle4.color("orange")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-50)
turtle4.pendown()


