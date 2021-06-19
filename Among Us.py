import turtle

win = turtle.getscreen()
im = turtle.Turtle()

body_color = 'red'
glass_color = 'skyblue'


def body():
    im.pensize(20)
    # im.speed(15)

    im.fillcolor(body_color)
    im.begin_fill()

    # right side
    im.right(90)
    im.forward(50)
    im.right(180)
    im.circle(40, -180)
    im.right(180)
    im.forward(200)

    # head curve
    im.right(180)
    im.circle(100, -180)

    # left side
    im.backward(20)
    im.left(15)
    im.circle(500, -20)
    im.backward(20)

    im.circle(40, -180)
    im.left(7)
    im.backward(50)

    # hip
    im.up()
    im.left(90)
    im.forward(10)
    im.right(90)
    im.down()
    im.right(240)
    im.circle(50, -70)

    im.end_fill()


def glass():
    im.up()
    im.right(230)
    im.forward(100)
    im.left(90)
    im.forward(20)
    im.right(90)

    im.down()
    im.fillcolor(glass_color)
    im.begin_fill()

    im.right(150)
    im.circle(90, -55)

    im.right(180)
    im.forward(1)
    im.right(180)
    im.circle(10, -65)
    im.right(180)
    im.forward(110)
    im.right(180)

    im.circle(50, -190)
    im.right(170)
    im.forward(80)

    im.right(180)
    im.circle(45, -30)

    im.end_fill()


def backpack():
    im.up()
    im.right(60)
    im.forward(100)
    im.right(90)
    im.forward(75)

    im.fillcolor(body_color)
    im.begin_fill()

    im.down()
    im.forward(30)
    im.right(255)

    im.circle(300, -30)
    im.right(260)
    im.forward(30)

    im.end_fill()


body()
glass()
backpack()

turtle.penup()
turtle.goto(50, -200)
turtle.pendown()
turtle.write('By Pallav', font=("Magenta Rose", 20))
turtle.done()
