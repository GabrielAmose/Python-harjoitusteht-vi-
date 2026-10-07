class Player:    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ending = set()

    #Adds a newly found ending to a set()
    def add_ending(self, end_name):
        self.ending.add(end_name)