import CustomTokenizer
import t
import Prog 

# Initialize tokenizer instance; see Tokenizer.py for a better description of what this means 
# tokens: A list of tokenized numbers corresponding to the program.
# numbers: A list of numbers; note that len(numbers) == # of "31" Tokens 
# ids: A list of ids; note that len(ids) == # of "32" Tokens 
tokens = [ 1, 4, 32, 12, 2, 32, 14, 31, 12, 11, 32, 12, 3, 33 ]
numbers = [ 25 ]
ids = [ "X", "X", "X" ]
t.tokenizer = CustomTokenizer.CustomTokenizer(tokens, numbers, ids)

# Parse 
program = Prog.Prog()

# Execute

# Print 

# Exit 

first_token = t.tokenizer.get_token()
if first_token != 1:
    print("First token must be program!")
    exit(-1)