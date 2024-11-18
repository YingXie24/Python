import json

def get_stored_username():
    """Get store username if available."""
    filename = "learning/chp10_files_and_exceptions/username.json"
    try: 
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = "learning/chp10_files_and_exceptions/username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def verify_username(username):
    """Ask whether current user is the person who last used the programme."""
    print(f"The user name '{username}' is stored in our database.")
    verify = input("Is that the correct username? Press 'Y' if yes, "
                    "Press 'N' if no: ")
    if verify == 'Y':
        print(f"Welcome back, {username}!")
    elif verify == 'N':
        username = get_new_username()
        print(f"Welcome new user {username}!")
    else:
        print("Please enter either 'Y' or 'N' only.")
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username: 
        username = verify_username(username)  
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()