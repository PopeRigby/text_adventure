"""Class for all characters including player"""

class Character:
    def __init__(self, name, starting_health=100, starting_gold=0, starting_items=[]):
        self.name = name
        self.health = Health(starting_health)
        self.gold = Gold(starting_gold)
        self.inventory = Inventory(starting_items)

class Health:
    def __init__(self, starting_value):
        self.health = starting_value

    def get_health(self):
        return self.health

    def heal(self, amount):
        self.health += amount
        return self.health

    def damage(self, amount):
        self.health -= amount
        return self.health

class Gold:
    def __init__(self, starting_value):
        self.gold = starting_value

    def get_gold(self):
        return self.gold

    def loot_gold(self, amount):
        self.gold += amount
        return self.gold

    def drop_gold(self, amount):
        self.gold -= amount
        return self.gold

class Inventory:
    def __init__(self, starting_items):
        self.inventory = starting_items

    def get_inventory(self):
        return self.inventory

    def loot_item(self, item):
        self.inventory.append(item)
        return self.inventory

    def drop_item(self, item):
        self.inventory.remove(item)
        return self.inventory
