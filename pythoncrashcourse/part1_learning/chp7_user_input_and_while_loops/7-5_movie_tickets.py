while True:
    age = input("\nWhat is your age?")

    age = int(age)

    if age < 3:
        price = 0
    
    elif age <= 12: 
        price = 10

    else:
        price = 15

    print(f"The ticket costs {price}.")
