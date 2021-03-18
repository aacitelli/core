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
            print("Assign: Expected token {}, got token {}".format(
                t.Tokens.EQUALS.value, tokNo))
            return -1

        # Exp
        self.__exp = Exp.Exp()
        self.__exp.parse()

        # `;` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.SEMICOLON.value:
            print("Assign: Expected token {}, got token {}".format(
                t.Tokens.SEMICOLON.value, tokNo))
            return -1

        # Successful error code
        return 0

    def exec(self):
        exp_val = self.__exp.exec()
        self.__id.exec(None, exp_val)  # Pass in Assign flag

    def print(self, indentation):
        print(" " * indentation, end="")
        self.__id.print(0)
        print(" = ", end="")
        self.__exp.print(0)
        print(";")