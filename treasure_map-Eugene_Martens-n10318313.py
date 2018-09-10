
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10318313
#    Student name: Eugene Martens
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():
    
    # Set up the drawing window with enough space for the grid and
    # legend
    setup(window_width, window_height)
    setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    bgcolor('light grey')

    # Get ready to draw the grid
    penup()
    color('slate grey')
    width(2)

    # Draw the horizontal grid lines
    setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(0, y_coord)
        pendown()
        forward(num_squares * grid_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(x_coord, 0)
        pendown()
        forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_coord, y_offset)
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_offset, y_coord + y_offset)
        write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    #goto((num_squares * grid_size) + margin, (num_squares * grid_size) // 2)
    #write('    Put your legend here', align = 'left',
          #font=('Arial', 24, 'normal'))    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Top left', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in IFB104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', choice(starting_points), randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(randint(0, 19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.
#

#Draw Text, and reset to centre
def write_text(text, alignment) :
    saveCoord = xcor(), ycor(); 
    setheading(270);
    forward(10);
    write(text, align = alignment , font=('Arial', 24, 'normal'));
    goto(saveCoord);

#TDA
def draw_line_left():
    saveCoord = xcor(), ycor(); 
    setheading(180);
    forward(50);
    setheading(270);
    forward(50);
    pendown();
    color('gray');
    forward(100);
    penup();
    goto(saveCoord);

#TDA
def draw_line_right():
    pendown();
#TDA
def draw_line_down():
    pendown();
#TDA
def draw_line_top():
    pendown();

#combing forward and direction functions
    
def move_towards(direction, steps) :
    setheading(direction);
    forward(steps);

#designate 2 points and create an arc with theta angle
def make_arc(a, b, theta):

    distance = b - a;
    setheading(direction);
    forward(steps);

#Creates a circle
#stamps with a specificed color
#and resets turtle
def oval_stamp(stretch_w, strech_l, pen_color):
    color(pen_color);
    shape("circle");
    shapesize(stretch_w, strech_l, 2);
    stamp();
    shape('arrow');
    shapesize(1,1,1);
    color('black');

#Goes to 4 diffrent points and
#fills if fill is set to true
def draw_quad(p0, p1, p2, p3, fill = True):
    if fill : begin_fill();
    move_towards(p0[0], p0[1]);
    move_towards(p1[0], p1[1]);
    move_towards(p2[0], p2[1]);
    move_towards(p3[0], p3[1]);
    if fill: end_fill();
    
#Draw Bucket, calling it legend_0
#for more generic approuch
def draw_legend_0():
    saveCoord = xcor(), ycor(); 


    #Create Left Side
    fillcolor('gray');
    move_towards(90, 35);
    begin_fill();
    move_towards(180, 49);
    move_towards(285, 80);
    move_towards(0, 30);
    end_fill();
    goto(saveCoord);

    #Create Right Side
    move_towards(90, 35);
    begin_fill();
    move_towards(180, -49);
    move_towards(255, 80);
    move_towards(0, -30);
    end_fill();
    goto(saveCoord);
    

    #move_towards(270, 70);
    #oval_stamp(3, 'grey');
    setheading(0);
    
   # dot(50);
    penup();
    color('black');

    #Create inner bucket oval
    move_towards(90, 35);
    oval_stamp(4.6, 1, 'black');

    #Create bucket water oval
    move_towards(270, 2);
    oval_stamp(4.4, .8, 'lightblue');

    #Create bucket bottom oval
    move_towards(270, 70);
    oval_stamp(2.8, 1, 'gray');
    
    goto(saveCoord);
    
def draw_legend_1():
    saveCoord = xcor(), ycor();

    #Draw Handle
    move_towards(45, 50);
    pendown();
    pensize(5);
    color('burlywood4');
    move_towards(225, 80);
    penup();
    move_towards(135, 20);
    pendown();


    #turn off tracing, ull thank me later
    #and draw bristles
    tracer(False);
    
    for bristle in range(40):
        pensize(4);
        color('burlywood2');
        move_towards(225, 6);
        move_towards(45, 6);
        color('burlywood4');
        pensize(9);
        move_towards(315, 1);
    tracer(True);
    
    penup();

    color('black');
    penup();
    setheading(0);
    goto(saveCoord);


