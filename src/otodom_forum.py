# TODO 1: Implement get_listings for all pages
# TODO 2: Implement filtering for acuall offers

from search_query import SearchQuery
from web_driver import WebDriver

class OtodomForum:
    _search_query = ''
    _driver = None
    _current_page = ''
    _pages_limit = None

    def __init__(self, search_query: SearchQuery):
        self._search_query = search_query
        self._driver = WebDriver()
        self._current_page = self._get_url_for_search_query()


    def get_all_listings(self):
        listings = set()
        prev_listings_length = 0
        while(True):
            listings.update(self.get_listings_from_current_page())
            self.go_to_the_next_page()
            if(prev_listings_length == len(listings)):
                break
            prev_listings_length = len(listings)
        return listings

    def go_to_the_next_page(self):
        page_number = self._get_page_number()
        if (page_number == 0):
            self._current_page += '?page=2'
        self._current_page = self._current_page.replace(f'page={page_number}', f'page={page_number+1}')


    def go_to_the_previous_page(self):
        page_number = self._get_page_number()
        if (page_number > 1):
            self._current_page = self._current_page.replace(f'page={page_number}', f'page={page_number-1}')
            return
        raise(Exception('Can not got to the previous_page. Already on page 0'))

    
    def get_listings_from_current_page(self):
        outgoing_links = set()
        outgoing_links.update(self._driver.get_outgoing_links(self._current_page))
        outgoing_links = filter(self._otodom_listing_filter, outgoing_links)
        return outgoing_links

    def use_custom_driver(self,driver):
        self._driver = driver

    def set_page_limit(self, limit):
        self._pages_limit = limit

    def _get_page_number(self):
        if(self._current_page.find('page=') == -1):
            return 0
        return int(self._current_page.split('page=')[1])

    def _otodom_listing_filter(self,listing):
        return listing.find('oferta') != -1


    def _get_url_for_search_query(self):
        url_static_part = 'https://www.otodom.pl/pl/wyniki'
        return url_static_part + self._parse_search_query()

    def _parse_search_query(self):
        if(self._search_query.offer == None):
            raise Exception('Missing offer argument')
        else:
            offer = self._parse_offer(self._search_query.offer)
        
        if(self._search_query.real_estate == None):
            raise Exception('Missing real_estate argument')
        else:
            real_estate = self._parse_real_estate(self._search_query.real_estate)
        
        if(self._search_query.location == None):
            raise Exception('Missing location argument')
        else:
            location = self._parse_location(self._search_query.location)
        
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
        raise('Unknown Location')

