import turtle

t = turtle.Turtle()

scr = turtle.Screen()
scr.bgcolor('black')
t.speed(0)

col = ("yellow", "red", "cyan", "green")

for i in range(400):
    t.pencolor(col[i%4])
    t.width(2)
    t.forward(i)
    t.right(89)
    t.forward(i*2)
    t.right(89)
