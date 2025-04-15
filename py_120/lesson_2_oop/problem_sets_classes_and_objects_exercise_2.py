class Person:
    # See the suggested solution for a better way of handling the name input that won't output any empty spaces on line 9.
    def __init__(self, first_name):
        self._first_name = first_name
        self._last_name = ''

    @property
    def name(self):
        return self._first_name + " " + self._last_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith