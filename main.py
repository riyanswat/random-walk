from random import choice, randrange, randint
import turtle as t
RANGE = 500


s = t.Screen()

tim = t.Turtle()
t.colormode(255)
tim.pensize(15)
tim.speed(0)

def randcolor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


for i in range(RANGE):
    tim.color(randcolor())
    tim.circle(30, 180) # add a third argument i.e. 2, 3 for beautiful patterns
    tim.setheading(randrange(0, 271, 90))

s.exitonclick()
