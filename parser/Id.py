import t 
import Int 

class Id():

    def __init__(self):
        self.__id = None # If not None, we know this is a duplicate. In that case, contains a reference to the original copy. 
        self.__identifier = None
        self.__value = None 
        self.__is_original = None
        self.__was_declared = False

    # Static set of ids and what's essentially a static method 
    ids = set() 
    @classmethod
    def id_exists(cls, id):
        return id in cls.ids

    def parse(self):

        tokNo = t.tokenizer.get_token()
        if tokNo != t.Tokens.IDENTIFIER.value:
            print("Id: Expected token {}, got token {}".format(t.Tokens.IDENTIFIER.value, tokNo))
            return -1 

        # Grab the current id from the tokenizer (we need the actual id name, not just the numeric token)
        identifier = t.tokenizer.get_id()

        # If it's a token that already exists, set this class up as a pointer to the first initialized copy of this id 
        exists_already = False
        for id_object in self.ids:
            if id_object.__identifier == identifier:
                self.__id = id_object
                exists_already = True
                break

        # If it doesn't, this is our first reference, which holds __identifier and __values
        if not exists_already:
            self.__identifier = identifier
            self.__was_declared = True 
            self.__is_original = True
            self.ids.add(self)
        else:
            self.__is_original = False 

        t.tokenizer.skip_token()

    # Essentially, if I pass in a value as the first parameter, this acts as a setter method that returns the value set.
    # Otherwise, it acts like a getter method.
    # If declare is not None, then this is part of a Decl sequence 
    # If assign is not None, then this is part of an Assign statement
    def exec(self, declare, assign):
        
        # Error if trying to declare when already declared
        if self.__id is not None and declare is not None:
            print("Id ERROR: Variable {} declared more than one time!".format(self.__id.__identifier))
            return -1 

        # If this class is a pointer, just pass the exec() call to that one
        if self.__id is not None:
            return self.__id.exec(declare, assign)

        # We haven't seen this before; Error if referencing undeclared variable 
        if self.__is_original and not self.__was_declared:
            print("Id ERROR: Variable {} referenced before declaration!".format(self.__identifier))
            return -1 

        # We're declaring
        if declare is not None:
            self.__was_declared = True 

        # We're initializing!
        elif assign is not None: 
            self.__value = assign

        # We're WTF WE SHOULDN'T BE HERE GET OUT GET OUT GET OUT 
        else: 
            print("Id ERROR: Shouldn't get here!")      

        # We return value, as that's always what we want during execution, and the actual id itself is only used when printing
        return self.__value

    def print(self, indentation):
        print(" " * indentation, end="")
        if self.__id is not None:
            self.__id.print(indentation)
        else:
            print(self.__identifier, end="")

    def print_value(self, indentation):
        print(" " * indentation, end="")
        if self.__is_original:
            print(self.__value, end="")
        else:
            self.__id.print_value(0)

    def read_in_value(self):
        if self.__is_original:
            self.__value = input("{}: ".format(self.__identifier))
        else:
            self.__id.read_in_value()