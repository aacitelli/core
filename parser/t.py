tokenizer = None

from enum import Enum 
class Tokens(Enum):
    PROGRAM = 1
    BEGIN = 2
    END = 3
    INT = 4
    IF = 5
    THEN = 6
    ELSE = 7
    WHILE = 8 
    LOOP = 9
    READ = 10
    WRITE = 11
    SEMICOLON = 12
    COMMA = 13
    EQUALS = 14
    EXCLAMATION_POINT = 15
    OPEN_BRACKET = 16
    CLOSED_BRACKET = 17
    DOUBLE_AND = 18
    DOUBLE_OR = 19
    OPEN_PAREN = 20
    CLOSED_PAREN = 21
    PLUS = 22
    MINUS = 23
    STAR = 24
    NOT_EQUALS = 25
    DOUBLE_EQUALS = 26
    LESS_THAN = 27
    GREATER_THAN = 28
    LESS_THAN_OR_EQUAL_TO = 29
    GREATER_THAN_OR_EQUAL_TO = 30
    NUMBER = 31
    IDENTIFIER = 32