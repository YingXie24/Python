import re
user_input = str(input("What is your input?"))

def floating(string):

    is_floating = False
    if re.search(r"^[+-]?\d*\.\d+", user_input) is not None:
        is_floating =  True

    print(is_floating)

floating(user_input)