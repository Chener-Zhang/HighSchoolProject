
# 
# gold hw2pr3.py
#
# Name(s): chener zhang 
#

# CANOPY SETTING FOR TURTLE
# 
# be sure that you disable PyLab (under Preferences Python)
# (you may need to restart the Python kernel after this)

# Answer 1
from turtle import *
def spiral(initialLength,angle,multiplier):
    
    if initialLength < 1:
        return
    else:
        forward(initialLength)
        right(angle)
        
        spiral((initialLength*multiplier),angle,multiplier)
    
        # an example: poly(sz,n,N)
def poly( sz, n, N ):
    """ poly draws a regular polygon with
        sz: # of pixels per side
        n:  # of sides yet to draw
        N:  # of sides in the whole polygon
    """
    if n < 1:
        return
    else:
        forward( sz )
        right( 360.0/N )
        poly( sz, n-1, N )

#
# try this out (paste and hit return):
"""
poly(50,7,7); mainloop()
"""

# customize! (paste and hit return twice):
"""
width(5); shape( 'turtle' )
color( 'darkgreen' )
poly(50,7,7); mainloop()
"""


#
# Here, you'll write spiral, svtree, and snowflake
#       and, if you like, your own custom-artwork f'n...
#
# Answer for the 'tree make'
from turtle import *
def svtree(trunklength,levels):
    if levels == 0:
        return
    else:
        forward(trunklength)
        left(30)
        svtree(trunklength*0.8,levels-1)
        right(60)
        svtree(trunklength*0.8,levels-1)
        left (30)
        backward (trunklength)
        return

# snow 
from turtle import *
def snowflake(sidelength, levels):
    """ fractal snowflake function
          sidelength: pixels in the largest-scale triangle side
          levels: the number of recursive levels in each side
    """
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)

def flakeside(sidelength, levels):
    if levels==0:
        return 
    forward(sidelength)
    left(60)
    snowflake(sidelength,levels-1)
    left(120)
    
    
    
    
    
   

    
    
        
