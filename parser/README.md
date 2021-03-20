## Notes to the Grader
- Tested w/ Python 3.9.1; any version of Python3 would probably work 
- Example run: `python main.py tests/everything.txt` 
- Tokenizer Issues
    - While I *think* it works properly, I don't feel confident using my tokenizer without spaces between the tokens. Please create spaces between tokens.
    - My tokenizer doesn't handle empty lines with more than a newline on them very well (i.e. a line with just a few empty spaces). Ensure empty lines are just a newline character.
- I've included a few test cases (already spaced out). These include the three given for the tokenizer as well as the one someone put together on Piazza that tests every case, `everything.txt`. 