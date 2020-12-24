      ### for "2"
            
            for i in range(15):
                  row = 0
                  for d in range(i,15):
                        if a == 5:
                              print "you win"
                              return
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
                              print " you win"
                              return
                        else:
                              if A[d][col] == 2:
                                    col +=1
                                    a +=1
                              else:
                                    col +=1
                                    a = 0
            for i in range(15):
                  row = 0
                  for d in range(i,15):
                        if a == 5:
                              print "you win"
                              return
                        else:
                              if A[row][d] == 2:
                                    row -= 1
                                    a +=1
                              else:
                                    row -=1
                                    a = 0

            for i in range(15):
                  col = 0
                  for d in range(i,15):
                        if a == 5:
                              print "you win"
                              return
                        else:
                              if A[d][col] == 2:
                                    col -= 1
                                    a +=1
                              else:
                                    col -=1
                                    a = 0
 
