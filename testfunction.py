import unittest
from backend import get_data


class TestBackend(unittest.TestCase):
    # Test if the function returns a "list"
    def test_if_list(self):
        result = get_data(place="Paris", days=3)
        self.assertIsInstance(result, list)

    # Test if the function returns 24 items in the list
    def test_number_items(self):
        result = get_data(place="Paris", days=3)
        self.assertEqual(len(result), 24)

    # Test if the function returns a list that contains "weather" and "temp" that we need for the app
    def test_content(self):
        result = get_data(place="Paris", days=3)
        for item in result:
            main_dict = item['main']
            self.assertIn('temp', main_dict)
            self.assertIn('weather', item)


if __name__ == '__main__':
    unittest.main()
