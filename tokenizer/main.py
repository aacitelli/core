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
    while token != 33:
        print("{}".format(token), end=" ")
        #print("calling skipToken()")
        tokenizer.skipToken()
        #print("calling getToken()")
        token = tokenizer.getToken()
    print("33") # We always exit the loop on an eof; probably a cleaner way, but this works 

    # Close file
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])