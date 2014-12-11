import turtle
import random

wn = turtle.Screen()
kiwi = turtle.Turtle()

wn.bgcolor("grey")

colours = ["cyan", "purple", "white", "black"]

for i in range(10):
    for i in range(4):
        kiwi.color(random.choice(colours))
        kiwi.forward(100)
        kiwi.right(90)
    kiwi.right(36)

wn.exitonclick()
