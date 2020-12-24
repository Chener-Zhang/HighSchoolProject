# hw6 problem 2
#
# name(s): 
# date: 
#
#
#

# For cs5gold, you'll write a power program
# For cs5black, it's a fibonacci program

# Either way, be sure to call it Problem2 !

# This is a placeholder by that name whose code you'll replace:
Problem2 = """
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
    hmmmAssembler.main(Problem2)     # this runs the code!
#   change this name   ^^^^^^^^  to run a different function!


