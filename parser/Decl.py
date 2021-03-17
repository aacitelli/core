import t 
import IdList 

class Decl():

    def __init__(self):
        self.__idlist = None

    def parse(self):

        # `int` token 
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.INT.value:
            print("Decl: Expected token {}, got token {}".format(t.Tokens.INT.value, tokNo))
            return -1 

        # IdList
        self.__id_list = IdList.IdList()
        self.__id_list.parse()

        # `;` token 
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != 12:
            print("Decl: Expected token {}, got token {}".format(12, tokNo))
            return -1 
            
        # Successful error code 
        return 0 

    def exec(self):
        self.__id_list.exec()

    def print(self, indentation):
        print(" " * indentation, end="")
        print("int ", end="")
        self.__id_list.print(0)
        print(";")