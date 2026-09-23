import random
class Character:
    def __init__(self):
        self.strength = self.ability() 
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        dice_rolls.remove(min(dice_rolls))  # Finds and drops the minimum instantly
        return sum(dice_rolls)


def modifier(value):
    return (value - 10) // 2