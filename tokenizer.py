class Tokenizer: 

    def __init__(self, file):
        self.tokens = []
        self.file = file

    # Returns (info about) current token; 
    # Repeated calls to getToken() return the same token 
    def getToken(self): 
        pass

    # Skips current token; next getToken() call will return new token 
    def skipToken(self):
        pass 

    # Returns the value of the current (integer) token 
    # Errors out if the current token is not an integer 
    def intVal(self):
        pass

    # Returns the name (string) of the current (id) token 
    # Errors out if the current token is not an id 
    def idName(self): 
        pass =