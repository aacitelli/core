import t


class CompOp():
    def __init__(self):
        self.__alternative = None

    def parse(self):

        # Get whatever token it is
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        print("Comp: Consumed token no {}.".format(tokNo))

        if tokNo == t.Tokens.NOT_EQUALS.value:
            self.__alternative = 1
        elif tokNo == t.Tokens.DOUBLE_EQUALS.value:
            self.__alternative = 2
        elif tokNo == t.Tokens.LESS_THAN.value:
            self.__alternative = 3
        elif tokNo == t.Tokens.GREATER_THAN.value:
            self.__alternative = 4
        elif tokNo == t.Tokens.LESS_THAN_OR_EQUAL_TO.value:
            self.__alternative = 5
        elif tokNo == t.Tokens.GREATER_THAN_OR_EQUAL_TO.value:
            self.__alternative = 6
        else:
            print("CompOp: Invalid Token {}".format(tokNo))
            return -1

        # Successful error code
        return 0

    def exec(self):
        return self.__alternative

    def print(self, indentation):
        print(" " * indentation, end="")
        if self.__alternative == 1:
            print(" != ", out="")
        if self.__alternative == 2:
            print(" == ", out="")
        if self.__alternative == 3:
            print(" < ", out="")
        if self.__alternative == 4:
            print(" > ", out="")
        if self.__alternative == 5:
            print(" <= ", out="")
        if self.__alternative == 6:
            print(" >= ", out="")