# Create a Person class with two instance variables to hold a person's first and last names. The names should be passed to the constructor as arguments and stored separately. The first and last names are required and must consist entirely of alphabetic characters.

# The class should also have a getter method that returns the person's name as a full name (the first and last names are separated by spaces), with both first and last names capitalized correctly.

# The class should also have a setter method that takes the name from a two-element tuple. These names must meet the requirements given for the constructor.

class Person:
    @classmethod
    def capitalize_name(cls, first_name, last_name): # I should probably have used an underscore at the start of the method name to indicate its privacy
        return first_name.capitalize() + " " + last_name.capitalize()
    
    @classmethod
    def check_validity(cls, first_name, last_name): # I should probably have used an underscore at the start of the method name to indicate its privacy
        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError("Name must be alphabetic.")
    
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self.check_validity(first_name, last_name)
        self._name = self.capitalize_name(self._first_name, self._last_name)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, names_tuple):
        self.check_validity(names_tuple[0], names_tuple[1])
        self._name = self.capitalize_name(names_tuple[0], names_tuple[1])
            

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel') # This invokes the setter method
print(actor.name)              # This invokes the getter method (it's not simply passing the value of actor.name to print())
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall

character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.