import t 
import DeclSeq
import StmtSeq

class Prog():

    def __init__(self):
        self.__declseq = None
        self.__stmtseq = None

    def parse(self):

        # `program` token 
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != 1:
            print("Expected token {}, got token {}".format(1, tokNo))
            return -1 

        # DeclSeq
        self.__declseq = DeclSeq.DeclSeq()
        self.__declseq.parse()

        # `begin` token 
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != 2:
            print("Expected token {}, got token {}".format(2, tokNo))
            return -1 

        # StmtSeq
        self.__stmtseq = StmtSeq.StmtSeq()
        self.__stmtseq.parse()

        # `end` token 
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != 3:
            print("Expected token {}, got token {}".format(3, tokNo))
            return -1 

        # Successful error code 
        return 0 

    def exec(self):
        self.__declseq.exec()
        self.__stmtseq.exec()

    def print(self):
        print("program")
        self.__declseq.print()
        print("begin")
        self.__stmtseq.print()
        print("end")