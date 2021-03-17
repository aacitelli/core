import t 
import Fac

class Exp():

    def __init__(self):
        self.__fac = None 
        self.__exp = None
        self.__alternative = None 

    def parse(self):

        # Fac
        self.__fac = Fac.Fac()
        self.__fac.parse()

        # Use one-token lookahead to decide which production we used 
        tokNo = t.tokenizer.get_token()
        if tokNo == t.Tokens.PLUS.value:
            self.__exp = Exp()
            self.__exp.parse()
            self.__alternative = 2
        elif tokNo == t.Tokens.MINUS.value:
            self.__exp = Exp()
            self.__exp.parse()
            self.__alternative = 3
        else:
            self.__alternative = 1
        
        # Successful error code
        return 0  

    def exec(self):
        if self.__alternative == 1:
            return self.__fac.exec()
        if self.__alternative == 2:
            return self.__fac.exec() + self.__exp.exec()
        return self.__fac.exec() - self.__exp.exec()

    def print(self, indentation):
        print(" " * indentation, end="")
        self.__fac.print(0)
        if self.__alternative == 2:
            print(" + ", end="")
            self.__exp.print(0)
        if self.__alternative == 3:
            print(" - ", end="")
            self.__exp.print(0)