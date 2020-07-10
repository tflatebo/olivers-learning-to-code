import turtle, random, time, sys

random.seed()

def random_color():
    rgbl=[random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]    
    return tuple(rgbl)

sides = int(sys.argv[1])
iterations = int(sys.argv[2])
wait = int(sys.argv[3])

turtle.colormode(255)
turtle.bgcolor("black")

t = turtle.Pen()
t.speed(0)

colors = []

for c in range(sides):
    colors.append(random_color())

for x in range(iterations):
    #t.forward(x*3 / sides+x)
    t.circle(x/2)
    t.left(360/sides+1)
    t.pencolor(colors[x % sides])

time.sleep(wait)