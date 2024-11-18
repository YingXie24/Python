sandwich_orders = ["tuna", "ham", "pastrami", "mushroom", "beetroot", "pastrami"]
made_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(f"The sandwich orders is now {sandwich_orders}.")

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()

    print(f"\nI made your {made_sandwich} sandwich.")

    made_sandwiches.append(made_sandwich)

    print(f"The sandwiches made at this point are {made_sandwiches}")


