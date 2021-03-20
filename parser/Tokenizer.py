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

    # Used to compare if a given character can start off our chain; so, we truncate anything that's two long to just be the first characters and eliminate duplicates
    specialCharacters = {
        ";", ",", "=", "!", "[", "]", "&", "|", "(", ")", "+", "-", "*", "<",
        ">"
    }

    # List of 3-tuples such that:
    # 1st Value = The token value (i.e. 1-34)
    # 2nd Value = The string value of the token (filled if identifier)
    # 3rd Value = The integer value of the token (filled if integer)
    most_recent_valid_token = None

    # Holds the value of line() after our next token
    # We update this at the end of every getToken() call, and call getToken() in skipToken(),
    #   so that all we have to do in skipToken() is simply read in a new line if it's empty or set our old line equal to this new line
    line_after_trim = ""

    def __init__(self, f):
        self.f = f
        self.line = f.readline().strip()

    def set_recent_token(self, val):
        self.most_recent_valid_token = val

    # Returns (info about) current token;
    # Repeated calls to getToken() return the same token
    # Precondition: Excepting whitespace at the beginning, first character is the first character of our next token.
    def get_token(self):

        # If we start out not immediately on a token (due to stuff skipToken sets), we know we're at EOF
        if self.line == "":
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
                if token + char == "!" and pos < len(
                        self.line) and self.line[pos] == "=":
                    self.line_after_trim = self.line[pos + 1:]
                    return 25
                if token + char == "=" and pos < len(
                        self.line) and self.line[pos] == "=":
                    self.line_after_trim = self.line[pos + 1:]
                    return 26
                if token + char == "<" and pos < len(
                        self.line) and self.line[pos] == "=":
                    self.line_after_trim = self.line[pos + 1:]
                    return 26
                if token + char == ">" and pos < len(
                        self.line) and self.line[pos] == "=":
                    self.line_after_trim = self.line[pos + 1:]
                    return 26

                # print("Detected in tokenToID.")
                self.line_after_trim = self.line[pos:]

                # If it's not at end of line, we have to check next character to make sure it is either a separator or a special character
                if len(self.line_after_trim):
                    if self.tokenToID[token + char] not in range(
                            12, 30) and self.line_after_trim[0] != " ":
                        print("ERROR: Invalid token!")
                        return -1

                return self.tokenToID[token + char]

            # If we are about to add a special character:
            # - If it's a valid number or identifier, split it there
            # - If it's not a valid number or identifier, error out
            if char in self.specialCharacters and token != "":
                # print("Special character connected! Char: {}".format(char))
                if self.isValidNumber(token):
                    # print("It's a number!")
                    self.set_recent_token(int(token))
                    self.line_after_trim = self.line[pos - 1:]
                    return 31
                if self.isValidIdentifier(token):
                    # print("{} is an identifier!".format(token))
                    self.set_recent_token(token)
                    self.line_after_trim = self.line[pos - 1:]
                    return 32
                else:
                    print(
                        "\nERROR: Special character without prior whitespace not preceded by a number or identifier!"
                    )
                    return -1

            # Add on the new one
            token += char
            # print("token: {}".format(token))
            # print("Token: {}".format(token))

        # If we get out without an error but without recognizing a character, test for identifier/number (i.e. end of line)
        if self.isValidNumber(token):
            self.set_recent_token(int(token))
            self.line_after_trim = self.line[pos:]
            return 31
        if self.isValidIdentifier(token):
            self.set_recent_token(token)
            self.line_after_trim = self.line[pos:]
            return 32

        print("\n114: ERROR: Invalid token \"{}\"".format(token))
        return -1

        # Otherwise, error out (return the string token we errored on; main knows to look for this)
        # return token

    # Skips current token; next getToken() call will return new token
    # AKA moves our input such that the current beginning of the line is the next character
    def skip_token(self):
        # print("Line pre-skipToken(): {}".format(self.line))
        self.get_token(
        )  # Don't care about the return code, we just need it to update self.line_after_trim
        # print("line_after_trim: {}".format(self.line_after_trim))
        self.line_after_trim.strip()

        # Existing line is empty
        if not len(self.line_after_trim):
            self.line = self.f.readline()
            stripped_copy = self.line.strip()
            while self.line == "\n" or (len(self.line) > 0
                                        and len(stripped_copy) == 0):
                self.line = self.f.readline()
                stripped_copy = self.line.strip()
                # print("newline: {}".format(self.line))
            # print("read in this line: \"{}\"".format(self.line))
        else:
            self.line = self.line_after_trim
        # print("Line post-skipToken(): {}".format(self.line))

    # Returns actual value of the number currently at get_token
    def get_int(self):
        if self.get_token() != 31:
            print("ERROR: get_int called on non-integer value!")
            return -1
        return self.most_recent_valid_token

    # Returns actual string of the identifier currently at get_token
    def get_id(self):
        if self.get_token() != 32:
            print("ERROR: get_id called on non-id value!")
            return -1
        return self.most_recent_valid_token

    # See file regex.md for an explanation of this
    def isValidIdentifier(self, str):
        return re.search(r"^(?=.{1,8}$)[A-Z][A-Z]*\d*$", str) != None

    # Valid numbers in our language must be eight or fewer digits
    def isValidNumber(self, str):
        if not str.isdigit():
            return False
        return int(str) <= 99999999