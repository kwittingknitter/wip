import unittest

from utils import get_proper_name


class TestGetProperName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proper_name_length = 2
        cls.proper_name_type = str
        cls.proper_name = get_proper_name()

    def test_get_proper_name_length(self):
        self.assertEqual(
            len(self.proper_name), self.proper_name_length)
        
    def test_get_proper_name_type(self):
        self.assertIsInstance(
            self.proper_name, self.proper_name_type)

    def test_combines_two_distinct_parts(self):
        self.assertNotEqual(
            self.proper_name[0], self.proper_name[1])


if __name__ == "__main__":
    unittest.main()
