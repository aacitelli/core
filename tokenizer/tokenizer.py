# RegEx for checking identifier validity 
import re 

class Tokenizer:

    tokenToID = {
        "program": 1,
        "begin": 2,
        "end": 3,
        "int": 4,
        "if": 5,
        "then": 6,
        "else": 7,
        "while": 8,
        "loop": 9,
        "read": 10,
        "write": 11,
        ";": 12,
        ",": 13,
        "=": 14,
        "!": 15,
        "[": 16,
        "]": 17,
        "&&": 18,
        "||": 19,
        "(": 20,
        ")": 21,
        "+": 22,
        "-": 23,
        "*": 24,
        "!=": 25,
        "==": 26,
        "<": 27,
        ">": 28,
        "<=": 29,
        ">=": 30
    }

    idToToken = {
        1: "program",
        2: "begin",
        3: "end",
        4: "int",
        5: "if",
        6: "then",
        7: "else",
        8: "while",
        9: "loop",
        10: "read",
        11: "write",
        12: ";",
        13: ",",
        14: "=",
        15: "!",
        16: "[",
        17: "]",
        18: "&&",
        19: "||",
        20: "(",
        21: ")",
        22: "+",
        23: "-",
        24: "*",
        25: "!=",
        26: "==",
        27: "<",
        28: ">",
        29: "<=",
        30: ">="
        # 31 = Integer
        # 32 = Identifier
        # 33 = EOF
    }

    def __init__(self, f):
        self.f = f
        self.line = f.readline().strip()

    # Returns (info about) current token;
    # Repeated calls to getToken() return the same token
    # Precondition: The first character of self.line() is the beginning of our character and is not whitespace
    def getToken(self):

        # If we start out not immediately on a token (due to stuff skipToken sets), we know we're at EOF
        if len(self.line) == 0:
            # print("getToken: Returning EOF token.")
            return 33

        # Loop until we get (1) End of line or (2) White space
        token = ""
        pos = 0
        while pos < len(self.line) and self.line[pos] != " ":
            token += self.line[pos]
            pos += 1
            #print("token {} from pos {}".format(token, pos))

        # If it's one of our vanilla special characters
        if token in self.tokenToID:
            # print("getToken: Returning {} token.".format(token))
            return self.tokenToID[token]

        # Debug 
        # print("Special Character {}".format(token))

        # Check if it's an integer
        if token.isdigit():
            # print("getToken: Returning {} token.".format(token))
            return 31

        # Check if it's a valid identifier using RegEx 
        '''
        Seemed like a fun place to use RegEx. Learned a ton figuring this out. 
        Walkthrough:
        - ^$ = Wandates we match the entire string, not just subsets
        - (?=.{0,8}$) = Lookahead expression that mandates length
        - [A-Z][A-Z]*\d* = Mandates order and actual content 
        '''
        if re.search(r"^(?=.{0,8}$)[A-Z][A-Z]*\d*$", token) != None:
            return 32

        # Otherwise, error out (return the token we errored on; main knows to look for this)
        return token  

    # Skips current token; next getToken() call will return new token
    # AKA moves our input such that the current beginning of the line is the next character
    def skipToken(self):

        # print("Line pre-skipToken(): {}".format(self.line))

        # Strip our line to be sure
        self.line = self.line.strip()

        # If we're at the very end of a line, read in a new line, strip it, and return 
        if not len(self.line):
            self.line = self.f.readline()
            return

        # Keep trimming stuff off until we either:
        # (1) Get to a newline, meaning we should read in a new line, then strip it, then return 
        # (2) Get to a space, meaning we should strip our current line then return 
        while len(self.line) and self.line[0] != "\n" and self.line[0] != " ":
            self.line = self.line[1:]
            # print("self.line: {}".format(self.line))
        if not len(self.line) or self.line[0] == "\n":
            self.line = self.f.readline().strip()
        else:
            self.line = self.line.strip()

        # print("Line post-skipToken(): {}".format(self.line))

    # Returns the value of the current (integer) token
    # Errors out if the current token is not an integer
    def intVal(self, str):
        pass

    # Returns the name (string) of the current (id) token
    # Errors out if the current token is not an id
    def idName(self, str):
        pass