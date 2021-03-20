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
            # print("IdList: Consumed `,` token.")
            self.__id_list = IdList()
            self.__id_list.parse()

        # Successful error code
        return 0

    def exec(self, declare):
        output = []
        output.append(self.__id.exec(declare, None))
        if self.__id_list != None:
            output.append(self.__id_list.exec(declare))
        return output

    def print(self):
        self.__id.print()
        if self.__id_list != None:
            print(", ", end="")
            self.__id_list.print()

    def print_values(self):
        self.__id.print_value()
        if self.__id_list is not None:
            self.__id_list.print_values()
        print()

    def input_values(self):
        self.__id.read_in_value()
        if self.__id_list is not None:
            self.__id_list.input_values()