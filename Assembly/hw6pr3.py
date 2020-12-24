# hw6 problem 3
#
# date: 
#
# Hmmm...
#
#

# For cs5gold, you'll write a fibonacci program
# For cs5black, it's a recursive Hanoi-solving program

# Either way, be sure to call it Problem3 !

# This is a placeholder by that name whose code you'll replace:
Problem3 = """
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
    hmmmAssembler.main(Problem3)     # this runs the code!
#   change this name   ^^^^^^^^  to run a different function!


