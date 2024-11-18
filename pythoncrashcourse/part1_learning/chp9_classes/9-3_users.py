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


xy = User("ying", "xie", "female", "malaysia")
xy.describe_user()
xy.greet_user()

xy.increment_login_attempts()
xy.increment_login_attempts()
xy.increment_login_attempts()
print(f"The user has logged in {xy.login_attempts} times.")

xy.reset_login_attempts()
print(f"The user has logged in {xy.login_attempts} times.")