# TODO 1: Implement get_listings for all pages

from search_query import SearchQuery
class OtodomForum:
    _search_query = ''

    def __init__(self, search_query: SearchQuery):
        self._search_query = search_query

    def get_listings(self):
        return self.get_listings_from_page()

    def get_listings_from_page(self):
        from selenium_web_driver import SeleniumWebDriver
        driver = SeleniumWebDriver()
        return self.get_listings_using_custom_driver(driver)

    def get_listings_using_custom_driver(self, driver):
        url = self._get_url_for_search_query()
        outgoingLinks = driver.get_outgoing_links(url)
        listings = []
        for link in outgoingLinks:
            listings.append({
                'url': link
            })
        return listings

    def _get_url_for_search_query(self):
        url_static_part = 'https://www.otodom.pl/pl/wyniki'
        return url_static_part + self._parse_search_query(self._search_query)

    def _parse_search_query(self, search_query):
        offer = self._parse_offer(search_query.offer)
        real_estate = self._parse_real_estate(search_query.real_estate)
        location = self._parse_location(search_query.location)
        return f'/{offer}/{real_estate}/{location}&limit=72'

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