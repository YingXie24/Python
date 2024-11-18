motorcycles = ['honda', 'yamaha', 'suzuki', 'lotus', 'suzuki', 'ferrari', 'suzuki', 'perodua']
print(motorcycles)

# changing elements in a list in place
motorcycles[0] = 'proton'
print(motorcycles)

# appending elements to the end of a list
motorcycles.append("mercedes")
print(motorcycles)

# adding element to a specific position in the list
motorcycles.insert(1, "Volkswagen")
print(motorcycles)

# removing the last item in the list
last_item = motorcycles.pop()
print("this is the result after pop", motorcycles)
print(last_item)

# removing an item when you know the position of the item 
first_item =  motorcycles.pop(0)
print(motorcycles)
print(first_item)

# removing an item by value. only removes the first occurance
motorcycles.remove("suzuki")
print(motorcycles)

# remove all occurences using loop
count = 0
while motorcycles.count("suzuki"):   
    motorcycles.remove("suzuki")
    count += 1
    print(f"removed {count}")
    print(motorcycles)

num_occurences = motorcycles.count("suzuki")
for i in range(num_occurences):
    motorcycles.remove("suzuki")
    print(motorcycles)
    

