import unittest
from src import HappyNumber as h


class HappyNumberTest(unittest.TestCase):

    def test_should_return_true_when_number_is_seven(self):
        self.assertTrue(h.HappyNumber().is_happy_number(7))

    def test_should_return_false_when_number_is_eight(self):
        self.assertFalse(h.HappyNumber().is_happy_number(8))

    def test_should_return_eight_from_power_and_sum_twenty_two(self):
        self.assertEqual(h.HappyNumber().power_and_sum_each_number(22), 8)

    def test_should_return_true_if_number_was_used(self):
        happy = h.HappyNumber()
        happy.used_numbers.append(1)
        self.assertTrue(happy.is_number_already_used(1))

    def test_should_return_false_if_number_was_not_used(self):
        happy = h.HappyNumber()
        happy.used_numbers.append(1)
        self.assertFalse(happy.is_number_already_used(2))

    
if __name__ == '__main__':
    unittest.main()
