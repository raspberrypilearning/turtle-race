#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for stap in range(15):
  write(stap, align='center')
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

rood = Turtle()
rood.color('red')
rood.shape('turtle')

rood.penup()
rood.goto(-160, 100)
rood.pendown()

for draai in range(10):
  rood.right(36)

blauw = Turtle()
blauw.color('blue')
blauw.shape('turtle')

blauw.penup()
blauw.goto(-160, 70)
blauw.pendown()

for draai in range(72):
  blauw.left(5)

groen = Turtle()
groen.shape('turtle')
groen.color('geel')

groen.penup()
groen.goto(-160, 40)
groen.pendown()

for draai in range(60):
  groen.right(6)

geel = Turtle()
geel.shape('turtle')
geel.color('turquoise')

geel.penup()
geel.goto(-160, 10)
geel.pendown()

for draai in range(30):
  geel.left(12)

for draai in range(100):
  rood.forward(randint(1,5))
  blauw.forward(randint(1,5))
  groen.forward(randint(1,5))
  geel.forward(randint(1,5))
  
