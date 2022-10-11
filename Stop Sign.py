#Gillian Bedward
#Stop Sign
import math
import turtle
#Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10
#Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
#Calculate the diameter of the octagon
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)
#Initialize the turtle
#Move the turtle to the starting point.
#Draw the octagon.
for x in range (8):
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.pensize(10)
    turtle.color("red")
    turtle.speed(100)
    turtle.forward(100)
    turtle.right(45)
    turtle.end_fill()
#Display 'STOP'
turtle.write("STOP", move=True, align="center", font=("Times New Roman",50,"normal"))
