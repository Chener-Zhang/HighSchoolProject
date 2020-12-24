#
# hw3pr1gr.py - graphical "Lights On!"
#


from turtle import *
import csgrid; from csgrid import *
from random import *


#
# This gets called once for each mouseclick
#
def evolve(oldL, user):
    """ L is the list of lights
        user is the column clicked
    """
    print "The user clicked at column:", user
    newL = [mutate(i, oldL, user) for i in range(len(oldL))]
    show(newL)                 # display
    
    if newL == [1]*len(oldL):
        print "Hooray!"


#
# mutate is the same as before
#
def mutate(i, oldL, user):
    """ returns the new ith element, based on
          i, the index
          oldL, the old list
          user, the user's chosen column
    """
    if i == user or i - 1 == user or i + 1 == user :
        new_ith_element = 1 - oldL[i]       
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element



#
# start the game here (with color definitions)
#

setColor(0, "blue")
setColor(1, "white")

show( [0,1,0,0,1,0,1] )




#
# Graphics stuff - the "mouse handler" is here
#                  (The rest is hidden away in csgrid)
#



#
# set the mouse handler, so that it reponds to mouse clicks
#
def mouseHandler(x,y):
    """ This function is called with each mouse click.

        Its inputs are the pixel location of the
        next mouse click: (x,y)
        
        It computes the column (within the list)
        where the click occurred with getCol.

        The overall list is shared between turtle graphics
        and the other parts of your program as a global
        variable named currentL. In general, global variables
        make software more complex, but sometimes they are
        necessary.

        Then, this function calls the next generation via
        runGraphicsGen( L, col ) - note that the col is available!
    """
    user = getCol(x,y)
    oldL = csgrid.currentL  # get from the graphics module
    evolve(oldL,user)       # call evolve


onscreenclick(mouseHandler)



done()  # if you don't run idle -n, you may need this line uncommented...





