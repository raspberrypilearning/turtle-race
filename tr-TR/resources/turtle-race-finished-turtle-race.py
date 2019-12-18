#!/bin/python3
# translated by Volkan ÇEVİK into Turkish

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for kademe in range(15):
  write(kademe, align='center')
  right(90)
  for rakam in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

ipek = Turtle()
ipek.color('red')
ipek.shape('turtle')

ipek.penup()
ipek.goto(-160, 100)
ipek.pendown()

for sira in range(10):
  ipek.right(36)

ceyda = Turtle()
ceyda.color('blue')
ceyda.shape('turtle')

ceyda.penup()
ceyda.goto(-160, 70)
ceyda.pendown()

for sira in range(72):
  ceyda.left(5)

volkan = Turtle()
volkan.shape('turtle')
volkan.color('yellow')

volkan.penup()
volkan.goto(-160, 40)
volkan.pendown()

for sira in range(60):
  volkan.right(6)

gulsen = Turtle()
gulsen.shape('turtle')
gulsen.color('turquoise')

gulsen.penup()
gulsen.goto(-160, 10)
gulsen.pendown()

for sira in range(30):
  gulsen.left(12)

for sira in range(100):
  ipek.forward(randint(1,5))
  ceyda.forward(randint(1,5))
  volkan.forward(randint(1,5))
  gulsen.forward(randint(1,5))
  