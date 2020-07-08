import turtle, random, time

random.seed()

def random_color():
    rgbl=[random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]    
    return tuple(rgbl)

t = turtle.Pen()
t.speed(-5)

turtle.colormode(255)
turtle.bgcolor("black")

for x in range(1000):
    t.pencolor(random_color())
    t.width(x/200+1)
    t.forward(x)
    t.left(179)

time.sleep(60)