#Draw Legen 2, Or Overalls in this case    
def draw_legend_2():
    saveCoord = xcor(), ycor();
    penup();
    color('darkblue');
    move_towards(180, 25);
    move_towards(90, 10);

    #Draw Quad, taking in 4 points
    #each point is a directiion and steps
    # [270, 40] is in drection 270 go 40 steps
    # and supply 4 points to create quad
    #left it as this incase we dont want to create perfect
    #squares and rectangles
    draw_quad([270, 50], [0, 50], [90, 50], [180, 50]);
    goto(saveCoord);

#---------------------- Strap Left -----------------------------------------#
    move_towards(90, 10);
    move_towards(180, 25);
    begin_fill();

    move_towards(90, 30);
    move_towards(0, 7);
    move_towards(270,30);
    end_fill();
    goto(saveCoord);
#---------------------- Strap Left -----------------------------------------#
    
#---------------------- Buckle Left -----------------------------------------#
    move_towards(90, 10);
    move_towards(180, 25);

    move_towards(90, 15);
    move_towards(180, 1);
    color('grey73');
    draw_quad([270, 8], [0, 10], [90, 8], [180, 10]);
    color('darkblue');

    goto(saveCoord);
#---------------------- Buckle Left -----------------------------------------#

#---------------------- Strap Right -----------------------------------------#   
    move_towards(90, 10);
    move_towards(0, 25);
    begin_fill();

    move_towards(90, 30);
    move_towards(180, 7);
    move_towards(270,30);
    end_fill();
    
    penup();
    goto(saveCoord);

#---------------------- Strap Right -----------------------------------------#
    
#---------------------- Buckle Right -----------------------------------------#
    move_towards(90, 10);
    move_towards(0, 25);

    move_towards(90, 15);
    move_towards(0, 1);
    color('grey73');
    draw_quad([270, 8], [180, 10], [90, 8], [0, 10]);
    color('darkblue');

    goto(saveCoord);
#---------------------- Buckle Right -----------------------------------------#
    

#---------------------- Pouch -----------------------------------------#
    

    color('lightblue');
    move_towards(180, 15);
    move_towards(90, -5);

    draw_quad([270, 20], [0, 31], [90, 20], [180, 31]);

    #reset to centre of current
    color('black');
    penup();
    setheading(0);
    goto(saveCoord);
#---------------------- Pouch -----------------------------------------#
    
#---------------------- Pouch Lip-----------------------------------------#
    
    color('DarkCyan');
    move_towards(180, 20);
    move_towards(90, 0);

    draw_quad([270, 7], [0, 40], [90, 7], [180, 40]);
    
    penup();
    goto(saveCoord);
#---------------------- Pouch Lip-----------------------------------------#

#---------------------- Over Side Left-----------------------------------------#
        
    color('darkblue');

    begin_fill()
    move_towards(180, 25);
    q_store = xcor(), ycor();
    #pendown();
    move_towards(240, 12);
    move_towards(270, 29);
    move_towards(0, 10);
    goto(q_store);
    end_fill();
    penup();
    goto(saveCoord);
#---------------------- Over Side Left-----------------------------------------#
        

#---------------------- Over Side Right-----------------------------------------#
        
    
    color('darkblue');

    begin_fill()
    move_towards(180, -25);
    q_store = xcor(), ycor();
    #pendown();
    move_towards(300, 12);
    move_towards(270, 29);
    move_towards(0, -10);
    goto(q_store);
    end_fill();

    #reset to centre of current
    color('black');
    penup();
    setheading(0);
    goto(saveCoord);
#---------------------- Over Side Right-----------------------------------------#
        
   
#Creating Legend 3 Token, in this case Hat    
def draw_legend_3():
#-------------------- Hat Lip -------------
    saveCoord = xcor(), ycor();
    move_towards(90, -20);
    move_towards(180, 18);
    setheading(90);
    oval_stamp(3.0, 1, 'burlywood3');
    goto(saveCoord);
#-------------------- Hat Lip  -------------

#-------------------- Hat Middle  -------------
    fillcolor('burlywood4');
    begin_fill();
    move_towards(180, 17);
    move_towards(90, -18);
    move_towards(180, -64);
    move_towards(90, 18);
    end_fill();
    goto(saveCoord);
#-------------------- Hat Middle  -------------

#-------------------- Hat Bottom  -------------    
    move_towards(90, 0);
    move_towards(180, -15);
    setheading(90);
    oval_stamp(3.0, 1, 'burlywood4');
    goto(saveCoord);
#-------------------- Hat Bottom  -------------

#-------------------- Hat Top  ------------- 
    move_towards(90, -20);
    move_towards(180, -15);
    setheading(90);
    oval_stamp(3.0, 1, 'burlywood4');
