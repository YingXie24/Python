from user import User

class Privilege:
    def __init__(self):
        self.privileges = ["can add post", "can delete post"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User): 
    """Represent aspects of an user, specific to admins."""

    def __init__(self, first_name, last_name, gender, nationality):
        """Initialise attributes of the parent class."""
        """Then initialise attributes specific to the child class."""
        super().__init__(first_name, last_name, gender, nationality)
        self.privileges = Privilege()