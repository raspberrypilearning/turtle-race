#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for krok in range(15):
  write(krok, align='center')
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

red = Turtle()
red.color('red')
red.shape('turtle')

red.penup()
red.goto(-160, 100)
red.pendown()

for krok in range(10):
  red.right(36)

blue = Turtle()
blue.color('blue')
blue.shape('turtle')

blue.penup()
blue.goto(-160, 70)
blue.pendown()

for krok in range(72):
  blue.left(5)

green = Turtle()
green.shape('turtle')
green.color('turquoise')

green.penup()
green.goto(-160, 40)
green.pendown()

for krok in range(60):
  green.right(6)

yellow = Turtle()
yellow.shape('turtle')
yellow.color('yellow')

yellow.penup()
yellow.goto(-160, 10)
yellow.pendown()

for krok in range(30):
  yellow.left(12)

for hid in range(100):
  red.forward(randint(1,5))
  blue.forward(randint(1,5))
  green.forward(randint(1,5))
  yellow.forward(randint(1,5))
  
