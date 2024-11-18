import unittest
from city_functions import get_formatted_city

class TestCityName(unittest.TestCase):
    """Tests the function "get_formatted_city" """

    def test_two_inputs(self):
        received_full_name = get_formatted_city("santiago", "chile")
        expected_full_name = "Santiago, Chile - Population Unknown"
        self.assertEqual(received_full_name, expected_full_name)

    def test_three_inputs(self):
        received_full_name = get_formatted_city("santiago", "chile", 30000)
        expected_full_name = "Santiago, Chile - Population 30000"
        self.assertEqual(received_full_name, expected_full_name)

if __name__ == '__main__':
    unittest.main()