#-------------------- Hat Top  -------------
    
    #reset to centre of current
    color('black');
    penup();
    setheading(0);
    goto(saveCoord);

#Creating Legend 4 Token, in this case
#Boot
def draw_legend_4():
    saveCoord = xcor(), ycor();

#-------------------- Shoe Sole Middle Oval -------------------
    penup();
    move_towards(270, 30);
    move_towards(0, 25);
    setheading(90);
    oval_stamp(2.0, 0.75, 'black');
    goto(saveCoord);
#-------------------- Shoe Sole Middle  Oval -------------------
    
#-------------------- Shoe Sole Oval ---------------------
    move_towards(270, 28);
    move_towards(0, 5);
    setheading(75);
    oval_stamp(2.3, 0.75, 'black');
    goto(saveCoord);
#-------------------- Shoe Sole Oval ---------------------

#-------------------- Toe Oval ---------------------
    move_towards(270, 25);
    move_towards(0, 18);
    setheading(90);
    oval_stamp(2.5, 0.70, 'burlywood3');
#-------------------- Toe Oval ---------------------
    
    
#-------------------- Bottom Oval ---------------------
    move_towards(0, -35);
    move_towards(90, 20);
    setheading(90);
    oval_stamp(1.4, 1.4, 'burlywood3');
    reset_pos = xcor(), ycor();
    color('burlywood3');

    #Goto Save Coord
    reset_pos = xcor(), ycor();
#-------------------- Bottom ---------------------
    
#--------------------Heel Sole ---------------------
    color('black');
    goto(saveCoord);
    begin_fill()
    move_towards(180, 12);
    move_towards(270, 28);
    move_towards(180, 23);
    move_towards(270, 10);
    move_towards(0, 22);
    move_towards(90, 10);
    goto(saveCoord);
    goto(reset_pos);
    end_fill()
#--------------------Heel Sole ---------------------
    
#--------------------Heel Top---------------------
    color('burlywood3');
    begin_fill();
    move_towards(180, 16);
    move_towards(270, 30);
    move_towards(0, 23);
    goto(saveCoord);
    goto(reset_pos);
    end_fill();
#--------------------Heel Top---------------------
   
#--------------------Boot Top---------------------
    goto(saveCoord);
    color('burlywood3');
    move_towards(180, 30);
    move_towards(270, 20);
    draw_quad([90, 60], [0, 30], [270, 60], [180, 30]);
    
    penup();
    goto(saveCoord);
    
    move_towards(90, 35);
    reset_pos = xcor(), ycor();
#--------------------Boot Top---------------------
    
#-------------------- Boot Arc---------------------
    pendown();
    begin_fill();
    make_lace('burlywood3');
    move_towards(270, 10);
    make_lace('burlywood3');
    move_towards(280, 20);
    make_lace('burlywood3');
    move_towards(290, 10);
    make_lace('burlywood3');
    move_towards(320, 10);
    make_lace('burlywood3');
    move_towards(340, 10);
    make_lace('burlywood3');
    move_towards(350, 15);

    move_towards(285, 5);
    move_towards(270, 2);
    move_towards(180, 50);
    move_towards(90, 40);
    goto(reset_pos);
    end_fill();
    move_towards(272, 10);
#-------------------- Boot Arc---------------------     
    goto(reset_pos);
    
   #reset to centre of current
    color('black');
    penup();
    setheading(0);
    goto(saveCoord);

#creating a quick line that
#goes to and from in 4 steps
#and resets pos and color
def make_lace(original_color):
    color('black');
    width(3);
    move_towards(240, 4);
    move_towards(45, 4);
    color(original_color);

#if no token value matches
#instead of crashing just draw a dot
def draw_legend_unkown():
    saveCoord = xcor(), ycor();
    
    pendown();
    color('black');
    dot(50)
    penup();
    color('black');

    setheading(0);
    goto(saveCoord);

