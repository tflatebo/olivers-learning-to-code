import turtle, random, time, sys

random.seed()

name = turtle.textinput("Enter your name", "What is your name?")

def random_color():
    rgbl=[random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]    
    return tuple(rgbl)

sides = 3
iterations = 100
wait = 5
font = "arial"

if (len(sys.argv) > 3):
    sides = int(sys.argv[1])
    iterations = int(sys.argv[2])
    wait = int(sys.argv[3])
    font = sys.argv[4]

turtle.colormode(255)
turtle.bgcolor("black")

t = turtle.Pen()
t.speed(0)

colors = []

for c in range(sides):
    colors.append(random_color())

for x in range(iterations):
    t.pencolor(colors[x % sides])
    t.penup()
    t.forward(x*sides)
    t.pendown()
    t.write(name, font = (font, int((x+sides)/sides), "bold"))
    t.left(92)
    

time.sleep(wait)