
class Human:
    def __init__(self, first_name, last_name, age, height, weight, gender):
        # these are the attributes of the class
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.gender = gender
        self.weight = weight

# methods are actions
    def say_name(self):
        print(f'My name is {self.first_name} {self.last_name}')

    def lose_weight(self, amount):
        # current weight minus current weight
        self.weight -= amount


tom = Human('tom', 'harris', 33, 6, "male")
kyle = Human('kyle', 'arris', 43, 6, "male")

tom.say_name()
kyle.say_name()


print(tom.weight)
tom.lose_weight(30)
