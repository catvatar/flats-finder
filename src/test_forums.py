import unittest

from search_query import SearchQuery
from forums import Forum

class TestBrowser(unittest.TestCase):
    def test_forum_throws_on_wrong_forum(self):
        with self.assertRaises(TypeError):
            Forum(SearchQuery({
                'forum' : 'Unsupported',
                'location' : 'Bialystok',
                'property_type': 'apartment',
                'offer' : 'rent',
            }))
    def test_can_iterate_over_forum(self):
        forum = Forum(SearchQuery({
            'forum' : 'Otodom',
            'location' : 'Warsaw',
            'property_type': 'apartment',
            'offer' : 'rent',
        }))
        for offer in forum:
            self.assertIsNotNone(offer)