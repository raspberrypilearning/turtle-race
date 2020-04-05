#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for passa in range(15):
  write(passa, align='center')
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

vermella = Turtle()
vermella.color('red')
vermella.shape('turtle')

vermella.penup()
vermella.goto(-160, 100)
vermella.pendown()

for torn in range(10):
  vermella.right(36)

blava = Turtle()
blava.color('blue')
blava.shape('turtle')

blava.penup()
blava.goto(-160, 70)
blava.pendown()

for torn in range(72):
  blava.left(5)

verda = Turtle()
verda.shape('turtle')
verda.color('yellow')

verda.penup()
verda.goto(-160, 40)
verda.pendown()

for torn in range(60):
  verda.right(6)

groga = Turtle()
groga.shape('turtle')
groga.color('turquoise')

groga.penup()
groga.goto(-160, 10)
groga.pendown()

for torn in range(30):
  groga.left(12)

for torn in range(100):
  vermella.forward(randint(1,5))
  blava.forward(randint(1,5))
  verda.forward(randint(1,5))
  groga.forward(randint(1,5))
  