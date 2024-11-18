def order_sandwich(*sandwiches):
    """Accept a list of items a person wants on a sandwich"""

    print("\n")
    for sandwich in sandwiches:
        print(sandwich)

order_sandwich("tuna")
order_sandwich("pastrami", "beetroot", "cucumber")