while True:
    
    number_1 = input("\nGive me one number: ")
    number_2 = input("Give me another number: ")

    try:
        sum_numbers = int(number_1) + int(number_2)
        print(f"The sum of the two numbers are {sum_numbers}.")

    except ValueError:
        print("Please give numbers only. ")