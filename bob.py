import turtle
import random

random.seed()

def random_color():
    rgbl=[random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]    
    return tuple(rgbl)

t = turtle.Pen()
t.speed(-5)

turtle.colormode(255)
turtle.bgcolor("black")

for x in range(720):
    t.pencolor(random_color())
    t.width(x/500+1)
    t.forward(x)
    t.left(179)