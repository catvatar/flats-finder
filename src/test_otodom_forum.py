import unittest
from unittest.mock import MagicMock
from otodom_forum import OtodomForum
from search_query import SearchQuery
from selenium_web_driver import SeleniumWebDriver


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
        self.assertEqual(OtodomForum(query)._get_url_for_search_query(),otodomUrl)

    def test_get_listings(self):
        outgoingLinks = [
            'https://www.otodom.pl/oferta/1234',
            'https://www.otodom.pl/oferta/5678',
            'https://www.otodom.pl/oferta/91011'
        ]
        driver = MagicMock(spec=SeleniumWebDriver)
        driver.get_outgoing_links = MagicMock(return_value=outgoingLinks)
        query = SearchQuery({
            'location' : 'Warsaw',
            'real_estate': 'apartment',
            'offer' : 'rent',
        })
        otodom = OtodomForum(query)
        otodom.use_custom_driver(driver)
        listings = otodom.get_listings()
        for i in range(len(outgoingLinks)):
            self.assertEqual(listings[i]['url'], outgoingLinks[i])


if __name__ == '__main__':
    unittest.main()