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

roja = Turtle()
roja.color('red')
roja.shape('turtle')

roja.penup()
roja.goto(-160, 100)
roja.pendown()

for turn in range(10):
  roja.right(36)

azul = Turtle()
azul.color('blue')
azul.shape('turtle')

azul.penup()
azul.goto(-160, 70)
azul.pendown()

for turn in range(72):
  azul.left(5)

verde = Turtle()
verde.shape('turtle')
verde.color('green')

verde.penup()
verde.goto(-160, 40)
verde.pendown()

for turn in range(60):
  verde.right(6)

amarillo = Turtle()
amarillo.shape('turtle')
amarillo.color('yellow')

amarillo.penup()
amarillo.goto(-160, 10)
amarillo.pendown()

for turn in range(30):
  amarillo.left(12)

for turn in range(100):
  roja.forward(randint(1,5))
  azul.forward(randint(1,5))
  verde.forward(randint(1,5))
  amarillo.forward(randint(1,5))
  