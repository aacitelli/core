import t 
import Assign 
import If 
import Loop 
import In 
import Out

class Stmt():

    def __init__(self):
        self.__assign = None 
        self.__if = None 
        self.__loop = None 
        self.__in = None 
        self.__out = None
        self.__alternative = None 

    def parse(self):

        # We use one-token lookahead to determine which alternative to use 

        # get_token == identifier
        tokNo = t.tokenizer.get_token()
        if tokNo == t.Tokens.IDENTIFIER.value:
            self.__assign = Assign.Assign()
            self.__assign.parse()
            self.__alternative = 1
        
        # get_token == "if"
        elif tokNo == t.Tokens.IF.value:
            self.__if = If.If()
            self.__if.parse()
            self.__alternative = 2

        # get_token == "while"
        elif tokNo == t.Tokens.WHILE.value:
            self.__while = Loop.Loop()
            self.__while.parse()
            self.__alternative = 3

        # get_token == "read"
        elif tokNo == t.Tokens.READ.value:
            self.__in = In.In()
            self.__in.parse()
            self.__alternative = 4

        # get_token == "write"
        elif tokNo == t.Tokens.WRITE.value:
            self.__out = Out.Out()
            self.__out.parse()
            self.__alternative = 5
        
        # Successful error code
        return 0  

    def exec(self):
        if self.__alternative == 1:
            self.__assign.exec()
        if self.__alternative == 2:
            self.__if.exec()
        if self.__alternative == 3:
            self.__loop.exec()
        if self.__alternative == 4:
            self.__in.exec()
        if self.__alternative == 5:
            self.__out.exec()

    def print(self, indentation):
        print(" " * indentation, end="")
        if self.__alternative == 1:
            self.__assign.print(0)
        if self.__alternative == 2:
            self.__if.print(0)
        if self.__alternative == 3:
            self.__loop.print(0)
        if self.__alternative == 4:
            self.__in.print(0)
        if self.__alternative == 5:
            self.__out.print(0)
    