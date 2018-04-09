#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for krok in range(15):
  write(krok, align='center')
  right(90)
  for liczba in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

czerwony = Turtle()
czerwony.color('red')
czerwony.shape('turtle')

czerwony.penup()
czerwony.goto(-160, 100)
czerwony.pendown()

for tura in range(10):
  czerwony.right(36)

niebieski = Turtle()
niebieski.color('blue')
niebieski.shape('turtle')

niebieski.penup()
niebieski.goto(-160, 70)
niebieski.pendown()

for tura in range(72):
  niebieski.left(5)

zolty = Turtle()
zolty.shape('turtle')
zolty.color('yellow')

zolty.penup()
zolty.goto(-160, 40)
zolty.pendown()

for tura in range(60):
  zolty.right(6)

turkusowy = Turtle()
turkusowy.shape('turtle')
turkusowy.color('turquoise')

turkusowy.penup()
turkusowy.goto(-160, 10)
turkusowy.pendown()

for tura in range(30):
  turkusowy.left(12)

for tura in range(100):
  czerwony.forward(randint(1,5))
  niebieski.forward(randint(1,5))
  zolty.forward(randint(1,5))
  turkusowy.forward(randint(1,5))
