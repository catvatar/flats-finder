# TODO 1: Implement get_listings for all pages
# TODO 2: Implement filtering for acuall offers

from search_query import SearchQuery
from selenium_web_driver import SeleniumWebDriver

class OtodomForum:
    _search_query = ''
    _driver = None

    def __init__(self, search_query: SearchQuery):
        self._search_query = search_query
        self._driver = SeleniumWebDriver()

    def get_listings(self):
        listings = []
        url = self._get_url_for_search_query()
        listings.append(self.get_listing_from_page(url))
        return listings


    def get_listing_from_page(self, url):
        outgoingLinks = self._driver.get_outgoing_links(url)
        return self._create_listings(outgoingLinks)

    def use_custom_driver(self,driver):
        self._driver = driver

    def _create_listings(self, urls):
        listings = []
        for url in urls:
            listings.append({'url': url})
        return listings

    def _get_url_for_search_query(self):
        url_static_part = 'https://www.otodom.pl/pl/wyniki'
        return url_static_part + self._parse_search_query(self._search_query)

    def _parse_search_query(self, search_query):
        offer = self._parse_offer(search_query.offer)
        real_estate = self._parse_real_estate(search_query.real_estate)
        location = self._parse_location(search_query.location)
        return f'/{offer}/{real_estate}/{location}'

    def _parse_offer(self, offer):
        if(offer == 'rent'):
            return 'wynajem'
        elif(offer == 'sell'):
            return 'sprzedaz'
        raise ValueError

    def _parse_real_estate(self, real_estate):
        if(real_estate == 'apartment'):
            return 'mieszkanie'
        if(real_estate == 'house'):
            return 'dom'
        raise ValueError

    def _parse_location(self, location):
        if(location == 'Poland'):
            return 'cala-polska'
        if(location == 'Warsaw'):
            return 'mazowieckie/warszawa/warszawa/warszawa'
        if(location == 'Bialystok'):
            return 'podlaskie/bialystok/bialystok/bialystok'