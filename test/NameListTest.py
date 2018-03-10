import unittest
from DojoPython.src.NameList import NameList


class NameListTest(unittest.TestCase):

    def test_return_name_list(self):
        object_list = [
            {'name': 'Bart'},
            {'name': 'Lisa'},
            {'name': 'Maggie'}
        ]

        names = NameList.name_list(object_list)
        self.assertTrue(names, "")
        print(names)
