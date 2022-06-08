
class Pet:

    def __init__(self, name, type, trick, noise):
        self.name = name
        self.type = type
        self.trick = trick
        self.health = 85
        self.energy = 75
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("Bark!")
        return self


class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


dog_treats = ['none']
dog_food = ['Super Kibble']

krypto = Pet("Krypto", "Super-Dog", ['FLIES AROUND'], noise="Bark!")

Superman = Ninja("Clark", "Kent", dog_treats, dog_food, krypto)


Superman.walk().feed().bathe()

# implement __init__( name , type , tricks ):

# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
