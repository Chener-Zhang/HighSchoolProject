import sys

class Game:
      def __init__(self):
            self.board = []
            width = 15 ##### you can make change here
            for col in range(width): # col shi hang
                  self.board += [[0]* width]

                  
      def printBoard(self):
          """ this function prints the 2d list-of-lists
              A without spaces (using sys.stdout.write)
          """
          i = 0
          print "   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 " 
          for row in self.board:
              sys.stdout.write("%2d"%(i))
              i += 1               
              for col in row:
                  sys.stdout.write(" " + str(col)+ " ")
              sys.stdout.write('\n')


      def countneibor(self):
            A = self.board
            a = 0
            for i in range(15) :                 
                  for col in range(15):
                        if a == 5:
                              print "you win!"
                              return  True
                        else:
                              if A[i][col] == 1:
                                    a += 1
                              else:
                                    a = 0
                                    
            for i in range(15):
                  for row in range(15):
                        if a == 5:
                              print"you win!"
                              return  True
                        else:
                              if A[row][i] == 1:
                                    a +=1
                              else:
                                    a = 0
            ### right to left
            
            for i in range(15):
                  row = 0
                  for d in range(i,15):
                        if a == 5:
                              print "you win!"
                              return  True
                        else:
                              if A[row][d] == 1:
                                    row +=1
                                    a +=1
                                    
                              else:
                                    row +=1
                                    a = 0

            for i in range(15):
                  col = 0
                  for d in range(i,15):
                        if a == 5:
                              print "you win!"
                              return  True
                        else:
                              if A[d][col] == 1:
                                    col +=1
                                    a +=1
                              else:
                                    col +=1
                                    a = 0
            ###left to right
                                    
            for i in range(15):
                  col = 4
                  for d in range(i,15):
                        if a == 5:
                              print "you win!"
                              return  True
                        else:
                              if A[d][col] == 1:
                                    col -= 1
                                    a +=1
                                    
                                    
                              else:
                                    col -=1
                                    a = 0

            for i in range(14,-1,-1):
                  row = 0
                  for d in range(i,-1,-1):
                        if a == 5:
                              print "you win!"
                              return  True
                        else:
                              if A[row][d] == 1:
                                    row += 1
                                    a +=1
                              else:
                                    row +=1
                                    a = 0
                  
                  ##########
            for i in range(15) :                 
                  for col in range(15):
                        if a == 5:
                              print " you win!"
                              return    True
                        else:
                              if A[i][col] == 2:
                                    a += 1
                              else:
                                    a = 0
                                    
            for i in range(15):
                  for row in range(15):
                        if a == 5:
                              print" you win!"
                              return  True
                        else:
                              if A[row][i] == 2:
                                    a +=1
                              else:
                                    a = 0
            ### right to left
            
            for i in range(15):
                  row = 0
                  for d in range(i,15):
                        if a == 5:
                              print "you win!"
                              return  True
                        else:
                              if A[row][d] == 2:
                                    row +=1
                                    a +=1
                                    
                              else:
                                    row +=1
                                    a = 0

            for i in range(15):
                  col = 0
                  for d in range(i,15):
                        if a == 5:
                              print " you win!"
                              return  True
                        else:
                              if A[d][col] == 2:
                                    col +=1
                                    a +=1
                              else:
                                    col +=1
                                    a = 0
            ###left to right
                                    
            for i in range(15):
                  col = 4
                  for d in range(i,15):
                        if a == 5:
                              print "you win!"
                              return  True
                        else:
                              if A[d][col] == 2:
                                    col -= 1
                                    a +=1
                                    
                                    
                              else:
                                    col -=1
                                    a = 0

            for i in range(14,-1,-1):
                  row = 0
                  for d in range(i,-1,-1):
                        if a == 5:
                              print "you win!"
                              return  True
                        else:
                              if A[row][d] == 2:
                                    row += 1
                                    a +=1
                              else:
                                    row +=1
                                    a = 0


      def codn(self):
            A = self.board
            player1row = raw_input("player1 type a row number")
            player1col = raw_input("player1 type a col number")
            row = int(player1row) 
            col = int(player1col)
            if A[row][col] == 0:
                  A[row][col] = 1
                  self.printBoard()
            elif self.countneibor():
                  return 
            else:
                  print"Do not type the number that already exist"
                  player1row = raw_input("player1 type a row number")
                  player1col = raw_input("player1 type a col number")
                  row = int(player1row) 
                  col = int(player1col) 
            if A[row][col] == 0:
                  A[row][col] = 1
                  self.printBoard()
            elif self.countneibor():
                  return 
                  
            player2row = raw_input("player2 type a row number")
            player2col = raw_input("player2 type a col number")
            row = int(player2row)
            col = int(player2col)
            
            if A[row][col] == 0:
                  A[row][col] = 2
                  self.printBoard()
            elif self.countneibor():
                  return
            
            else:
                  print"Do not type the number that already exist"
                  player2row = raw_input("player2 type a row number")
                  player2col = raw_input("player2 type a col number")
                  row = int(player2row) 
                  col = int(player2col)
            if A[row][col] == 0:
                  A[row][col] = 2
                  self.printBoard()
            elif self.countneibor():
                  return 


            ### 
            self.codn()

                  
                  
            

            

                  
            
                
      

            


                  
            
            

 
                  
                  

            

              

      

            
                  
            




              
