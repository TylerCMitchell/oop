# Importing the ninja and pirate files
from classes.ninja import Ninja
from classes.pirate import Pirate
import time
# Importing a module that holds the sleep function that we are using.

# defining a class called game. game inheriting classes ninja and pirate (parents)


class Game(Ninja, Pirate):
    # Setting global attribute for the game class
    current_tick = 0

# Controller function
    def __init__(self):
        # Storing an instance of ninja
        self.michelangelo = Ninja("Michelangelo")
        self.jack_sparrow = Pirate("Jack Sparrow")
        self.current_tick = 0

    def tick(self):  # defining a function called tick
        # setting our 'tick' to .1 second, telling program to pause .1 sec
        time.sleep(.1)
        # incrementing the current tick attribute to the current instance of the game class
        self.current_tick += 1


# This is our menu
print("1) Start new game")
print("2) Exit game")

# Option variable that will be input 1 or 2, determining the players choice to begin or end
option = input("Enter an option")

# Conditional that instructs what to do based on the what the input is
if(option == "1"):
    new_game = Game()
elif(option == "2"):
    print("Goodbye")

# Creating a while loop
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

# Conditional checking who hits '0' first
if(new_game.michelangelo.health <= 0 and new_game.jack_sparrow.health > 0):
    print("Jack Sparrow is the winner.")
elif(new_game.jack_sparrow.health <= 0 and new_game.michelangelo.health > 0):
    print("Michelangelo is the winner.")

# Our next step was to create interactivity with the player getting to choose different attacks, as is this code predetermines that Michelangelo will hit '0' before Jack Sparrow
print("1) Start new game")
print("2) Exit game")

# Another chance to choose option variable that will be input 1 or 2, determining the players choice to begin or end
option = input("Enter an option")
