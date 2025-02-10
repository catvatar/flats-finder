from search_query import SearchQuery
from otodom_forum import OtodomForum

import json

from logging import Logger

query_example = SearchQuery({
    'location' : 'Warsaw',
    'real_estate': 'apartment',
    'offer' : 'rent',
})

listings = OtodomForum(query_example).get_all_listings()
print(f'Listings length = {len(listings)}')
with open('listings.json', 'w') as f:
    json.dump(list(listings), f)