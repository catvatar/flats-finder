# URLS for Otodom.pl
# https://www.otodom.pl/pl/wyniki/sprzedaz/kawalerka/mazowieckie/warszawa/warszawa/warszawa/?ownerTypeSingleSelect=ALL&distanceRadius=5&priceMin=2&priceMax=68&areaMin=1&areaMax=36&viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/haleimagazyny/cala-polska?ownerTypeSingleSelect=ALL&viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/haleimagazyny,rynek-pierwotny/cala-polska?limit=36&ownerTypeSingleSelect=AGENCY&pricePerMeterMin=5&pricePerMeterMax=6&daysSinceCreated=1&heightMin=3&heightMax=4&advertId=12&description=123&heating=%5BYES%5D&extras=%5BIS_PRIVATE_OWNER%5D&useTypes=%5BSTOCK%5D&by=DEFAULT&direction=DESC&viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/podlaskie/bialystok/bialystok/bialystok/bacieczki?viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa/bielany?viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa/bielany?limit=36&ownerTypeSingleSelect=ALL&by=DEFAULT&direction=DESC&viewType=listing
# URL Structure:
## Source page
# https://www.otodom.pl
## List of parameters
# /pl/wyniki/sprzedaz
# /[kawalerka,haleimagazyny],[rynek-pierwotny]
# /[mazowieckie/warszawa/warszawa/warszawa/bielany, podlaskie/bialystok/bialystok/bialystok/bacieczki, cala-polska]
# ?ownerTypeSingleSelect=[ALL,AGENCY]
# &distanceRadius=5
# &priceMin=2
# &priceMax=68
# &areaMin=1
# &areaMax=36
# &viewType=listing
# &limit=36
# &pricePerMeterMin=5
# &pricePerMeterMax=6
# &daysSinceCreated=1
# &heightMin=3
# &heightMax=4
# &advertId=12
# &description=123
# &heating=[YES]
# &extras=[IS_PRIVATE_OWNER]
# &useTypes=[STOCK]
# &by=DEFAULT
# &direction=DESC
# &viewType=listing

import unittest
from Otodom import Otodom

class TestBrowser(unittest.TestCase):
    otodom = None
    
    def setUp(self):
        self.otodom = Otodom()

    def tearDown(self):
        self.otodom = None

    def test_empty_search(self):
        self.otodom.parse_arguments()
        search_url = self.otodom.get_url_with_search_params()
        assertEqual(search_url, empty_search)

    empty_search = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska'

if __name__ == '__main__':
    unittest.main()
