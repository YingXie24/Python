# When copying lists, remember to use the slice notation to avoid pointer problems
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

# prove that we have 2 separate lists
my_foods.append('cannoli') 
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)