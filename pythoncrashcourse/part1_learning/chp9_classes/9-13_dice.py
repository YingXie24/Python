from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        random_number = randint(1, self.sides)
        return random_number
    
    def roll_ten_times(self):
        for i in range(10):
            roll = self.roll_die()
            print(roll)

# Make a 6-sided die
six_sided_die = Die()
print("\nRoll a 6 sided die:")
six_sided_die.roll_ten_times()

# Make a 10-sided die
ten_sided_die = Die(10)
print("\nRoll a 10 sided die:")
ten_sided_die.roll_ten_times()