import t 
import Let 
import Int 

class Id():

    def __init__(self):
        self.__identifier = None 

    # Static set of ids and what's essentially a static method 
    ids = set() 
    @classmethod
    def id_exists(cls, id):
        return id in cls.ids