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

class IceCreamStand:
    """Represents aspects of a restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes of the parent class."""
        """Then initialise attributes specific to ice cream stands."""
        super().__init__()
        self.flavors = ['cotton candy', 'tangerine', 'pistachio']
    
    def display_flavors(self):
        print(f"The flavors of icecream available are: {self.flavors}.")


scoop = IceCreamStand("scoop", "dessert")
scoop.display_flavors()