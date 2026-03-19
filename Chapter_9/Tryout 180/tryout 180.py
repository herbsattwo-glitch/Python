import random  # we need random numbers

class Die:
    def __init__(self, sides=6):
        # sides = how many numbers the die can roll (default is 6)
        self.sides = sides

    def roll_die(self):
        # pick a random number between 1 and the number of sides
        return random.randint(1, self.sides)

# make a 6-sided die and roll it 10 times
six_die = Die()
print("Rolling a 6-sided die:")
for _ in range(10):
    print(six_die.roll_die())

# make a 10-sided die and roll it 10 times
ten_die = Die(10)
print("\nRolling a 10-sided die:")
for _ in range(10):
    print(ten_die.roll_die())

# make a 20-sided die and roll it 10 times
twenty_die = Die(20)
print("\nRolling a 20-sided die:")
for _ in range(10):
    print(twenty_die.roll_die())



import random

# list with 10 numbers and 5 letters
lottery_items = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']

# randomly pick 4 items
winning_combo = random.sample(lottery_items, 4)

print("Winning combo is:", winning_combo)
print("Any ticket matching these 4 wins a prize!")




import random

lottery_items = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
my_ticket = [1, 'A', 5, 'C']  # your chosen ticket

attempts = 0
while True:
    attempts += 1
    draw = random.sample(lottery_items, 4)
    if set(draw) == set(my_ticket):
        print("Your ticket won after", attempts, "draws!")
        break
