import turtle as u
import random
import time
rs = u.Turtle
c = ["red", "blue", "green", "orange", "yellow" ]
d = [0, 90, 180, 270]
u.speed(10.5)

u.hideturtle()
time.sleep(5)
for i in range(1000):
    u.pensize(9)
    u.forward(20)
    u.setheading(random.choice(d))
    u.color(random.choice(c))

screen = u.Screen()
screen.exitonclick()
