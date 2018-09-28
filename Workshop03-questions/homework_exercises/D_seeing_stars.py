#--------------------------------------------------------------------
#
# Seeing stars
#
# In the lecture demonstration program "stars and stripes" we saw
# how function definitions allowed us to reuse a function that
# drew a star but was parameterised so that specific characteristics
# of the star could be changed each time.  As a further exercise in
# "parameterisation", develop a program that uses this function to
# draw a hundred stars on the screen.  Each star should be of
# a random size and colour and should appear in a random location.
# You can find a list of all the colours supported by Python at:
# http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
#
# Hint: This is very similar to last week's Starry, Starry Night
# exercise, so you can use your solution to that as a starting
# point if you're stuck.
#

colors = ["blue", "green", "yellow", "red", "orange", "purple"];
             

# Import the function to draw stars (make sure a copy of file
# flag_elements.py is in the same folder as this one)
from flag_elements import star

# Import the turtle graphics and random functions
from turtle import *
from random import *

# Set the drawing speed, if necessary
speed("fastest")
penup();

## DEVELOP YOUR SOLUTION HERE
for step in range(100) :
    color('black');
    speed('fastest');
    goto(randint(-Screen().screensize()[0], Screen().screensize()[0]), randint(-Screen().screensize()[1], Screen().screensize()[1]));
    star(uniform(1, 10), colors[int(uniform(0, len(colors) - 1))]);

# Exit gracefully
hideturtle()
done()
