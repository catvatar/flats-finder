import unittest
from otodom_forum import OtodomForum
from search_query import SearchQuery

class TestBrowser(unittest.TestCase):
    def test_search_query_exists(self):
        otodom = OtodomForum({})
        self.assertIsNotNone(otodom)
    
    def test_simple_search(self):
        query = SearchQuery({
            'location' : 'Warsaw',
            'real_estate': 'apartment',
            'offer' : 'rent',
        })
        otodomUrl = 'https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/mazowieckie/warszawa/warszawa/warszawa'
        self.assertEqual(OtodomForum(query),otodomUrl)
if __name__ == '__main__':
    unittest.main()