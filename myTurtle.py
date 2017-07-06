from turtle import *
import math

#name your turtle
psyduck = Turtle()

#give him a starting position
psyduck.setposition(0,0)
psyduck.pendown()

#set my variables
numsides = int(input("How many sides do you want in your shape? "))
int_angle = 360 / int(numsides)
my_pen_color = input("What color do you want the shape border to be? ")
my_fill_color = input("What color do you want the inside of your shape to be? ")
my_pen_width = int(input("How wide do you want your pen to be? "))
my_pen_speed = int(input("How fast do you want the pen to go? "))

#Setting pen color
psyduck.pencolor(my_pen_color)

#Setting pen width
psyduck.width(my_pen_width)

#Setting fill color
psyduck.fillcolor(my_fill_color)

#Setting pen speed
psyduck.speed(my_pen_speed)

#Begin color fill
psyduck.begin_fill()

#Drawing the shape
for i in range (1, numsides + 1):
    psyduck.forward(50)
    psyduck.right(int_angle)

#End color fill
psyduck.end_fill()
psyduck.penup()
