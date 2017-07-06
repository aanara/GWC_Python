from turtle import *
import math

#name your turtle
tentacool = Turtle()

#set my variables
radius = int(input("What radius circle do you want? "))
my_pen_color = input("What color do you want the shape border to be? ")
my_fill_color = input("What color do you want the inside of your shape to be? ")
my_pen_width = int(input("How wide do you want your pen to be? "))
my_pen_speed = int(input("How fast do you want the pen to go? "))

#give him a starting position
tentacool.setposition(0,0)

#pen down
tentacool.pendown()

#Setting pen color
tentacool.pencolor(my_pen_color)

#Setting pen width
tentacool.width(my_pen_width)

#Setting fill color
tentacool.fillcolor(my_fill_color)

#Setting pen speed
tentacool.speed(my_pen_speed)

#Begin color fill
tentacool.begin_fill()

#drawing circle
tentacool.circle(radius)

#End color fill
tentacool.end_fill()

#pen up
tentacool.penup()
