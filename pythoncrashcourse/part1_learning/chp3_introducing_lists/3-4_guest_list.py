guests = ["ali", "baba", "chia"]

for guest in guests: 
    print("I would like to invite you to dinner, " + guest.title())

absent = "baba"
print(f"\n{absent.title()} cannot make it.")
guests.remove("baba")

new = "doreen"
print(f"\n{new.title()} is the new person I am inviting.")
guests.append(new)
for guest in guests: 
    print("I would like to invite you to dinner, " + guest.title())

print("\nI now have a bigger table!")
new2 = "elephantDee"
new3 = "fatherJames"
guests.insert(0, new2)
guests.insert(2, new3)
print(guests)

print("\nI now only have space for 2 guests!")
# count the number of guests
num_guests = len(guests)
# for the people that is more than 2 guests
for i in range(num_guests - 2):
    # remove the last member from the list
    guest_removed = guests.pop()
    print(f"I'm sorry I can't invite you to dinner, {guest_removed}")
print(f"the guests remaining are {guests}")

del guests[:]
print(f"\nthe empty list is {guests}")

