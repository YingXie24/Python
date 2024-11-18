class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, customer_served):
        """Set the number served to the given value."""
        self.number_served =  customer_served

    def increment_number_served(self, customers_arrived):
        """Add the give amount to the number served."""
        self.number_served += customers_arrived



lg = Restaurant("La Gingette", "French cuisine")
lg.describe_restaurant()
lg.open_restaurant()

rs= Restaurant("Rasa Sayang", "Malaysian cuisine")
rs.describe_restaurant()

# Change value of attribute directly
print(lg.number_served)
lg.number_served = 78
print(lg.number_served)

# Change value of attribute using method
lg.set_number_served(999)
print(lg.number_served)

# Incrementing value of attribute using method
lg.increment_number_served(857)
print(lg.number_served)