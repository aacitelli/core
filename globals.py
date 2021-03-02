from tokenizer.tokenizer import Tokenizer

def setup(f):
    global tokenizer
    tokenizer = Tokenizer(f)