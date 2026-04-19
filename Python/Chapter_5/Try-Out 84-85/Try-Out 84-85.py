# ============================================================
# Exercises 5-3 through 5-7 bundled together in one file
# Idiot-proof comments included for clarity
# ============================================================

# -------------------------------
# 5-3. Alien Colors #1
# -------------------------------
# Task: Create a variable called alien_color and assign it 'green', 'yellow', or 'red'.
# Write an if statement to test whether the alien’s color is green.
# If it is, print "Player just earned 5 points".
# One version should pass (print message), another should fail (no output).

# Version that passes
alien_color = 'green'  # STEP 1: assign alien color to 'green'
if alien_color == 'green':  # STEP 2: check if alien_color equals 'green'
    print("Player just earned 5 points!")  # STEP 3: condition true, so print message

# Version that fails
alien_color = 'red'  # STEP 1: assign alien color to 'red'
if alien_color == 'green':  # STEP 2: check if alien_color equals 'green'
    print("Player just earned 5 points!")  # STEP 3: condition false, so nothing prints


# -------------------------------
# 5-4. Alien Colors #2
# -------------------------------
# Task: Use if-else chain.
# If alien is green → print 5 points.
# If alien is not green → print 10 points.

# Version that runs the if block
alien_color = 'green'  # STEP 1: alien is green
if alien_color == 'green':  # STEP 2: condition true
    print("Player just earned 5 points!")  # STEP 3: print 5 points
else:
    print("Player just earned 10 points!")  # skipped

# Version that runs the else block
alien_color = 'yellow'  # STEP 1: alien is yellow
if alien_color == 'green':  # STEP 2: condition false
    print("Player just earned 5 points!")  # skipped
else:
    print("Player just earned 10 points!")  # STEP 3: print 10 points


# -------------------------------
# 5-5. Alien Colors #3
# -------------------------------
# Task: Use if-elif-else chain.
# green → 5 points, yellow → 10 points, red → 15 points.

# Version for green alien
alien_color = 'green'  # STEP 1: alien is green
if alien_color == 'green':  # STEP 2: condition true
    print("Player earned 5 points!")  # STEP 3: print 5 points
elif alien_color == 'yellow':
    print("Player earned 10 points!")  # skipped
else:
    print("Player earned 15 points!")  # skipped

# Version for yellow alien
alien_color = 'yellow'  # STEP 1: alien is yellow
if alien_color == 'green':  # condition false
    print("Player earned 5 points!")  # skipped
elif alien_color == 'yellow':  # condition true
    print("Player earned 10 points!")  # STEP 3: print 10 points
else:
    print("Player earned 15 points!")  # skipped

# Version for red alien
alien_color = 'red'  # STEP 1: alien is red
if alien_color == 'green':  # condition false
    print("Player earned 5 points!")  # skipped
elif alien_color == 'yellow':  # condition false
    print("Player earned 10 points!")  # skipped
else:
    print("Player earned 15 points!")  # STEP 3: print 15 points


# -------------------------------
# 5-6. Stages of Life
# -------------------------------
# Task: Use if-elif-else chain to determine life stage based on age.
# <2 baby, 2-3 toddler, 4-12 kid, 13-19 teenager, 20-64 adult, 65+ elder.

age = 25  # STEP 1: set age value
if age < 2:  # STEP 2: check if less than 2
    print("Person is a baby.")
elif age < 4:  # STEP 3: check if between 2 and 3
    print("Person is a toddler.")
elif age < 13:  # STEP 4: check if between 4 and 12
    print("Person is a kid.")
elif age < 20:  # STEP 5: check if between 13 and 19
    print("Person is a teenager.")
elif age < 65:  # STEP 6: check if between 20 and 64
    print("Person is an adult.")
else:  # STEP 7: if none of the above, must be 65+
    print("Person is an elder.")


# -------------------------------
# 5-7. Favorite Fruit
# -------------------------------
# Task: Make a list of favorite fruits.
# Write independent if statements to check for certain fruits.

favorite_fruits = ['banana', 'mango', 'apple']  # STEP 1: create list of favorite fruits

# STEP 2: check for banana
if 'banana' in favorite_fruits:
    print("You really like bananas!")

# STEP 3: check for mango
if 'mango' in favorite_fruits:
    print("You really like mangoes!")

# STEP 4: check for apple
if 'apple' in favorite_fruits:
    print("You really like apples!")

# STEP 5: check for orange
if 'orange' in favorite_fruits:
    print("You really like oranges!")  # won't print because orange not in list

# STEP 6: check for grapes
if 'grapes' in favorite_fruits:
    print("You really like grapes!")  # won't print because grapes not in list
