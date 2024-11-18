responses = {}
flag = True

while flag: 
    name = input("\nWhat is your name? ")
    country = input("\nWhere is your dream vacation? ")
    responses[name] = country

    pass_on = input("\nDo you want to pass on to the next person? (yes/no) ")
    if pass_on == 'no':
        flag = False

print("\n -- Polling is complete. -- ")
for name, country in responses.items():
    print(f"{name.title()} wants to go to {country.title()}.")