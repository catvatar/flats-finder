import unittest
from search_query import SearchQuery

class TestBrowser(unittest.TestCase):
    def test_throws_when_missing_required_params(self):
        with self.assertRaises(ValueError):
            query = SearchQuery({})

    def test_correct_search_query_init(self):
        query = SearchQuery({
            'forum' : 'Otodom',
            'location' : 'Warsaw',
            'property_type': 'apartment',
            'offer' : 'rent',
        })
        self.assertIsNotNone(query)

    def test_same_queries_are_equal(self):
        query_A = SearchQuery({
            'forum' : 'Otodom',
            'location' : 'Warsaw',
            'property_type': 'apartment',
            'offer' : 'rent',
        })
        query_B = SearchQuery({
            'forum' : 'Otodom',
            'location' : 'Warsaw',
            'property_type': 'apartment',
            'offer' : 'rent',
        })
        self.assertEqual(query_A,query_B)

    def test_different_queries_are_not_equal(self):
        query_A = SearchQuery({
            'forum' : 'Otodom',
            'location' : 'Warsaw',
            'property_type': 'apartment',
            'offer' : 'rent',
        })
        query_B = SearchQuery({
            'forum' : 'Otodom',
            'location' : 'Bialystok',
            'property_type': 'apartment',
            'offer' : 'rent',
        })
        self.assertNotEqual(query_A, query_B)

    def todo_throws_on_unsupported_arguments(self):
        #TODO replace todo in todo_throws_on_unsupported_arguments with test
        with self.assertRaises(ValueError):
            query = SearchQuery({
                'forum' : 'Unsupported',
                'location' : 'Bialystok',
                'property_type': 'apartment',
                'offer' : 'rent',
            })

if __name__ == '__main__':
    unittest.main()