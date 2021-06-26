import turtle
import math

kalam = turtle.Turtle()
kalam.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")
kalam.color("white")

k = 20

kalam.left(90)
kalam.penup()
kalam.goto(-7 * k, 0)
kalam.pendown()

for a in range(-7 * k, -3 * k, 1):
    x = a / k
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    kalam.goto(a, y * k)

for a in range(-3 * k, -1 * k - 1, 1):
    x = a / k
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    kalam.goto(a, y * k)

kalam.goto(-1 * k, 3 * k)
kalam.goto(int(-0.5 * k), int(2.2 * k))
kalam.goto(int(0.5 * k), int(2.2 * k))
kalam.goto(1 * k, 3 * k)
print("Batman Logo with Python Turtle")
for a in range(1 * k + 1, 3 * k + 1, 1):
    x = a / k
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    kalam.goto(a, y * k)

for a in range(3 * k + 1, 7 * k + 1, 1):
    x = a / k
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    kalam.goto(a, y * k)

for a in range(7 * k, 4 * k, -1):
    x = a / k
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    kalam.goto(a, y * k)

for a in range(4 * k, -4 * k, -1):
    x = a / k
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    kalam.goto(a, y * k)

for a in range(-4 * k - 1, -7 * k - 1, -1):
    x = a / k
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    kalam.goto(a, y * k)

kalam.penup()
kalam.penup()
kalam.goto(25, -150)
kalam.pendown()
kalam.write('By Pallav', font=("Magenta Rose", 20))
turtle.done()
