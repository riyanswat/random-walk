from random import choice, randrange, randint
import turtle
RANGE = 500


s = turtle.Screen()

t = turtle.Turtle()
turtle.colormode(255)
t.pensize(15)
t.speed(0)

def randcolor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


for i in range(RANGE):
    t.color(randcolor())
    t.circle(30, 180) # add a third argument i.e. 2, 3 for beautiful patterns
    t.setheading(randrange(0, 271, 90))

s.exitonclick()
