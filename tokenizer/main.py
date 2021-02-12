import sys
from tokenizer import Tokenizer


def main(argv):

    # Open file and handle any errors
    f = open(argv[0], "r")

    # Initialize tokenizer and pass file object
    tokenizer = Tokenizer(f)

    # Loop and print result until we get to it returning an EOF character
    #print("calling getToken()")
    token = tokenizer.getToken()
    error = type(token) is str
    while token != 33 and not error:
        print("{}".format(token), end=" ")
        tokenizer.skipToken()
        token = tokenizer.getToken()
        error = type(token) is str

    if error:
        print("\nERROR: Invalid Token {}".format(token))
    else:
        print("33") # We always exit the loop on an eof; probably a cleaner way, but this works 

    # Close file
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])