import t
import Decl 

class DeclSeq():

    def __init__(self):
        self.__decl = None
        self.__decl_seq = None

    def parse(self):

        # Decl
        self.__decl = Decl.Decl()
        self.__decl.parse()

        # List of Decl, if one-token lookahead shows us there is another decl 
        # NOTE: The above decl will call skip_token, so we don't have to worry about infinite recursion here 
        if t.tokenizer.get_token() == t.Tokens.INT.value:
            self.__decl_seq = DeclSeq.DeclSeq()
            self.__decl_seq.parse()
        
        # Successful error code
        return 0  

    def exec(self):
        self.__decl.exec()
        if self.__decl_seq != None:
            self.__decl_seq.exec()

    def print(self):
        self.__decl.print()
        if self.__decl_seq != None:
            self.__decl_seq.print()