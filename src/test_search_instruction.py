import unittest

from search_instruction import SearchInstruction
from search_query import SearchQuery

class TestBrowser(unittest.TestCase):
    def test_search_for_apartments_for_sell_in_warsaw(self):
        searching_instructions = SearchInstruction("Apartments for sell in Warsaw")
        expected_result = SearchQuery({
            'location': 'Warsaw',
            'offer': 'sell',
            'property_type': 'apartment',
        })
        for query in searching_instructions:
            self.assertEqual(query, expected_result)

    def test_search_in_two_cities(self):
        searching_instructions = SearchInstruction("Apartments for sell in Warsaw and Bialystok")
        queries = searching_instructions.get_all_queries()
        self.assertTrue(SearchQuery({
            'location': 'Warsaw',
            'offer': 'sell',
            'property_type': 'apartment',
        }) in queries)
        self.assertTrue(SearchQuery({
            'location': 'Bialystok',
            'offer': 'sell',
            'property_type': 'apartment',
        }) in queries)

    def test_random_capitalization(self):
        searching_instructions = SearchInstruction("HOuses and apartmEnts FOR RENT IN WARSAW")
        queries = searching_instructions.get_all_queries()
        self.assertTrue(SearchQuery({
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'apartment',
        }) in queries)
        self.assertTrue(SearchQuery({
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'house',
        }) in queries)

    def todo_instruction_conjunctions(self):
        #TODO: make this test pass
        searching_instructions = SearchInstruction("houses for sell in bialystok and apartments for rent in warsaw")
        queries = searching_instructions.get_all_queries()
        self.assertTrue(SearchQuery({
            'location': 'Bialystok',
            'offer': 'sell',
            'property_type': 'house',
        }) in queries)
        self.assertTrue(SearchQuery({
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'apartment',
        }) in queries)
        self.assertFalse(SearchQuery({
            'location': 'Bialystok',
            'offer': 'rent',
            'property_type': 'house',
        }) in queries)
        self.assertFalse(SearchQuery({
            'location': 'Bialystok',
            'offer': 'sell',
            'property_type': 'apartment',
        }) in queries)
        self.assertFalse(SearchQuery({
            'location': 'Warsaw',
            'offer': 'sell',
            'property_type': 'apartment',
        }) in queries)
        self.assertFalse(SearchQuery({
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'house',
        }) in queries)


