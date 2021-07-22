"""Class for all characters including player"""

class Character:
    def __init__(self, starting_health=100, starting_gold=0, starting_items=[]):
        self.health = starting_health
        self.gold = starting_gold
        self.inventory = starting_items

class Health:
    def __init__(self, starting_value):
        self.health = starting_value

    def get_health():
        return self.health

    def heal(amount):
        self.health += amount
        return self.health

    def damage(amount):
        self.health -= amount
        return self.health

class Gold:
    def __init__(self, starting_value):
        self.gold = starting_value

    def get_gold():
        return self.gold

    def loot_gold(amount):
        self.gold += amount
        return self.gold

    def drop_gold(amount):
        self.gold -= amount
        return self.gold

class Inventory:
    def __init__(self, starting_items):
        self.inventory = starting_items

    def get_inventory():
        return self.inventory

    def loot_item(item):
        self.inventory.append(item)
        return self.inventory

    def drop_item(item):
        self.inventory.remove(item)
        return self.inventory
