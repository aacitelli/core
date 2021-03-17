import t 
import Id 

class IdList():

    def __init__(self):
        self.__id = None
        self.__id_list = None

    def parse(self):

        # Id
        self.__id = Id.Id()
        self.__id.parse()

        # If next is a comma, we are in second comma 
        # `,` token 
        tokNo = t.tokenizer.get_token()
        if tokNo == t.Tokens.COMMA.value:
            t.tokenizer.skip_token()
            self.__id_list = IdList()
            self.__id_list.parse()
            
        # Successful error code 
        return 0 

    def exec(self, declare):
        output = []
        output.append(self.__id.exec(declare, None))
        if self.__id_list != None:
            output.append(self.__id_list.exec(declare, None))
        return output

    def print(self, indentation):
        print(" " * indentation, end="")
        self.__id.print(0)
        if self.__id_list != None:
            print(", ", end="")
            self.__id_list.print(0)

    def print_values(self, indentation):
        print(" " * indentation, end="")
        self.__id.print_value(0)
        if self.__id_list is not None:
            self.__id_list.print_values(0)