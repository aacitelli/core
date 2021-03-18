import t
import Cond
import StmtSeq


class Loop():
    def __init__(self):
        self.__cond = None
        self.__stmt_seq = None

    def parse(self):

        # `while` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.WHILE.value:
            print("If: Expected token {}, got token {}".format(
                t.Tokens.WHILE.value, tokNo))
            return -1
        print("Loop: Consumed `while` token.")

        # Cond
        self.__cond = Cond.Cond()
        self.__cond.parse()

        # `loop` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.LOOP.value:
            print("If: Expected token {}, got token {}".format(
                t.Tokens.LOOP.value, tokNo))
            return -1
        print("Loop: Consumed `loop` token.")

        # StmtSeq
        self.__stmt_seq = StmtSeq.StmtSeq()
        self.__stmt_seq.parse()

        # `end` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.WHILE.value:
            print("If: Expected token {}, got token {}".format(
                t.Tokens.WHILE.value, tokNo))
            return -1
        print("Loop: Consumed `end` token.")

        # `;` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.SEMICOLON.value:
            print("If: Expected token {}, got token {}".format(
                t.Tokens.SEMICOLON.value, tokNo))
            return -1
        print("Loop: Consumed `;` token.")

        # Successful error code
        return 0

    def exec(self):
        self.__cond.exec()
        while self.__cond.value:
            self.__stmt_seq.exec()
            self.__cond.exec()

    def print(self, indentation):
        print(" " * indentation, end="")
        print("while")
        self.__cond.print(indentation + 4)
        print(" loop")
        self.__stmt_seq.print(indentation + 4)
        print("end")