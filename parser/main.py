import sys
from ParseTree import ParseTree
if __name__ == "__main__":

    # Check that user passed in name of a file 
    if len(sys.argv[1] <= 1):
        print("ERROR: Must pass in file name as first command-line argument!")

    # Read in our file
    f = open(sys.argv[1], "r")
    if not f:
        print("Error reading file {}".format(sys.argv[1]))

    # Init ParseTree Object 
    parseTree = ParseTree()

    # Iterate token by token, processing each one and building our scene tree 
    for line in f:
        parseTree.handleToken(int(line))

    # Close file
    f.close()