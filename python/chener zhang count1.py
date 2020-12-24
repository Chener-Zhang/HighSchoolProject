def count1(s):
    """ this function count how many 1 in the s"""
    if  10+(s%10)/10 == 1 or s / 10 == 1 :
        return 1 
    elif s / 10 == 0:
        return 0
       
     
    else:
        first = s % 10
        rest = s / 10
        #useit
        if first == 1 :
            return 1 + count1(rest)
        #loseit
        else:
            return 0 + count1(rest) 

        
