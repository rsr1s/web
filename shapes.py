import turtle as u
import random
rs = u.Turtle
c = ["red", "blue", "green", "orange", "yellow","cyan","violet"]
u.speed(3)
u.bgcolor("black")

u.hideturtle()
u.goto(0,-100)

def num(number_of_side):

    angle = 360/number_of_side
    for i in range(number_of_side):
        u.forward(50)
        u.left(angle)


for a in range(3, 30):
    u.color(random.choice(c))
    num(a)

screen = u.Screen()
screen.exitonclick()
