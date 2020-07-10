import turtle, random, time, sys

random.seed()

def random_color():
    rgbl=[random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]    
    return tuple(rgbl)

turtle.colormode(255)
turtle.bgcolor("black")

t = turtle.Pen()
t.speed(0)
sides = int(sys.argv[1])

for x in range (200):
    t.forward(x*3 / sides+x)
    t.left(360/sides+1)
    t.pencolor(random_color())

time.sleep(10)