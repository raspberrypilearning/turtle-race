#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for paso in range(15):
  write(paso, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

rojo = Turtle()
rojo.color('red')
rojo.shape('turtle')

rojo.penup()
rojo.goto(-160, 100)
rojo.pendown()

for giro in range(10):
  rojo.right(36)

azul = Turtle()
azul.color('blue')
azul.shape('turtle')

azul.penup()
azul.goto(-160, 70)
azul.pendown()

for giro in range(72):
  azul.left(5)

verde = Turtle()
verde.shape('turtle')
verde.color('turquoise')

verde.penup()
verde.goto(-160, 40)
verde.pendown()

for giro in range(60):
  verde.right(6)

amarillo = Turtle()
amarillo.shape('turtle')
amarillo.color('yellow')

amarillo.penup()
amarillo.goto(-160, 10)
amarillo.pendown()

for giro in range(30):
  amarillo.left(12)

for giro in range(100):
  rojo.forward(randint(1,5))
  azul.forward(randint(1,5))
  verde.forward(randint(1,5))
  amarillo.forward(randint(1,5))
  