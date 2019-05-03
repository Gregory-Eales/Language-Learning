import random


class Dice:
    def __init__(self, value=0):
        self.value = value

    def roll_dice(self):
        self.value = random.randrange(1, 7)
        return self.value


dice1 = Dice()
dice2 = Dice()
x = input("Press enter to roll:")
while x != "q":
    print(str(dice1.roll_dice()) + " and " + str(dice2.roll_dice()))
    x = input("Press enter to roll again, or type 'q' to quit:")
