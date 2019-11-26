#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for passo in range(15):
  write(passo, align='center')
  right(90)
  for numero in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

vermelha = Turtle()
vermelha.color('red')
vermelha.shape('turtle')

vermelha.penup()
vermelha.goto(-160, 100)
vermelha.pendown()

for turn in range(10):
  vermelha.right(36)

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

amarela = Turtle()
amarela.shape('turtle')
amarela.color('yellow')

amarela.penup()
amarela.goto(-160, 10)
amarela.pendown()

for turn in range(30):
  amarela.left(12)

for turn in range(100):
  vermelha.forward(randint(1,5))
  azul.forward(randint(1,5))
  verde.forward(randint(1,5))
  amarela.forward(randint(1,5))
  
