from search_query import SearchQuery
from otodom_forum import OtodomForum

query_example = SearchQuery({
    'location' : 'Warsaw',
    'location_radius' : '5km',
    'real_estate': 'apartment',
    'offer' : 'rent',
})

listings = OtodomForum(query_example).get_listings_from_page()
[print(listing['url']) for listing in listings]