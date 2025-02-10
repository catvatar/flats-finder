import unittest
from unittest.mock import MagicMock
from otodom_forum import OtodomForum
from search_query import SearchQuery
from web_driver import WebDriver


class TestBrowser(unittest.TestCase):
    def test_raises_error_if_missing_arguments(self):
        with self.assertRaises(Exception) as context:
            otodom = OtodomForum({})

    def test_simple_search(self):
        query = SearchQuery({
            'location' : 'Warsaw',
            'real_estate': 'apartment',
            'offer' : 'rent',
        })
        otodomUrl = 'https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/mazowieckie/warszawa/warszawa/warszawa'
        self.assertEqual(OtodomForum(query)._get_url_for_search_query(),otodomUrl)

    def test_get_listings(self):
        outgoingLinks = [
            'https://www.otodom.pl/oferta/1234',
            'https://www.otodom.pl/oferta/5678',
            'https://www.otodom.pl/oferta/5678',
            'https://www.otodom.pl/oferta/91011'
        ]
        driver = MagicMock(spec=WebDriver)
        driver.get_outgoing_links = MagicMock(return_value=outgoingLinks)
        query = SearchQuery({
            'location' : 'Warsaw',
            'real_estate': 'apartment',
            'offer' : 'rent',
        })
        otodom = OtodomForum(query)
        otodom.use_custom_driver(driver)
        listings = otodom.get_all_listings()
        self.assertEqual(len(listings), 3)
        for outgoingLink in outgoingLinks:
            self.assertTrue(outgoingLink in listings)

    def test_go_to_the_next_previous_page(self):
        query = SearchQuery({
            'location' : 'Warsaw',
            'real_estate': 'apartment',
            'offer' : 'rent',
        })
        otodomUrl = 'https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/mazowieckie/warszawa/warszawa/warszawa'
        otodomForum = OtodomForum(query)
        otodomForum.go_to_the_next_page()
        self.assertEqual(otodomForum._current_page,otodomUrl + '?page=2')
        otodomForum.go_to_the_previous_page()
        self.assertEqual(otodomForum._current_page,otodomUrl + '?page=1')
        otodomForum.go_to_the_next_page()
        otodomForum.go_to_the_next_page()
        self.assertEqual(otodomForum._current_page,otodomUrl + '?page=3')
    def test_throws_on_invalid_location(self):
        query = SearchQuery({
            'location' : 'Shit in ass',
            'real_estate': 'apartment',
            'offer' : 'rent',
        })
        with self.assertRaises(Exception) as context:
            otodom = OtodomForum(query)


if __name__ == '__main__':
    unittest.main()