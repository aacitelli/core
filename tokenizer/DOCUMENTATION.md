# Interpreter: DOCUMENTATION
By: Anden Acitelli.2

# Overall Tokenizer Design
First, let's define the inputs and outputs of the system.

- **Input(s)**: The name of a file that is our source code. 
- **Output(s)**: A sequence of numbers representing the numerical tokenization of the provided source code file. 

The Tokenizer first opens the file and makes sure the file was opened correctly. 

Then, it initializes a copy of the Tokenizer. The Tokenizer keeps track of the following member variables: 

- **tokenToID**: An object that lets us easily map from plaintext tokens to their numerical equivalent, and verify if a given string is a valid plaintext token. 
    - Note that 31/32/33 (numbers, identifiers, and EOF respectively) are handled on a case by case basis.
- **specialCharacters**: A set object that is used to see if a given character is a special character. This includes all numerical tokens from 12-30.
    - Note that, as I only use this set in circumstances where I care only about the first character, I trimmed any special characters that were more than one digit, then got rid of duplicates.
- **tokens**: A list of 3-tuples with the following data:
    - The token's numerical equivalent, which occurs with every token
    - The token's associated number, if it's a number (i.e. token ID #31). Set to `None` if it's not a number.
    - The token's associated identifier, if it's an identifier (i.e. token ID #32). Set to `None` if it's not an identifier.
    - Note that we need to save this because the output of the tokenizer itself is just the numbers, so identifiers and numbers get collapsed to just being the token (31/32), and we need to save that actual value somewhere. 
- **line**: Where we currently are in the input, essentially. The 0th position of this is always either the beginning of our next token, or a whitespace immediately preceding our next token.
- **line_after_trim**: I go into more depth on this later when I'm explaining skipToken(). 

The Tokenizer has the following functions: 

- **__init__** (the constructor): Saves a reference to the file pointer, and reads in a line of the file. Just basic setup stuff.
- **skipToken()**: Moves our current "position" one token forward. 
    - Every time getToken() runs, it updates what our current line will look like after we get rid of a token. 
    - So, all I have to do in skipToken() is (1) Read in a line, if it's empty or (2) Set our current line representation to what getToken() saved to that variable, which essentially trims the token. 
- **getToken()**: Returns the token that starts at the beginning of line.
    - Note that we call string.strip() at the beginning of this, which will get rid of any leading or trailing whitespaces.
    - This also updates line_after_trim, which is what line would look like if we were to slash off a token. 
- **intVal()**: <TODO> Works with the tokens member to return the actual number for a given number.
- **idName()**: <TODO> Works with the tokens member to return the actual identifier for a given identifier.
- **isValidIdentifier()**: Uses regex to identify whether a given string is a valid identifier (i.e. starts with a capital, then has a string of capitals then numbers such that the whole thing is <= 8 in length)

## User Manual
To use the Tokenizer, simply initialize the Tokenizer class, passing in a file object to the constructor. Then, alternate `getToken()` and `skipToken()` calls, printing out the result. This will print out what Professor Soundarajan is looking for, which is the sequence of numbers.

## Test Process
I did the following to test my system:
- Ran the three test cases Professor Soundarajan provided us on Piazza.
- Ran a "===XY" case, as the document specifically noted that 
- Tested the following edge cases:
    - Empty file, which should print out nothing (except EOF)
    - File that's a bunch of empty lines before the program even starts

## Known Remaining Bugs
None that I know of. 