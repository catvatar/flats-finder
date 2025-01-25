
query_example = SearchQuery({
    'location' : 'Warsaw',
    'location_radius' : '5km',
    'real_estate': 'apartment',
    'offer' : 'rent',
})

listings = OtodomForum(query_example).get_listings()
print(listings.url)