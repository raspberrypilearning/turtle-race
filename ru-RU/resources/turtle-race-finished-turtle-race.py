#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for hod in range(15):
  write(hod, align='center')
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

krasny = Turtle()
krasny.color('red')
krasny.shape('turtle')

krasny.penup()
krasny.goto(-160, 100)
krasny.pendown()

for povorot in range(10):
  krasny.right(36)

siny = Turtle()
siny.color('blue')
siny.shape('turtle')

siny.penup()
siny.goto(-160, 70)
siny.pendown()

for povorot in range(72):
  siny.left(5)

zeleny = Turtle()
zeleny.shape('turtle')
zeleny.color('yellow')

zeleny.penup()
zeleny.goto(-160, 40)
zeleny.pendown()

for povorot in range(60):
  zeleny.right(6)

zhelty = Turtle()
zhelty.shape('turtle')
zhelty.color('turquoise')

zhelty.penup()
zhelty.goto(-160, 10)
zhelty.pendown()

for povorot in range(30):
  zhelty.left(12)

for povorot in range(100):
  krasny.forward(randint(1,5))
  siny.forward(randint(1,5))
  zeleny.forward(randint(1,5))
  zhelty.forward(randint(1,5))
  
