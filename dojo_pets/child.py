import parent

dog_treats = ['none']
dog_food = ['Super Kibble']

krypto = parent.Pet("Krypto", "Super-Dog", ['FLIES AROUND'],
                    health=85, energy=75, noise="Bark!")

Superman = parent.Ninja("Clark", "Kent", dog_treats, dog_food, krypto)


Superman.walk().feed().bathe()
