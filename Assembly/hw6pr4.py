# hw6 problem 4
#
# date: 
#
# Hmmm...
#
#

# For cs5green, you'll write a recursive power program
# For cs5black, it's the Ex. Cr. "Ackermann" program

#
# GOLD students:
#
# for cs5gold -- don't use these Hmmm starter lines at all!
#     instad, simply overwrite all of the contents of this file
#     by copying the starting lines provided in hw6pr4's description
#     then, you'll write three programs involving loops...
#

#
# for cs5green and cs5black:
#
# This is a placeholder by that name whose code you'll replace:
Problem4 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# This function runs the Hmmm program specified
#
def run():
    """ runs a Hmmm program... """
    import hmmmAssembler ; reload(hmmmAssembler)  # import helpers
    hmmmAssembler.main(Problem4)     # this runs the code!
#   change this name   ^^^^^^^^  to run a different function!


