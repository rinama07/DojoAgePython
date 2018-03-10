import unittest
from Puzzles.src.main.FindShorterWord import FindShorterWord


class FindShorterWordTest(unittest.TestCase):

    def test_return_word_apple_in_list(self):
        words = [
            "apple",
            "apricot",
            "avocado",
            "banana",
            "bilberry",
            "blackberry",
            "blackcurrant",
            "blueberry",
            "boysenberry",
            "crab apples",
            "currant"
        ]

        word = FindShorterWord.find_shorter_word(words)
        self.assertTrue(word, "apple")

    def test_return_word_bilberry_in_list(self):
        words = [
            "blackberry",
            "blackcurrant",
            "bilberry",
            "boysenberry",
            "crab apples"
        ]

        word = FindShorterWord.find_shorter_word(words)
        self.assertTrue(word, "bilberry")

    def test_return_word_pea_in_list(self):
        words = [
            "eggplant",
            "olive",
            "pea"
        ]

        word = FindShorterWord.find_shorter_word(words)
        self.assertTrue(word, "pea")

    def test_return_empty_word(self):
        words = [""]

        word = FindShorterWord.find_shorter_word(words)
        self.assertTrue(word, '')
