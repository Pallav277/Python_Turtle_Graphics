import turtle

turtle.bgcolor("black")
sq = turtle.Turtle()
sq.speed(10)

sq.color("white")
for i in range(500):
    sq.forward(i)
    sq.left(91)
