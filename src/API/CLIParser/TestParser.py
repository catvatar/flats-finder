import unittest
from RealEstateSearchCriteria import *

class TestParser(unittest.TestCase):
    def test_parsing_without_arguments(self):
        parser = RealEstateSearchCriteria()
        args = parser.get_parsed_arguments()
        self.assertEqual(args.price_min, 0)
        self.assertEqual(args.price_max, 600000)
        self.assertEqual(args.min_area, 0)
        self.assertEqual(args.max_area, 100)
        self.assertEqual(args.place, 'Warszawa')
        self.assertEqual(args.time_filter, 'any')
        self.assertEqual(args.market_type, 'any')




if __name__ == '__main__':
    unittest.main()
