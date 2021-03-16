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
        if t.tokenizer.get_token() == 32:
            self.__assign = Assign.Assign()
            self.__alternative = 1
        
        # get_token == "if"
        if t.tokenizer.get_token() == t.Tokens.IF.value:
            self.__assign = If.If()
            self.__alternative = 2

        # get_token == "while"
        if t.tokenizer.get_token() == t.Tokens.WHILE.value:
            self.__assign = Loop.Loop()
            self.__alternative = 3

        # get_token == "read"
        if t.tokenizer.get_token() == t.Tokens.READ.value:
            self.__assign = In.In()
            self.__alternative = 4

        # get_token == "write"
        if t.tokenizer.get_token() == t.Tokens.WRITE.value:
            self.__assign = Out.Out()
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

    def print(self):
        if self.__alternative == 1:
            self.__assign.print()
        if self.__alternative == 2:
            self.__if.print()
        if self.__alternative == 3:
            self.__loop.print()
        if self.__alternative == 4:
            self.__in.print()
        if self.__alternative == 5:
            self.__out.print()
    