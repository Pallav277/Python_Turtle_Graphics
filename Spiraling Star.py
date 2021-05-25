import turtle
import random

sp = turtle.Turtle()
col = ["red", "blue", "white", "green", "yellow"]

scr = turtle.Screen()
scr.bgcolor("black")
sp.pensize(3)

for i in range(40):
    sp.color(random.choice(col))
    sp.forward(i * 10)
    sp.right(144)
