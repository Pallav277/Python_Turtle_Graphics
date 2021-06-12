import turtle

red = turtle.Turtle()  # Assigning "red" as the name of the turtle
red.getscreen().bgcolor('black')
red.color('red')
red.speed(0)

def curve(): # Method to draw curve
    for i in range(200): # To draw the curve step by step
        red.right(1)
        red.forward(1)

def heart():  # Method to draw full Heart
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()  # Left Curve
    red.left(120)
    curve()  # Right Curve
    red.forward(112)
    red.end_fill()

heart()
red.ht()  # Hiding Turtle
turtle.done()
