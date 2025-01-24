import unittest
import search_query

class TestBrowser(unittest.TestCase):
    def test_search_query_exists(self):
        query = search_query.SearchQuery()
        self.assertIsNotNone(query)

if __name__ == '__main__':
    unittest.main()