#
# hw3pr1.py - Lab problem: "Lights On!"
#
# Name: Chener Zhang
#
#

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.
import sys            # larger recursive stack
sys.setrecursionlimit(10000) # 10000 stack frames availble



def evolve(oldL, curgen = 0):
    print range(len(oldL))   ## List print 
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print oldL,                    # print the old list, L
    print "  (gen: " + str(curgen) + ")"  # and its gen.
    time.sleep(0.25)
    
    if allOnes(oldL) == 1:  # we're done!
        return curgen      # no return value... yet
    else:
        user = input("Index? ")
        newL = [ mutate(i,oldL,user) for i in range(len(oldL)) ]
        return evolve(newL, curgen + 1)

def allOnes(L):
    """ this function will check the all element in the list is "1" or not.
        if all of them are "1" , it will return True, if not, it will return
        False
    """ 
    if L == []:
        return True             #base case 
    elif L[0] == 1:
        return allOnes(L[1:])
    else:
        return False

def mutate(i, oldL, user = 0):
    
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    if i == user or i - 1 == user or i + 1 == user :
        new_ith_element = 1 - oldL[i]       
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element



def randBL(N):
    """ This function will return "1" or "0", and the N is the length of the
    element
    """
    if N == 0:
        return  []
    else:
        L = [choice([0,1])]
    return randBL(N - 1) + L

