# 4-3. Counting to Twenty
# Use a for loop to print numbers from 1 to 20
for number in range(1, 21):  # range(1, 21) means start at 1, stop before 21
    print(number)


# 4-4. One Million
# Make a list of numbers from 1 to 1,000,000
# WARNING: Printing all will flood your screen!
numbers = list(range(1, 1_000_001))  # underscore makes big numbers easier to read
# Uncomment the next line if you really want to print them (not recommended!)
# for number in numbers:
#     print(number)


# 4-5. Summing a Million
# Check that the list starts at 1 and ends at 1,000,000
print(min(numbers))  # should print 1
print(max(numbers))  # should print 1000000
print(sum(numbers))  # adds all numbers very quickly


# 4-6. Odd Numbers
# Use step=2 in range() to get odd numbers
for odd in range(1, 21, 2):  # start at 1, go up to 20, jump by 2
    print(odd)


# 4-7. Threes
# Multiples of 3 from 3 to 30
for three in range(3, 31, 3):  # start at 3, stop before 31, step by 3
    print(three)


# 4-8. Cubes
# Cube = number ** 3
for number in range(1, 11):  # numbers 1 through 10
    cube = number ** 3       # raise to the power of 3
    print(cube)


# 4-9. Cube Comprehension
# Use list comprehension to generate cubes
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)  # prints the whole list at once
