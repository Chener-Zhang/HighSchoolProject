def exact_change( target_amount,L):
       """check the L if it can accomplish the target_amount"""
       #basecase
       if target_amount == 0:
              return True
       elif target_amount < 0:
              return False
       elif L == [] :
              return False 
              
       
       else:  #recursive part
              coinToUse = L[0]
              restOfCoins = L[1:]
              
              #loseit 
              loseit = exact_change(target_amount,restOfCoins)

              #useit
              useit = exact_change(target_amount-coinToUse,restOfCoins)

       if useit:
              return True
       elif loseit:
              return True 
       else:
              return False

              
