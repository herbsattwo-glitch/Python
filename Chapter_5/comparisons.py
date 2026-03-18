a = 1500   # Store the number 1500 in variable 'a'
b = 2000   # Store the number 2000 in variable 'b'

# Check if a is equal to b
print(a == b)   # False, because 1500 is NOT equal to 2000

# Check if a is NOT equal to b
print(a != b)   # True, because 1500 is different from 2000

# Check two conditions at once using AND
# a > 1000 (True, because 1500 > 1000)
# b < 2500 (True, because 2000 < 2500)
# AND means both must be True → result is True
print(a > 1000 and b < 2500)

# Check two conditions at once using OR
# a < 1000 (False, because 1500 is not less than 1000)
# b > 1000 (True, because 2000 > 1000)
# OR means at least one must be True → result is True
print(a < 1000 or b > 1000)

# Mix of AND and OR
# a < 1000 (False)
# b > 1000 (True)
# b < 2500 (True)
# Rule: AND is checked first, then OR
# (False AND True) → False
# False OR True → True
print(a < 1000 and b > 1000 or b < 2500)
