#
# hw9pr1.py
# Chener Zhang

#
# first, practice reloading a file - without quitting Python:
#

# Here is a simple function:
def f(x)：
    """ adds one """
    return 2*x



# Try this function in Python with f(41)
# Then, change it so that it returns 2*x instead (and save...)
# without quitting Python, paste this "rerun" command:
#
# import hw9pr1; reload(hw9pr1); from hw9pr1 import *
#
# and then use the up-arrow to run f(41) again... 
# this time, it should be 82

# Using this trick (and the up-arrow shortcut) will save lots of time + typing!



#
# Here is a function that will help start hw9pr1's lab:
#

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [[0] * width]       # What do you need to add a whole row here?
                                 # You just need something that returns one row :-) !
    return A

import sys

def printBoard(A):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
        but, only in the * interior * of the 2d array
    """
    A = createBoard(width, height)
    for row in range(1,height-1):
        for col in range(1,width-1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width, height):
       A = createBoard(width, height)
       for row in range(1,height-1):
           for col in range(1,width-1):
               if row == col:
                   A[row][col] = 1
               else:
                   A[row][col] = 1
       return A
import random

def randomCells(width, height):
        A = createBoard(width, height)
        for row in range(1,height-1):
            for col in range(1,width-1):
                if row == col:
                    A[row][col] = random.choice([1,0]) 
                else:
                    A[row][col] = random.choice([1,0])
        return A

def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height )
    for row in range(1,height-1):
        for col in range(1,width-1):
            if A[row][col] == 1:
                newA[row][col] = 1 
    return newA


def innerReverse(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height )
    for row in range(1,height-1):
        for col in range(1,width-1):
            if A[row][col] == 1:
                newA[row][col] = 0
            elif A[row][col] == 0:
                newA[row][col] = 1

    return newA

def countNeighbors(row,col,A):
    count = 0
    B = 1
    if A[row - 1][col - 1] == 1:
        count = 0 + B 
    if A[row - 1][col] == 1:
        count = count + B
    if A[row - 1][col + 1] == 1:
        count = count + B
    if A[row][col - 1] == 1:
        count = count + B
    if A[row][col + 1] == 1:
        count = count + B
    if A[row + 1 ][col- 1] == 1:
        count = count + B
    if A[row + 1][col] == 1:
        count = count + B
    if A[row + 1][col + 1] == 1:
        count = count + B   
    return count 


def next_life_generation(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height )
    for row in range(1,height-1):
        for col in range(1,width-1):
            if countNeighbors(row,col,A) < 2:
                newA[row][col] = 0
            if countNeighbors(row,col,A) > 3:
                newA[row][col] = 0
            if countNeighbors(row,col,A) == 3:
                newA[row][col] = 1
            if countNeighbors(row,col,A) == 2:
                newA[row][col] = A[row][col] 

    return newA


######extra credit
def next_mutatelife_generation(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height )
    for row in range(1,height-1):
        for col in range(1,width-1):
            if countNeighbors(row,col,A) == 2: # if have 2 neibor, the cell can get enough energy from it neighbor
                newA[row][col] = 1
            if countNeighbors(row,col,A) == 3:#  the cell can get extra energy and food from it's neibors
                newA[row][col] = 1
            if countNeighbors(row,col,A) < 2:# because the neibor is too poor cannot supply enough food to it, so it will die
                newA[row][col] = 0
            if countNeighbors(row,col,A) == 0 :# it do not have any neibor, no one supply to food for it. so he will die
                newA[row][col] = 0 

    return newA

            

            
                

                
                
     


    





      
    



        

        

    
    
       

