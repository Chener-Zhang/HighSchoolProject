# hw6pr1.py - Hmmm!
#
# problem number: Lab!
#
# name:
# date:
#


# you'll write unique (or uniq) later in the lab...
#def unique(L):



# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Problem1 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

Problem1 = """
00 read r1          # get # from user to r1
01 write r1         #print r 1
02 copy r2 r1       # r2 = r1
03 mul r1 r1 r1     #r1*r1, get new r1
04 mul r1 r1 r2     #new r1 * r2, get new new ri
05 write r1         #print r1
06 setn r3 1        #set r3 == 1
07 sub r1 r1 r3     #subtract r2 from r1
08 write r1         # print r1
09 jeqzn r1 11      #if r1 == 0, then jump to 10 
10 jumpn 07         #if r1 != 0, then jump to 6
11 halt


"""




# Lab task #1: Change Problem1 to "the cubic countdown"

# Lab task #2: Write a random-number generator, named Random, here:
#   (Note: this is starter code for the inputs...)

Random = """
00 read r1    # input a
01 read r2    # input c
02 read r3    # input m
03 read r4    # input X_0
04 read r5    # input N
05 jeqzn r5 14      # if r5(N) == 0
06 setn r6 1        # set r6 ==1
07 sub r5 r5 r6     # N -1 
08 mul r7 r1 r4     # r7 = a * X0
09 add r8 r7 r2     # r8 = r7 + c
10 mod r9 r8 r3     # r9 = r8 % m
11 write r9         # print r9
12 copy r4 r9       # r9 = r4
13 jumpn 05         # jump to 05
14 halt             #stop

"""
m = 100
a = 20
c = 3



Fibonacci = """
00 read r1          #input r1
01 jeqzn r1 17      # if r1 == 0
02 setn r2 0        # set r2 == 0
03 setn r3 1        # set r3 == 1 
04 write r2         # print r2 
05 sub r4 r1 r3     # r4 = r1 - r3
06 write r3         # print r3
07 jeqzn r4 18      # if r4 == 0 then jump to 18
08 add r2 r2 r3     # r2 = r2 + r3
09 sub r5 r1 r2     # r5 = r1 - r2
10 write r2         # print r2 
11 jeqzn r5 18      # if r5 == 0 then jump to 18
12 add r3 r3 r2     # r3 = r3 + r2
13 sub r6 r1 r3     # r6 = r1 - r3
14 write r3         # print r3
15 jeqzn r6 18      # if r6 == 0 then jump to 18
16 jumpn 07         # jump to 07
17 write r1         # print r1 
18 halt             # stop!
"""


# This function runs the Hmmm program specified
#
def unique(L):
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return unique(L[1:])

def listFromFile(fileName):
    """ Takes a string containing a file name as input.  
        The file should contain numbers, with one number 
        on each line.  The output is a list of those 
        numbers.
    """
    numbersFile = open(fileName)     # open the file
    allText = numbersFile.read()     # get all the text from the file
    numbersFile.close()              # close the file
    
    justNums = allText.strip()       # just the numbers, still as a string
    listOfLines = justNums.split()   # into a list of strings: 1 per line
    strippedLines = [s.strip() for s in listOfLines] # remove spaces
    nonEmptyLines = [s for s in strippedLines if s != ''] # remove blanks
    listOfInts = [int(s) for s in listOfLines] # convert each line to an int
    
    return listOfInts
    
def run():
    """ runs a Hmmm program... """
    import hmmmAssembler ; reload(hmmmAssembler)  # import helpers
    hmmmAssembler.main(Fibonacci)     # this runs the code!
#   change this name   ^^^^^^^^  to run a different function!




