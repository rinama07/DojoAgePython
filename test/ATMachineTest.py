import unittest
from src import ATMachine as aT


class ATMachineTest(unittest.TestCase):

    hundred = 0
    fifty = 1
    twenty = 2
    ten = 3

    def test_withdraw_30_one_of_20_and_one_of_10(self):
        bills = aT.withdraw(30)
        self.assertEqual(bills[self.twenty], 1)
        self.assertEqual(bills[self.ten], 1)

    def test_withdraw_80_one_of_30_one_of_10(self):
        bills = aT.withdraw(80)
        self.assertEqual(bills[self.fifty], 1)
        self.assertEqual(bills[self.twenty], 1)
        self.assertEqual(bills[self.ten], 1)

    def test_withdraw_190_one_of_100_one_of_50_two_of_20(self):
        bills = aT.withdraw(190)
        self.assertEqual(bills[self.hundred], 1)
        self.assertEqual(bills[self.fifty], 1)
        self.assertEqual(bills[self.twenty], 2)


if __name__ == '__main__':
    unittest.main()
