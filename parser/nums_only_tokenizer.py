# NOTE: The Tokenizer converts the source code into numerical identifiers and offers a way to look up identifier names and numerical values. As I don't want to get points off for mistakes with my tokenizer, I essentially simulate that with this here, and all the parser/executor/printer methods go from this similified Tokenizer. 
class CustomTokenizer:        

    # Python equivalent of constructor
    def __init__(self, tokens, numbers, ids):
        self.__tokens = tokens # double underscore = private variable
        self.__numbers = numbers 
        self.__ids = ids
        self.__pos = 0
        self.__number_idx = 0
        self.__tokens_idx = 0

    def skipToken(self):
        if not self.__pos == len(self.tokens):
            self.__pos += 1

    def getToken(self):
        if self.__pos >= len(self.__tokens):
            return 33 
        return self.__tokens[self.__pos]

    # Counts what number "number" token we are from the start and returns it from corresponding array
    def get_num(self):
        if self.__tokens[self.__pos] != 31:
            print("get_num called on non-num!")
        return self.__ids[self.__pos]

    # Gets the number corresponding to the current token 
    def get_id(self):
        if self.__tokens[self.__pos] != 32:
            print("get_id called on non-id!")
        return self.__numbers[self.__pos]