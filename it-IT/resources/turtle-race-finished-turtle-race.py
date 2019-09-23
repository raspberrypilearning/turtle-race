#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for linea in range(15):
  write(linea, align='center')
  right(90)
  for n in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

rosso = Turtle()
rosso.color('red')
rosso.shape('turtle')

rosso.penup()
rosso.goto(-160, 100)
rosso.pendown()

for giro in range(10):
  rosso.right(36)

blu = Turtle()
blu.color('blue')
blu.shape('turtle')

blu.penup()
blu.goto(-160, 70)
blu.pendown()

for giro in range(72):
  blu.left(5)

giallo = Turtle()
giallo.shape('turtle')
giallo.color('yellow')

giallo.penup()
giallo.goto(-160, 40)
giallo.pendown()

for giro in range(60):
  giallo.right(6)

turchese = Turtle()
turchese.shape('turtle')
turchese.color('turquoise')

turchese.penup()
turchese.goto(-160, 10)
turchese.pendown()

for giro in range(30):
  turchese.left(12)

for turno in range(100):
  rosso.forward(randint(1,5))
  blu.forward(randint(1,5))
  giallo.forward(randint(1,5))
  turchese.forward(randint(1,5))
  
