import character
from random import randrange

class Combat:
    def __init__(self, participants):
        self.participants = participants

    def attack(self, target):
        roll = randrange(100)
        if roll >= 10:
            print("Hit!")
            target.health.damage(10)
            print(f"{target.name} takes {10} damage")

            if target.health.get_health() <= 0:
                self.kill(target)
        else:
            print("Miss!")

    def kill(self, target):
        self.participants.remove(target)
        print(f"{target.name} was killed!")
