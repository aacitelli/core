# see if a string is valid ident 
def identifierWorks(stringObj):

    print(stringObj)

    # Check length 
    if len(stringObj) < 1 or len(stringObj) > 8:
        return False

    # Check first character (must be capitol)
    if not stringObj[0].isupper():
        return False

    # Iterate through rest to see if it works 
    onLetters = True
    for char in stringObj[1:]:
        print(char)
        if onLetters: # If we're on the letters half, we either check lowercase or switch to numbers 
            if char.isdigit():
                onLetters = False
            else:
                if not char.isupper():
                    return False 
        else: # If on numbers, we just check that each one is a digit
            if not char.isdigit():
                return False
    return True