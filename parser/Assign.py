import t
import Id 
import Exp 

class Assign():

    def __init__(self):
        self.__id = None 
        self.__exp = None

    def parse(self):

        # Id 
        self.__id = Id.Id()
        self.__id.parse()
        
        # `=` token 
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.EQUALS.value:
            print("Expected token {}, got token {}".format(t.Tokens.EQUALS.value, tokNo))
            return -1 

        # Exp
        self.__exp = Exp.Exp()
        self.__exp.parse() 

        # `;` token 
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.SEMICOLON.value:
            print("Expected token {}, got token {}".format(t.Tokens.SEMICOLON.value, tokNo))
            return -1
            
        # Successful error code 
        return 0 

    def exec(self):
        self.__id.exec()
        self.__exp.exec()

    def print(self):
        self.__id.print()
        print(" = ", end="")
        self.__exp.print()
        print(";")