# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining method to draw a colored circle with a dynamic radius
def ring(col, rad):

	pen.fillcolor(col)
	pen.begin_fill()
	pen.circle(rad)
	pen.end_fill()

# Draw first ear
pen.up()
pen.setpos(-70, 140)
pen.down
ring('black', 30)

# Draw second ear
pen.up()
pen.setpos(70, 140)
pen.down()
ring('black', 30)

# Draw face
pen.up()
pen.setpos(0, 20)
pen.down()
ring('white', 80)


# Draw first eye
pen.up()
pen.setpos(-25, 95)
pen.down
ring('black', 16)

# Draw second eye
pen.up()
pen.setpos(25, 95)
pen.down()
ring('black', 16)

# Draw first eye
pen.up()
pen.setpos(-24, 97)
pen.down()
ring('white', 8)

# Draw second eye
pen.up()
pen.setpos(24, 97)
pen.down()
ring('white', 8)

# Draw nose
pen.up()
pen.setpos(0, 60)
pen.down
ring('black', 10)

# Draw mouth
pen.up()
pen.setpos(0, 60)
pen.down()
pen.right(90)
pen.circle(10, 180)
pen.up()
pen.setpos(0, 60)
pen.down()
pen.left(360)
pen.circle(10, -180)
pen.hideturtle()
