from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(16):
    write(step, align='center')
    right(90)
    forward(10)
    for i in range(11):
        pendown()
        forward(10) 
        penup()
        forward(5)
    backward(175) 
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

eve = Turtle()
eve.color('yellow')
eve.shape('turtle')

eve.penup()
eve.goto(-160, 40)
eve.pendown()

kai = Turtle()
kai.color('green')
kai.shape('turtle')

kai.penup()
kai.goto(-160, 10)
kai.pendown()

for turn in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    eve.forward(randint(1, 5))
    kai.forward(randint(1, 5))