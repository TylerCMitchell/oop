from classes.ninja import Ninja
from classes.pirate import Pirate
import time


class Game(Ninja, Pirate):
    current_tick = 0

    def __init__(self):
        self.michelangelo = Ninja("Michelangelo")
        self.jack_sparrow = Pirate("Jack Sparrow")
        self.current_tick = 0

    def tick(self):
        time.sleep(.1)
        self.current_tick += 1


print("1) Start new game")
print("2) Exit game")

option = input("Enter an option")

if(option == "1"):
    new_game = Game()
elif(option == "2"):
    print("Goodbye")

while(new_game.michelangelo.health > 0 and new_game.jack_sparrow.health > 0):
    if(new_game.current_tick == 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    elif(new_game.current_tick % new_game.michelangelo.speed == 0 and new_game.current_tick % new_game.jack_sparrow.speed == 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    elif(new_game.current_tick % new_game.michelangelo.speed == 0 and new_game.current_tick % new_game.jack_sparrow.speed != 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.tick()
    elif(new_game.current_tick % new_game.jack_sparrow.speed == 0 and new_game.current_tick % new_game.michelangelo.speed != 0):
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    else:
        new_game.tick()
    new_game.michelangelo.show_stats()
    new_game.jack_sparrow.show_stats()

if(new_game.michelangelo.health <= 0 and new_game.jack_sparrow.health > 0):
    print("Jack Sparrow is the winner.")
elif(new_game.jack_sparrow.health <= 0 and new_game.michelangelo.health > 0):
    print("Michelangelo is the winner.")

print("1) Start new game")
print("2) Exit game")

option = input("Enter an option")
