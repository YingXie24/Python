from random import randint, sample
from string import ascii_lowercase

# Make a list containing a series of 10 numbers from 0 to 9
lottery_list = []
for num in range(10):
    lottery_list.append(num)

# Add 5 random letters to the list
lottery_list.extend(sample(ascii_lowercase,5))

print(f"This is the list: {lottery_list}")

# Randomly select 4 characters from the list for the winning ticket
winning_ticket = sample(lottery_list, 4)
     
print("\nAny ticket matching these 4 characters wins.")    
print(winning_ticket) 

# Analyse how hard it might be to win the lottery
win_boolean = False
count = 0

while win_boolean == False:
    # Pull numbers for my ticket
    my_ticket = sample(lottery_list, 4)

    # Keep tabs for how many times the loop had to run to get a winning ticket
    count += 1
    print(f"\nTicket number {count}: {my_ticket}.")

    if my_ticket != winning_ticket:
        print("Try again.")

    else:
        print("Congratulations!")
        break

print(f"\nIt took you {count} tickets to win.")