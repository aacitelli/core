import t
import Op
import CompOp


class Comp():
    def __init__(self):
        self.__value = None
        self.__op1 = None
        self.__compOp = None
        self.__op2 = None

    def get_value(self):
        return self.__value

    def parse(self):

        # `(` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.OPEN_PAREN.value:
            print("Comp: Expected token {}, got token {}".format(
                t.Tokens.OPEN_PAREN.value, tokNo))
            return -1

        # Op1
        self.__op1 = Op.Op()
        self.__op1.parse()

        # CompOp
        self.__compOp = CompOp.CompOp()
        self.__compOp.parse()

        # Op2
        self.__op2 = Op.Op()
        self.__op2.parse()

        # `)` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.CLOSED_PAREN.value:
            print("Comp: Expected token {}, got token {}".format(
                t.Tokens.CLOSED_PAREN.value, tokNo))
            return -1

        # Successful error code
        return 0

    def exec(self):

        # Get values
        op1 = self.__op1.exec()
        op2 = self.__op2.exec()
        compOp = self.__compOp.exec()
        try:
            if compOp == 1:
                self.__value = op1 != op2
            if compOp == 2:
                self.__value = op1 == op2
            if compOp == 3:
                self.__value = op1 < op2
            if compOp == 4:
                self.__value = op1 > op2
            if compOp == 5:
                self.__value = op1 <= op2
            if compOp == 6:
                self.__value = op1 >= op2
            raise Exception("")
        except Exception:
            print("Error: Invalid Comparison {} {} {}".format(
                op1, compOp, op2))
            return -1
        return 0

    def print(self, indentation):
        print(" " * indentation, end="")
        print("(", end="")
        self.__op1.print(0)
        self.__compOp.print(0)
        self.__op2.print(0)
        print(")", end="")