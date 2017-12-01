# 测试工程
import unittest
from learnGrammar.str_learn import get_formatted_name


class nameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('hu', 'di')
        self.assertEqual(formatted_name, "Hu Di")
        formatted_name = get_formatted_name('hu', 'di', 'f')
        self.assertEqual(formatted_name, "Hu F Di")

    def test_list(self):
        testList = {1, 2, 3, 4, 5, 6}
        self.assertIn(4, testList)
        self.assertNotIn(7, testList)
        self.assertCountEqual({1,2, 3, 4, 5, 6}, testList)
