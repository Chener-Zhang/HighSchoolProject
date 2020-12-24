# 
# Name: chener zhang
#
# hw1pr1.py (Lab 1, part 1)
# slicing and indexing challenges
#

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):  [2,7,5,9]
answer0 = e[0:2] + pi[-2:]  
print answer0

# answer1 1: creating [7,1]
answer1 = e[1:]
print answer1

# answer2
answer2 = pi[-1:]+e[-1:]+e[-1:]
print answer2

# answer3
answer3 = pi[1:]
print answer3

# answer4
answer4 =e[-1:] +e[0:1] + pi[0:6:2]
print answer4





# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# answer5
answer5 = h[0]+h[4:] 
print answer5

# answer6
answer6 = c[0:4]+ m[1:3] + c[6:] 
print answer6

# answer7
answer7 = h[1:]+m[1:]
print answer7

# answer8
answer8 =h[0:3] +m[3:] +c[6:] +h[0:3]*3
print answer8

# answer9
answer9 =c[3:6] + c[1]+m[0] + h[-1:] +h[-2] +c[-2]+ c[1]
print answer9

# answer10
answer10 = c[0:6:2]+ h[1:3] +c[0]+h[1]+c[2]*2
print answer10




                             








