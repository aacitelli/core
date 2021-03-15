import t
import Decl 

class DeclSeq():

    def __init__(self):
        self.__decl = None
        self.__decl_seq = None

    def parse(self):

        # List of Decl 
        while t.tokenizer.get_token() == 4:
            decl = Decl.Decl()
            self.__decl_list.append(decl)
            decl.parse()
        
        # Successful error code
        return 0  

    def exec(self):
        for decl in self.__decl_list:
            decl.exec()

    def print(self):
        for decl in self.__decl_list:
            decl.print()