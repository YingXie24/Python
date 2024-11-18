class User:
    def __init__(self, first_name, last_name, gender, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.nationality = nationality
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user is called {self.first_name.title()} {self.last_name.title()}."
              f"\n The user is a {self.gender}."
              f"\n The user is from {self.nationality.title()}.")
    
    def greet_user(self):
        print(f"Welcome, {self.first_name.title()}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User): 
    """Represent aspects of an user, specific to admins."""

    def __init__(self, first_name, last_name, gender, nationality):
        """Initialise attributes of the parent class."""
        """Then initialise attributes specific to the child class."""
        super().__init__(first_name, last_name, gender, nationality)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


ali = Admin("Ali", "bakar", "male", "pakistan")
ali.show_privileges()
first_name = ali.first_name
print(first_name)