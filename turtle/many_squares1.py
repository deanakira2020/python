from turtle import *

shape('turtle')

speed(0)

def square():
    for i in range(4):
        forward(100)
        rt(90)

def many_squares():
    for i in range (144):
        square()
        rt(5)

many_squares()
