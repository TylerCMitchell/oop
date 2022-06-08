from ninja import Ninja
from pet import Pet


dog_treats = ['none']
dog_food = ['Super Kibble']

krypto = Pet("Krypto", "Super-Dog", ['FLIES AROUND'], noise="Bark!")

Superman = Ninja("Clark", "Kent", dog_treats, dog_food, krypto, noise="Bark!")


Superman.walk().feed().bathe()