#Read the strings passed in, check if its a single
#or double string and then checks if it matches a condition
def parse_location_instruction(location):
    location = location.split(' ');
    x = 0;
    y = 0;
    grid_centre = grid_size//2;

    centreCoord = ((grid_size * num_squares) // 2);
    
    #Centre so far is the only single word
    #insutruction, however can never be to sure
    if len(location) == 1:
        location[0].upper();
        
        if(location[0] == 'CENTRE'):
            x = centreCoord;
            y = centreCoord;
        else:
            x = centreCoord; 
            y = centreCoord;
    #if there are 2 instructions (not CENTRE) 
    elif len(location) > 1:
        
        for instruction in location:
            instruction = instruction.upper();

            if(instruction == 'LEFT'):
                x = 0 + grid_centre;
            elif(instruction == 'RIGHT'):
                x = grid_size * num_squares - grid_centre;
            elif(instruction == 'BOTTOM'):
                y = 0 + grid_centre;
            elif(instruction == 'TOP'):
                y = grid_size * num_squares - grid_centre;
            elif(instruction == 'CENTRE'):
                x = centreCoord;
                y = centreCoord;
            else :
                x = centreCoord;
                y = centreCoord;
             
    return x, y;
   

#Checks if String or int
def parse_instruction(instruction) :
    try :
        val = int(instruction);
        return True;
    except:
        return False;

#Reading oken parametre
#if value is an int we cant then go ahead and
#match value with a condition
def parse_token(token):
    #Is an int?
    if(parse_instruction(token)) :
        if(token == 0) :
            draw_legend_0();
            return 'Drawing Bucket'
        elif(token == 1) :
            draw_legend_1();
            return 'Drawing Mop'
        elif(token == 2) :
            draw_legend_2();
            return 'Drawing Overalls'
        elif(token == 3) :
            draw_legend_3();
            return 'Drawing Hat'
        elif(token == 4) :
            draw_legend_4();
            return 'Drawing Galoshes';
        elif(token == 5) :
            draw_line_left();
            return 'Drawing Left Line';
        elif(token == 99) :
            return 'Skipping draw';
        else:
            return 'No Sabe';
    else :
        #ok not an int, split and get insutructions
        token = token.split(' ');

        if len(token) > 1 :
            text = token[0];
            align = token[1];

            write_text(text, align);
        
        return 'Token not found, skipping Draw';


#Checking whether a string was passed
#then checking to see if the string matches with a case
def debug_parse_treasure(treasure):

    if(parse_instruction(treasure)) :
        if(treasure == 0) :
            return 'red';
        elif(treasure == 1) :
            return 'blue'
        elif(treasure == 2) :
            return 'green'
        elif(treasure == 3) :
            return 'yellow'
        elif(treasure == 4) :
            return 'orange'
        else:
            return 'yellow';
    else :
       raise ValueError('No Sabe');

#Checking whether a string was passed
#then checking to see if the string matches with a case
def parse_direction(direction) :
       
    if(not(parse_instruction(direction))) :
        if(direction == 'Start') :
            return 0;
        elif(direction == 'East') :
            return 0;
        elif(direction == 'West') :
            return 180;
        elif(direction == 'North') :
            return 90;
        elif(direction == 'South') :
            return 270;
        else:
            return 'No Sabe';
    else:
        raise ValueError('No Sabe');

#Following Coding Logic and creating
#legends based on the same path logic
legends_path = [
['Start', 'Top right', 'None'],
['East', 2, 'None'],
['South', 0, 'Legends left', 'poo'],
['South', 1, 0],
['South', 1, 1],
['South', 1, 2],
['South', 1, 3],
['South', 1, 4],
['Start', 'Top right', 'None'],
['East', 3, 'None'],
['South', 1, 'Bucket center'],
['South', 1, 'Mop center'],
['South', 1, 'Overalls center'],
['South', 1, 'Hat center'],
['South', 1, 'Boot center'],
]
    
# Follow the path as per the provided dataset
def follow_path(path):
    #Before we start the hunt we need to draw the legends
    
    if(len(path) == 1):
        print('Not much of a journey is it?');
        return;
    
    for step in range(len(path)):
        #pendown();
        #print(step);
        
        direction = parse_direction(path[step][0]);
        jump = path[step][1];

        
        if len(path[step]) > 2 :
            treasure_token = path[step][2];
        else :
            treasure_token = 'None';
               

        #checking jump to make sure its either
        #its a start location and start or
        #its a jump amount
        isJump = parse_instruction(jump);
        
        #check if value is a positional instruction,
        #or a jump value
        if(not(isJump)) :
            print('Start Treasure Hunt!');
            print('Going to Location', parse_location_instruction(jump));
            goto(parse_location_instruction(jump));
            parse_token(treasure_token);
            
        else :
            #pendown();
            setheading(direction);
            if jump != 0:
                forward(jump*100);
            #parse_token(treasure_token);
            print(parse_token(treasure_token));
            print('Continuing the Treasure Hunt!');

    print('Journey Has Ended');
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
title("Janitors Quest 2 : Hunt for the Gear")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.
#follow_path(fixed_path_0) # <-- used for code development only, not marking
follow_path(legends_path) # <------- Drawing Legends
follow_path(fixed_path_99) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
