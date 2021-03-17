import t 

class Int():

    def __init__(self):
        self.__num = None 

    def parse(self):
        tokNo = t.tokenizer.get_token()
        if tokNo != t.Tokens.NUMBER.value:
            print("Id: Expected token {}, got token {}".format(t.Tokens.NUMBER.value, tokNo))
            return -1 
        self.__num = t.tokenizer.get_int()
        t.tokenizer.skip_token()

    def exec(self):
        return self.__num

    def print(self, indentation):
        print(" " * indentation, end="")
        print(self.__num, end="")
        
    