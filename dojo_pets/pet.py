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
        print(self.noise)
