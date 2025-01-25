import unittest
from search_query import SearchQuery

class TestBrowser(unittest.TestCase):
    def test_throws_when_missing_required_params(self):
        with self.assertRaises(ValueError):
            query = SearchQuery({})

    def test_correct_search_query_init(self):
        query = SearchQuery({
            'location' : 'Warsaw',
            'real_estate': 'apartment',
            'offer' : 'rent',
        })
        self.assertIsNotNone(query)

if __name__ == '__main__':
    unittest.main()