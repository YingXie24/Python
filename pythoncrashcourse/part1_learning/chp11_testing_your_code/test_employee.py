import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    "Test for the class Employee."

    def setUp(self):
        """Create an instance for the Employee class."""
        """This instance will be userd in all test methods."""
        self.my_employee = Employee("Al-Habib", "Rohan", 10000)

    def test_give_default_raise(self):
        """Test that the default raise of 5000 works properly."""
        self.my_employee.give_raise()
        new_salary = self.my_employee.annual_salary
        self.assertEqual(new_salary, 15000)

    def test_give_custom_raise(self):
        """Test that the giving an arbritary raise works properly."""
        self.my_employee.give_raise(2888)
        new_salary = self.my_employee.annual_salary
        self.assertEqual(new_salary, 12888)

if __name__ == "__main__":
    unittest.main()