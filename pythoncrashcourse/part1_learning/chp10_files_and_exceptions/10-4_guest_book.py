while True:

    guest = input("What is your name? ")

    guest = guest.capitalize()

    print(f"Hello {guest}! Welcome to my mansion!")

    with open("learning/chp10_files_and_exceptions/guest_book.txt", 'a') as file_object: 
        file_object.write(f"{guest}\n")