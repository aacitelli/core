import t
import IdList


class In():
    def __init__(self):
        self.__id_list = None

    def parse(self):

        # `read` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.READ.value:
            print("Id: Expected token {}, got token {}".format(
                t.Tokens.READ.value, tokNo))
            return -1
        # print("In: Consumed `read` token.")

        # IdList
        self.__id_list = IdList.IdList()
        self.__id_list.parse()

        # `;` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.SEMICOLON.value:
            print("Id: Expected token {}, got token {}".format(
                t.Tokens.SEMICOLON.value, tokNo))
            return -1
        # print("In: Consumed `;` token.")

    # Essentially reads input and does an assign on each Id given
    def exec(self):
        self.__id_list.input_values()

    def print(self):
        print("read ", end="")
        self.__id_list.print()
        print(";")
