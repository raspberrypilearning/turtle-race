import turtle
import random

t = turtle.Turtle()
t.penup()
t.goto(-160, 140)
t.right(90)
x, y = t.position()

for step in range(16):
    if step != 0 :
        t.write(step, align='center')
        for n in range(8):
            t.penup()
            t.forward(10)
            t.pendown()
            t.forward(10)
    else :
        t.forward(10)
        t.pendown()
        t.forward(150)
    x = x + 20
    t.penup()
    t.goto(x, y)
t.hideturtle()

one = turtle.Turtle()
one.shape('turtle')
one.color('red')
one.penup()
one.goto(-180, 100)
one.right(360)
one.pendown()

two = turtle.Turtle()
two.shape('turtle')
two.color('yellow')
two.penup()
two.goto(-180, 70)
two.right(360)
two.pendown()

three = turtle.Turtle()
three.shape('turtle')
three.color('green')
three.penup()
three.goto(-180, 40)
three.right(360)
three.pendown()

four = turtle.Turtle()
four.shape('turtle')
four.color('blue')
four.penup()
four.goto(-180, 10)
four.right(360)
four.pendown()

r = []
d = [0, 0, 0, 0]
while(True):
    for i in range(4):
        ran = random.randint(1,5)
        r.append(ran)
        d[i] = d[i] + ran
    one.forward(r[0])
    two.forward(r[1])
    three.forward(r[2])
    four.forward(r[3])
    r = []
    if d[0] >= 320 or d[1] >= 320 or d[2] >= 320 or d[3] >= 320:
        break

turtle.done()