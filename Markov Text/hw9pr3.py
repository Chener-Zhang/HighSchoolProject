import random
def createDictionary( filename ):
    f = open( filename )
    text = f.read()
    f.close()
    LoW = text.split()
    d ={}
    previous = '$'
    
    for word in LoW:
        if d.has_key(previous):
            d[previous] = [word] + d[previous]
            previous = word
            
        else:
            d[previous] = [word]
            previous = word
            
        if word[-1] == '.' or word[-1] == '?'or word[-1] == '!':
            previous = '$'
            
    return d



def generateText( d, n ):
    nextword = random.choice(d['$'])
    text = ''
    
    for i in range(n - 1):
        if nextword[-1] == '.' or nextword[-1] == '?'or nextword[-1] == '!' :
            text = text+ " " +  nextword 
            nextword = random.choice(d['$'])
        else:                  
            text = text + " " + nextword
            nextword = random.choice(d[nextword])
            
    return text         
 

def literacy():
    d = createDictionary( 't.txt' )
    a = random.choice(range(50))
    return generateText( d, a )

        
    

        
    



    
    


