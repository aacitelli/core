# RegEx for checking identifier validity 
import re 

# Project = Wednesday
# 3231 Quiz = Tomorrow
# 3801 HW = Fri
# 3341 HW2 = Fri

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

    # Used to compare if a given character can start off our chain; so, we truncate anything that's two long to just be the first characters and eliminate duplicates
    specialCharacters = { ";", ",", "=", "!", "[", "]", "&", "|", "(", ")", 
        "+", "-", "*", "<", ">" } 

    # List of 3-tuples such that:
    # 1st Value = The token value (i.e. 1-34)
    # 2nd Value = The string value of the token (filled if identifier)
    # 3rd Value = The integer value of the token (filled if integer)
    tokens = [] 

    # Holds the value of line() after our next token 
    # We update this at the end of every getToken() call, and call getToken() in skipToken(), 
    #   so that all we have to do in skipToken() is simply read in a new line if it's empty or set our old line equal to this new line 
    line_after_trim = ""

    def __init__(self, f):
        self.f = f
        self.line = f.readline().strip()

    # Returns (info about) current token;
    # Repeated calls to getToken() return the same token
    # Precondition: Excepting whitespace at the beginning, first character is the first character of our next token.
    def getToken(self):

        # If we start out not immediately on a token (due to stuff skipToken sets), we know we're at EOF
        if not self.line:
            return 33

        # Strip our line to eliminate whitespace at the beginning
        self.line = self.line.strip()
        # print("Length: {}".format(len(self.line)))

        token = ""
        pos = 0
        while pos < len(self.line) and self.line[pos] != " ":

            # Character we are about to add
            char = self.line[pos]
            # print("char: {}".format(char))
            pos += 1
            # print("pos: {}".format(pos))

            # If it will give us something in tokenToID, return that
            # print("token + char: ".format((token + char)))
            if token + char in self.tokenToID:

                # Check to see if we can be greedier 
                if token + char == "!" and pos < len(self.line) and self.line[pos] == "=":
                    self.line_after_trim = self.line[pos + 1:]
                    return 25
                if token + char == "=" and pos < len(self.line) and self.line[pos] == "=":
                    self.line_after_trim = self.line[pos + 1:]
                    return 26
                if token + char == "<" and pos < len(self.line) and self.line[pos] == "=":
                    self.line_after_trim = self.line[pos + 1:]
                    return 26
                if token + char == ">" and pos < len(self.line) and self.line[pos] == "=":
                    self.line_after_trim = self.line[pos + 1:]
                    return 26

                # print("Detected in tokenToID.")
                self.line_after_trim = self.line[pos:]

                # If it's not at end of line, we have to check next character to make sure it is either a separator or a special character
                if len(self.line_after_trim):
                    if self.tokenToID[token + char] not in range(12, 30) and self.line_after_trim[0] != " ":
                        print("ERROR: Invalid token!")
                        return -1 

                return self.tokenToID[token + char]

            # If we are about to add a special character:
            # - If it's a valid number or identifier, split it there
            # - If it's not a valid number or identifier, error out 
            if char in self.specialCharacters:
                # print("Special character connected! Char: {}".format(char))
                if self.isValidNumber(token):
                    # print("It's a number!")
                    self.tokens.append((31, None, int(token)))
                    self.line_after_trim = self.line[pos - 1:]
                    return 31
                if self.isValidIdentifier(token): 
                    # print("{} is an identifier!".format(token))
                    self.tokens.append((32, token, None))
                    self.line_after_trim = self.line[pos - 1:]
                    return 32
                else: 
                    print("\nERROR: Special character without prior whitespace not preceded by a number or identifier!")
                    return -1

            # Add on the new one 
            token += char
            # print("token: {}".format(token))
            # print("Token: {}".format(token))

        # If we get out without an error but without recognizing a character, test for identifier/number (i.e. end of line)
        if self.isValidNumber(token):
            self.tokens.append((31, None, int(token)))
            self.line_after_trim = self.line[pos:]
            return 31
        if self.isValidIdentifier(token): 
            self.tokens.append((32, token, None))
            self.line_after_trim = self.line[pos:]
            return 32

        print("\n114: ERROR: Invalid token \"{}\"".format(token))
        return -1 
            
        # Otherwise, error out (return the string token we errored on; main knows to look for this)
        # return token  

    # Skips current token; next getToken() call will return new token
    # AKA moves our input such that the current beginning of the line is the next character
    def skipToken(self):
        # print("Line pre-skipToken(): {}".format(self.line))
        self.getToken() # Don't care about the return code, we just need it to update self.line_after_trim 
        # print("line_after_trim: {}".format(self.line_after_trim))
        self.line_after_trim.strip()

        # Existing line is empty
        if not len(self.line_after_trim):
            self.line = self.f.readline()
            while self.line == "\n":
                self.line = self.f.readline()
                # print("newline: {}".format(self.line))
            # print("read in this line: \"{}\"".format(self.line))
        else:
            self.line = self.line_after_trim
        # print("Line post-skipToken(): {}".format(self.line))

    # Returns the value of the current (integer) token
    # Errors out if the current token is not an integer
    def intVal(self, str):
        if self.tokens[len(tokens) - 1][2] is None:
            print("ERROR: intVal called on non-integer value!")
            return "ERROR"
        return tokens[len(tokens) - 1][2]

    # Returns the name (string) of the current (id) token
    # Errors out if the current token is not an id
    def idName(self, str):
        if self.tokens[len(tokens) - 1][1] is None:
            print("ERROR: intVal called on non-integer value!")
            return "ERROR"
        return tokens[len(tokens) - 1][1]

    # See file regex.md for an explanation of this 
    def isValidIdentifier(self, str):
        return re.search(r"^(?=.{1,8}$)[A-Z][A-Z]*\d*$", str) != None

    # Valid numbers in our language must be eight or fewer digits
    def isValidNumber(self, str):
        if not str.isdigit(): 
            return False 
        return int(str) <= 99999999