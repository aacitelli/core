import t 
import Int 

class Id():

    def __init__(self):
        self.__identifier = None 
        self.__value = None 

    def parse(self):
        tokNo = t.tokenizer.get_token()
        if tokNo != t.Tokens.IDENTIFIER.value:
            print("Id: Expected token {}, got token {}".format(t.Tokens.IDENTIFIER.value, tokNo))
            return -1 
        self.__identifier = t.tokenizer.get_id()
        t.tokenizer.skip_token()

    # Essentially, if I pass in a value as the first parameter, this acts as a setter method that returns the value set.
    # Otherwise, it acts like a getter method.
    def exec(self, initialize_val):
        if initialize_val != None:
            # print("Initialized {} to {}".format(self.__identifier, initialize_val))
            self.__value = initialize_val
        return self.__value

    def print(self, indentation):
        print(" " * indentation, end="")
        print(self.__identifier, end="")

    # Static set of ids and what's essentially a static method 
    ids = set() 
    @classmethod
    def id_exists(cls, id):
        return id in cls.ids