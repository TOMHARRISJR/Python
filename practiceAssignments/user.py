class User:
    
    def __init__(self, first_name, last_name, email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    
    
    
    def display_info(self):
        print(f"First: {self.first_name}") 
        print(f"Last: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points:{self.gold_card_points} ")
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("User already member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):

        if self.gold_card_points < amount:
            "Nice try but you dont have enough points!"
            return self
        self.gold_card_points = self.gold_card_points - amount
        return self





my_user = User("Tom","Harris","tom@gmail.com", 33)
my_user.display_info().enroll().spend_points(85).display_info()

# my_user.enroll()
# my_user.display_info()
# my_user.spend_points(85)
# my_user.display_info()










