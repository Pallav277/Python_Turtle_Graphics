import turtle
from turtle import *
from time import sleep

colormode(255)
red = (204, 0, 51);
green = (1, 153, 52);
yellow = (253, 210, 10);
blue = (0, 153, 255)
r = 120
seth(-150)
up()

# RED
color(red)
begin_fill()
fd(r)
down()
right(90)
circle(-r, 120)
fd(r * 3 ** .5)
left(120)
circle(2 * r, 120)
left(60)
fd(r * 3 ** .5)
end_fill()

# GREEN

left(180)
color(green)
begin_fill()
fd(r * 3 ** .5)
left(120)
circle(2 * r, 120)
left(60)
fd(r * 3 ** .5)
left(180)
circle(-r, 120)
end_fill()

# YELLOW

left(180)
circle(r, 120)
color(yellow)
begin_fill()
circle(r, 120)
right(180)
fd(r * 3 ** .5)
right(60)
circle(-2 * r, 120)
right(120)
fd(r * 3 ** .5)
end_fill()

# BLUE

up()
left(98)
fd(r / 10)
seth(60)
color(blue)
down()
begin_fill()
circle(distance(0, 0))
end_fill()
ht()

turtle.penup()
turtle.pencolor('black')
turtle.goto(75, -300)
turtle.pendown()
turtle.write('By Pallav', font=("Magenta Rose", 20))
done()
