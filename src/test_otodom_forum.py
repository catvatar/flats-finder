import unittest
from otodom import Otodom

class TestBrowser(unittest.TestCase):
    def test_search_query_exists(self):
        otodom = Otodom()
        self.assertIsNotNone(otodom)

if __name__ == '__main__':
    unittest.main()