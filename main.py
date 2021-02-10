import sys 
from tokenizer import Tokenizer

def main(argv):

    # Open file and handle any errors 
    file = open(argv[0], "r")

    # Initialize tokenizer and pass file object 
    Tokenizer(file)

    # Close file
    file.close()
    
if __name__ == "__main__":
    main(sys.argv[1:])