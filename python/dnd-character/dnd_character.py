from random import randint


class Character:
    def __init__(self):
        self.strength = sum(four_dice_select_three())
        self.dexterity = sum(four_dice_select_three())
        self.constitution = sum(four_dice_select_three())
        self.intelligence = sum(four_dice_select_three())
        self.wisdom = sum(four_dice_select_three())
        self.charisma = sum(four_dice_select_three())
        self.abilities_list = [
            self.strength,
            self.dexterity,
            self.constitution,
            self.intelligence,
            self.wisdom,
            self.charisma,
        ]

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return self.abilities_list[roll_dice() - 1]


def modifier(ability):
    return (ability - 10) // 2


def roll_dice(sides=6):
    return randint(1, sides)


def four_dice_select_three(sides=6):
    least = sides + 1
    dice = []
    for _ in range(4):
        d = roll_dice(sides)
        if d < least:
            least = d
        dice.append(d)

    dice.remove(least)

    return dice
