import turtle
import random
wn = turtle.Screen()
wn.setup(600, 600)
wn.bgcolor("black")
s = turtle.Turtle()
r = 10

for i in range(15):
    s.circle(r*i)
    s.penup()
    s.sety(r*i*-1)
    s.setx(r*i*-1)
    s.pendown()
    j = random.random()
    k = random.random()
    l = random.random()
    s.pencolor((j, k, l))
s.penup()
s.home()
s.pendown()

for i in range(15):
    s.circle(r*i)
    s.penup()
    s.setx(r*i)
    s.sety(r*i*-1)
    s.pendown()
    j = random.random()
    k = random.random()
    l = random.random()
    s.pencolor((j, k, l))
s.hideturtle()
turtle.done()
