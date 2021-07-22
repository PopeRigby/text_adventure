from player import Player

def run_game():
    """The main game loop"""
    player = Player(100, 0, [])

    while True:
        player_input = input("What would you like to do? ")
        if player_input == "q":
            print("Thanks for playing!")
            break

run_game()
