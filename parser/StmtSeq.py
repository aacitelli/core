import t 
import Stmt 

class StmtSeq():

    def __init__(self):
        self.__stmt = None 
        self.__stmt_seq = None

    def parse(self):

        # We know we have >= 1 statement regardless, so go ahead and parse it
        self.__stmt = Stmt.Stmt()
        self.__stmt.parse()

        # Use one-token lookahead to determine if are at the second alternative 
        tokNo = t.tokenizer.get_token()
        if tokNo == t.Tokens.IDENTIFIER.value or tokNo == t.Tokens.IF.value or tokNo == t.Tokens.WHILE.value or \
            tokNo == t.Tokens.READ.value or tokNo == t.Tokens.WRITE.value:
            self.__stmt_seq = StmtSeq()
            self.__stmt_seq.parse()
        
        # Successful error code
        return 0

    def exec(self):
        self.__stmt.exec()
        if self.__stmt_seq != None:
            self.__stmt_seq.exec()

    def print(self, indentation):
        print(" " * indentation, end="")
        self.__stmt.print(0)
        if self.__stmt_seq != None:
            self.__stmt_seq.print(indentation)