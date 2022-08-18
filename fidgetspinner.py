# import turtle
# t1 = turtle.Turtle()
# turtle.done()
from turtle import *
turn = 0
def spinner():
    clear()
    angle = turn/10
    right(angle)
    print("spinner")
    forward(100)
    dot(120, "green")
    back(100)
    right(120)
    forward(100)
    dot(120, "blue")
    back(100)
    right(120)
    forward(100)
    dot(120, "yellow")
    back(100)
    right(120)
    update()
def animate():
    print("animate")
    spinner()
    ontimer(animate, 20)
def flick():
    print("flick")
    global turn
    turn = turn+10
    print(turn)

setup(620, 620, 0, 0)
tracer(False)
width(20)
onkey(flick, "space")
listen()
animate()
done()
