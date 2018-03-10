import unittest
from src.Diamond import Diamond


class DiamondTest(unittest.TestCase):

    def test_should_return_a_diamond_from_A_to_C_with_five_lines(self):
        lines = Diamond().diamond_generator("C")
        self.assertEqual(len(lines), 5)
        self.assertEqual("   A", lines[0])
        self.assertEqual("  B B", lines[1])
        self.assertEqual(" C   C", lines[2])
        self.assertEqual("  B B", lines[3])
        self.assertEqual("   A", lines[4])

    def test_should_return_three_spaces(self):
        self.assertEqual("   ", Diamond.repeat_space(3))


if __name__ == '__main__':
    unittest.main()
