import turtle
import random

random.seed()

colors=['red','purple','blue',
        'green','yellow','orange']

t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(colors[random.randrange(0,5)])
    t.width(x/10+1)
    t.forward(x)
    t.left(40)