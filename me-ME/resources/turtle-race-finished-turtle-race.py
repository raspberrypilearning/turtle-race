#!/bin/python3


from turtle import *

from random import
randint

speed(0)

penup()

goto(-140, 140)


for korak in range(15):
 
  write(korak, align='center')

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


crvena = Turtle()

crvena.color('red')

crvena.shape('turtle')


crvena.penup()

crvena.goto(-160, 100)

crvena.pendown()


for krug in range(10):
  
crvena.right(36)


plava = Turtle()

plava.color('blue')

plava.shape('turtle')


plava.penup()

plava.goto(-160, 70)

plava.pendown()


for krug in range(72):
  
plava.left(5)


zelena = Turtle()

zelena.shape('turtle')

zelena.color('yellow')


zelena.penup()

zelena.goto(-160, 40)

zelena.pendown()


for krug in range(60):
  
zelena.right(6)


zuta = Turtle()

zuta.shape('turtle')

zuta.color('turquoise')


zuta.penup()

zuta.goto(-160, 10)

zuta.pendown()


for krug in range(30):

zuta.left(12)


for krug in range(100):
  
crvena.forward(randint(1,5))

plava.forward(randint(1,5))

zelena.forward(randint(1,5))

zuta.forward(randint(1,5))
  