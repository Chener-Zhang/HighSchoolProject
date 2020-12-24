#Answer 1 removeALL
def removeAll(e, L):
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else :
        return [L[0]] + removeAll(e, L[1:])

#Answer 2 # i don't know why this one didn't work well.
def zipper(L, K):
       if K==[]:
              return []
       elif L==0:
              return [] 
       else:
              print [L[0] + K[0]] + zipper(L[1:],K[1:])


#Answer 3  # the first part is work, but then i don't know how to check if e is
           # inside the L
def ind(e,L):
       n=0
       s=1
       if L[0]==e:
              return n
       elif L==0:
              return n
       else:
              return s + ind(e,L[1:]) 
       if L=[]:
               print 0
       else:
              return len(L)

       
