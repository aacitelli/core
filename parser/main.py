import Tokenizer
import t  # file we store globals in (i.e. the tokenizer and various enums)
import Prog
import sys


def main(argv):

    # Open file and handle any errors
    f = open(argv[0], "r")

    # Init file used to track our globals
    t.tokenizer = Tokenizer.Tokenizer(f)

    # Init top-level object
    program = Prog.Prog()

    # Form parse tree, which recursively calls parse() on each nonterminal
    program.parse()

    # Recursively print parse tree out
    print("\nPretty Printed: ")
    program.print()

    # Recursively execute parse tree
    print("\nProgram Output: ")
    program.exec()

    # Close file
    f.close()

    # Exit
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])