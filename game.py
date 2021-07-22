from combat import Combat
from player import Player
from character import Character

def run_game():
    """The main game loop"""
    player = Player("Player", 100, 0, [])
    goblin = Character("Goblin", 20, 0, [])
    characters = [player, goblin]

    while True:
        player_input = input("[Exploring] What would you like to do? ")
        if player_input == "hit":
            combat = Combat(characters)
            while len(combat.participants) > 1:
                player_input = input("[Combat] What would you like to do? ")
                if player_input == "hit":
                    combat.attack(goblin)
            print("Combat over")

        if player_input[0].lower() == "q":
            print("Thanks for playing!")
            break

run_game()
