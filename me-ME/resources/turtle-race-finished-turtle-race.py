#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for cam in range(15):
  write(cam, align='center')
  right(90)
  for rhif in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

coch = Turtle()
coch.color('red')
coch.shape('turtle')

coch.penup()
coch.goto(-160, 100)
coch.pendown()

for tro in range(10):
  coch.right(36)

glas = Turtle()
glas.color('blue')
glas.shape('turtle')

glas.penup()
glas.goto(-160, 70)
glas.pendown()

for tro in range(72):
  glas.left(5)

gwyrdd = Turtle()
gwyrdd.shape('turtle')
gwyrdd.color('yellow')

gwyrdd.penup()
gwyrdd.goto(-160, 40)
gwyrdd.pendown()

for tro in range(60):
  gwyrdd.right(6)

melyn = Turtle()
melyn.shape('turtle')
melyn.color('turquoise')

melyn.penup()
melyn.goto(-160, 10)
melyn.pendown()

for tro in range(30):
  melyn.left(12)

for tro in range(100):
  coch.forward(randint(1,5))
  glas.forward(randint(1,5))
  gwyrdd.forward(randint(1,5))
  melyn.forward(randint(1,5))
  