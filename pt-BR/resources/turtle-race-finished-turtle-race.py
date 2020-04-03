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

maria = Turtle()
maria.color('red')
maria.shape('turtle')

maria.penup()
maria.goto(-160, 100)
maria.pendown()

for turn in range(10):
  maria.right(36)

joao = Turtle()
joao.color('blue')
joao.shape('turtle')

joao.penup()
joao.goto(-160, 70)
joao.pendown()

for turn in range(72):
  joao.left(5)

antonio = Turtle()
antonio.shape('turtle')
antonio.color('green')

antonio.penup()
antonio.goto(-160, 40)
antonio.pendown()

for turn in range(60):
  antonio.right(6)

bianca = Turtle()
bianca.shape('turtle')
bianca.color('yellow')

bianca.penup()
bianca.goto(-160, 10)
bianca.pendown()

for turn in range(30):
  bianca.left(12)

for turn in range(100):
  maria.forward(randint(1,5))
  joao.forward(randint(1,5))
  antonio.forward(randint(1,5))
  bianca.forward(randint(1,5))
  
