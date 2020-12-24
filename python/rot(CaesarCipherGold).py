def rot(c,n):
    if ord(c) >= 97 and ord(c) <= 122:
        asciiValue = ord(c)
        letternumber = asciiValue - ord('a')
        rotated = (letternumber + n) % 26
        rotateda = rotated + ord('a')
        return chr(rotateda)
    elif ord(c) >= 65 and ord(c) <= 90:
        a = ord(c)
        number = a - ord('A')
        r = (number + n) % 26
        rt = r + ord('A')
        return chr(rt)
    else:
        return ' '


def list_to_str( L ):
    """ L must be a list of characters; then,
        this returns a single string from them
    """
    if len(L) == 0: return ''
    return L[0] + list_to_str( L[1:] )
        

def encipher( S , n ):
        return map(lambda x :rot(x,n),S) 
    
