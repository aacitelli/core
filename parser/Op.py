import t
import Int
import Id
import Exp


class Op():
    def __init__(self):
        self.__int = None
        self.__id = None
        self.__exp = None
        self.__alternative = None

    def parse(self):

        # Use one-token lookahead to determine whether it's <int>, <id>, or (<exp>)
        tokNo = t.tokenizer.get_token()
        if tokNo == t.Tokens.NUMBER.value:
            self.__int = Int.Int()
            self.__int.parse()
            self.__alternative = 1
        elif tokNo == t.Tokens.IDENTIFIER.value:
            self.__id = Id.Id()
            self.__id.parse()
            self.__alternative = 2
        elif tokNo == t.Tokens.OPEN_PAREN.value:
            self.__exp = Exp.Exp()
            self.__exp.parse()
            self.__alternative = 3
        else:
            print("Op: Invalid Next Token {}!".format(tokNo))
            exit(-1)
            return -1

        # Successful error code
        return 0

    def exec(self):
        if self.__alternative == 1:
            return self.__int.exec()
        if self.__alternative == 2:
            return self.__id.exec()
        if self.__alternative == 3:
            return self.__exp.exec()

    def print(self, indentation):
        print(" " * indentation, end="")
        if self.__alternative == 1:
            return self.__int.print(0)
        if self.__alternative == 2:
            return self.__id.print(0)
        if self.__alternative == 3:
            return self.__exp.print(0)