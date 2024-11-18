
# Using range() to make a list of numbers
numbers = list(range(11))
print(numbers)

# Using range()
even_num = list(range(60,79,2))
print(even_num)

squares = []
for num in range(1,10):
    squares.append(num**2)
print(squares)

# statistics
digits = [1,2,3,4,5,6,7]
print(min(digits))
print(max(digits))
print(sum(digits))

# one million
# for num in range (1,1000001):
#     print(num)

# summing a million
million_list = list(range(1,1000001))
print(min(million_list))
print(max(million_list))
print(sum(million_list))

# make a list of odd numbers for 1 to 2
for num in range(1,21,2):
    print(num)

# make a list of the multiples of 3 from 3 to 30
multiples_three = [num*3 for num in range(3,31)]
print(multiples_three)

# cube comprehension
cubes = [num**3 for num in range(1,11)]
print(cubes)
print(f"the last three numbers in the list are {cubes[-3:]}")