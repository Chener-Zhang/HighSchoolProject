#
# hw1pr2.py (Lab1, part 2)
#
# Name: chener zhang
# Date: 9.23
#

def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x

# answer 1
def sq(x):
    """ the output of sq is the squart of input"""
    return x**2

# answer 2
# i don't know how to do this one


# answer3
def checkends(s):
    if s[0] == s[-1]:
        return True
    else:
        return False

# answer 4
def flipside(s):
    """ this function will switch the 'first half of s' and ' second half of s'"""
    x = len(s)/2
    return x
    print flipside[x:]+ flipside[0:x]


# answer 5
def convertFromSeconds( s ):
    days = s / (24*60*60)  # # of days
    s = s % (24*60*60)     # the leftover
    hours = s / (60*60)    
    minutes = s/60
    seconds = s
    return [days, hours, minutes, seconds]


        

