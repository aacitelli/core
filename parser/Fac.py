import t
import Op


class Fac():
    def __init__(self):
        self.__op = None
        self.__fac = None
        self.__alternative = None

    def parse(self):

        # Op
        self.__op = Op.Op()
        self.__op.parse()

        # If we get an asterisk, means we use second production
        tokNo = t.tokenizer.get_token()
        if tokNo == t.Tokens.STAR.value:
            t.tokenizer.skip_token()
            # print("Fac: Consumed `*` token.")
            self.__fac = Fac()
            self.__fac.parse()
            self.__alternative = 2
        else:
            self.__alternative = 1

        # Successful error code
        return 0

    def exec(self):
        if self.__alternative == 1:
            return self.__op.exec()
        return self.__op.exec() * self.__fac.exec()

    def print(self):
        self.__op.print()
        if self.__alternative == 2:
            print(" * ", end="")
            self.__fac.print()