from classes.animal import Animal

class Dog(Animal):
    def __init__(self, name,owner,breed,color):
        super().__init__(name,owner)
        self.breed= breed
        self.color= color

    def print_info(self):
        super().print_info()
        print

