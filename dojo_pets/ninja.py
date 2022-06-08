from pet import Pet


class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet, noise):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        self.noise = noise

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        print(self.noise)
        return self


# implement __init__( name , type , tricks ):

# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
