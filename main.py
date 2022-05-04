import turtle
from turtle import Turtle, Screen

tod = Turtle()


def move_forward():
    tod.forward(10)


def move_backward():
    tod.backward(10)


def rotate_cw():
    current_heading = tod.heading()
    current_heading += 10
    tod.setheading(current_heading)


def rotate_ccw():
    current_heading = tod.heading()
    current_heading -= 10
    tod.setheading(current_heading)


def clear():
    tod.clear()
    tod.pu()
    tod.home()
    tod.pd()

screen = Screen()
screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=rotate_cw)
screen.onkeypress(key='d', fun=rotate_ccw)
screen.onkeypress(key='c', fun=clear)
screen.exitonclick()
