import turtle
import random
import time


t1 = turtle.Turtle()
t1.hideturtle()
t1.pensize(1)
t1.speed(0)


c=['red','blue','pink','orange','yellow','magenta','cyan']

time.sleep(5)
turtle.bgcolor("black")

t1.penup()
for u in range(80):
    
    t1.goto(-200,0)
    t1.pendown()
    colour = random.choice(c)
    t1.circle(45)
    t1.color(colour)
    t1.left(5)

t1.penup()
for u in range(80):
    
    t1.goto(200,-10)
    t1.pendown()
    colour = random.choice(c)
    t1.circle(45)
    t1.color(colour)
    t1.left(5)

t1.penup()
for u in range(80):
    
    t1.goto(-30,-300)
    t1.pendown()
    colour = random.choice(c)    
    t1.circle(45)
    t1.color(colour)
    t1.left(5)


t1.up()   
t1.goto(0,290)

t1.down()
t1.speed(0)
t1.hideturtle()

for a in range (80):
    ca = random.choice(c)
    t1.color(ca)
    t1.circle(45)
    t1.right(5)
    




t1.penup()
t1.goto(-50,-50)
t1.write("®§®",font=("Verdana",
    15,'normal'))


turtle.exitonclick()