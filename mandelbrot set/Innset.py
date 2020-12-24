numIterations = 1000
MAX_X = 2.0
MIN_X = -4.0 
MAX_Y = 2.0
MIN_Y = -2.0
coordinateList = [ -2.0, 1.0, -1.0, 1.0 ]
""" the result by changing numIterations it will shows more detail in the graph
"""
def inMSet(c, numIterations):
      z = 0 + 0j
      for i in range(numIterations): 
            z = z*z
            z = z + c
            if abs(z) > 2:
                  return False
      return True 

from bmp import *

def testImage():
    """ a function to demonstrate how
        to create and save a bitmap image
    """
    width = 200
    height = 200
    image = BitMap(width, height)

    # create a loop in order to draw some pixels
    
    for col in range(width):
        if col % 10 == 0: print 'col is', col
        for row in range(height):
            if col % 10 == 0 or row % 10 == 0:
                image.plotPoint(col, row)

    # we have now looped through every image pixel
    # next, we write it out to a file

    image.saveFile("test.bmp")

    
def scale(pix, pixNum, floatMin, floatMax):
      a = pix * 1.0 / pixNum * 1.0
      sum = abs(floatMin) + abs(floatMax)
      b = sum * a
      c = floatMin + b
      return c 

def mset(width, height,):
      image = BitMap(width, height)
      for col in range(width):
          for row in range(height):
                  x = scale(col,width,MIN_X,MAX_X)
                  y = scale(row,height,MIN_Y,MAX_Y)*1j
                  c = x +y
                  if inMSet(c,numIterations):
                        image.plotPoint(col, row)
      image.saveFile("test.bmp")


def msetColor(width, height):
      image = BitMap(width, height)          
      for col in range(width):
          for row in range(height):
                  x = scale(col,width,MIN_X,MAX_X)
                  y = scale(row,height,MIN_Y,MAX_Y)*1j
                  c = x + y
                  mycolor = Color(row*2,row*20,row*2)
                  if inMSet(c,numIterations):
                        image.setPenColor(mycolor)
                        image.plotPoint(col, row)
      image.saveFile("test.bmp")


      
