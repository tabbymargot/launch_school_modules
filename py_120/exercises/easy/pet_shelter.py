class Pet:
    def __init__(self, animal, pet_name):
        self._animal = animal
        self._pet_name = pet_name
        
class Owner(Pet):
    def __init__(self, owner_name):
        self._owner_name = owner_name

class Shelter(Owner):
    def __init__(self):
        self.adoptions = {}

    def adopt(self, owner, pet):
        self.adoptions.setdefault(owner._owner_name, [])
        self.adoptions[owner._owner_name].append({pet._pet_name: pet._animal})

    def print_adoptions(self):
        for owner in self.adoptions:
            print(f'{owner} has adopted the following pets')
            pet_list = self.adoptions[owner]
            for pet in pet_list:
                for pet_name, pet_type in pet.items():
                    print(f'a {pet_type} named {pet_name}')


cocoa   = Pet('cat', 'Cocoa')
# print(cocoa._animal, cocoa._pet_name)
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
# print(phanson._owner_name)
bholmes = Owner('B Holmes')

self = Shelter()
self.adopt(phanson, cocoa)
self.adopt(phanson, cheddar)
self.adopt(phanson, darwin)
self.adopt(bholmes, kennedy)
self.adopt(bholmes, sweetie)
self.adopt(bholmes, molly)
self.adopt(bholmes, chester)

self.print_adoptions()



# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.



# print(f"{phanson.pet_name} has {phanson.number_of_pets()} "
#     "adopted pets.")
# print(f"{bholmes.pet_name} has {bholmes.number_of_pets()} "
#     "adopted pets.")

