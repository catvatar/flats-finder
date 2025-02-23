from search_query import SearchQuery
from web_driver import WebDriver

class Forum:
    _listings_iterator = None
    def __init__(self, query: SearchQuery):
        match(query.forum):
            case 'Otodom':
                self._listings_iterator = OtodomForumIterator(query)
            case _:
                self._listings_iterator = ForumIteratorTemplate(query)
                raise TypeError(f'Unsupported forum: {query.forum}')

    def __iter__(self):
        return self._listings_iterator

class ForumIteratorTemplate:
    pages = None

    current_page = []
    index_on_current_page = 0

    def __init__(self, query: SearchQuery):
        self.pages = self._query_adapter(query)

    def _query_adapter(self, query):
        raise NotImplemented

    def get_all_listings(self):
        listings = []
        for listing in self:
            listings.append(listing)
        return listings

    def __next__(self):
        if self.index_on_current_page < len(self.current_page):
            return self._get_listing_from_current_page_and_increment()
        self.current_page = self.pages.__next__()
        self.index_on_current_page = 0
        return self._get_listing_from_current_page_and_increment()

    def _get_listing_from_current_page_and_increment(self):
        listing = self.current_page[self.index_on_current_page]
        self.index_on_current_page = self.index_on_current_page + 1
        return listing

    def __iter__(self):
        return self

class OtodomForumIterator(ForumIteratorTemplate):
    def _query_adapter(self, query):
        return OtodomPagesIterator(query)

class PagesIteratorTemplate:
    query = None
    page_index = 0

    def __init__(self, query):
        self.query = query

    def __next__(self):
        url = self._build_url()
        self.page_index = self.page_index + 1
        return self._get_listings_from_page(url)

    def __iter__(self):
        return self
    
    def _build_url(self):
        raise NotImplemented

    def _get_listings_from_page(self, url):
        raise NotImplemented


class OtodomPagesIterator(PagesIteratorTemplate):
    _driver = WebDriver

    def override_driver(driver):
        _driver = driver

    def _build_url(self):
        url_static_part = 'https://www.otodom.pl/pl/wyniki'
        return url_static_part + self._parse_search_query() + self._specify_page_index()

    def _get_listings_from_page(self, url):
        outgoing_links = set()
        outgoing_links.update(self._driver.get_outgoing_links(url, './/a[@data-cy="listing-item-link"]'))
        return outgoing_links

    def _specify_page_index(self):
        return f'?page={self.page_index}'

    def _parse_search_query(self):
        offer = self._parse_offer(self.query.offer)
        property_type = self._parse_property_type(self.query.property_type)
        location = self._parse_location(self.query.location)
        
        return f'/{offer}/{property_type}/{location}'

    def _parse_offer(self, offer):
        if(offer == 'rent'):
            return 'wynajem'
        elif(offer == 'sell'):
            return 'sprzedaz'
        raise ValueError

    def _parse_property_type(self, property_type):
        if(property_type == 'apartment'):
            return 'mieszkanie'
        if(property_type == 'house'):
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

class OtodomForum():
    _search_query = ''
    _current_page = ''
    _pages_limit = None

    def __init__(self, search_query: SearchQuery):
        self._search_query = search_query
        self._driver = WebDriver()
        self._current_page = self._get_url_for_search_query()
    