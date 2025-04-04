# Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

class Food:

    def __init__(self, food_name, quality):
        self.food_name = food_name
        self.quality = quality

    def description(self):
        print(f'{self.food_name} is delicious and tastes very {self.quality}')

pasta = Food('spaghetti', 'mediterranean')
pasta.description()

curry = Food('korma', 'spicy')
curry.description()