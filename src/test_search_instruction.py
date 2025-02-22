import unittest

from search_instruction import SearchInstruction
from search_query import SearchQuery

class TestBrowser(unittest.TestCase):
    def test_search_for_apartments_for_sell_in_warsaw(self):
        searching_instructions = SearchInstruction("Apartments for sell in Warsaw on Otodom")
        expected_result = SearchQuery({
            'forum': 'Otodom',
            'location': 'Warsaw',
            'offer': 'sell',
            'property_type': 'apartment',
        })
        for query in searching_instructions:
            self.assertEqual(query, expected_result)

    def test_search_in_two_cities(self):
        searching_instructions = SearchInstruction("Apartments for sell in Warsaw and Bialystok on Otodom")
        queries = searching_instructions.get_all_queries()
        self.assertTrue(SearchQuery({
            'forum': 'Otodom',
            'location': 'Warsaw',
            'offer': 'sell',
            'property_type': 'apartment',
        }) in queries)
        self.assertTrue(SearchQuery({
            'forum': 'Otodom',
            'location': 'Bialystok',
            'offer': 'sell',
            'property_type': 'apartment',
        }) in queries)

    def test_random_capitalization(self):
        searching_instructions = SearchInstruction("HOuses and apartmEnts FOR RENT IN WARSAW on Otodom")
        queries = searching_instructions.get_all_queries()
        self.assertTrue(SearchQuery({
            'forum': 'Otodom',
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'apartment',
        }) in queries)
        self.assertTrue(SearchQuery({
            'forum': 'Otodom',
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'house',
        }) in queries)

    def test_complex_search_instruction(self):
        searching_instructions = SearchInstruction("Houses and apartments for sell and rent in Bialystok and Warsaw on Otodom")
        queries = searching_instructions.get_all_queries()
        self.assertEqual(len(queries), 8)
        self.assertTrue(SearchQuery({
            'forum': 'Otodom',
            'location': 'Bialystok',
            'offer': 'sell',
            'property_type': 'house',
        }) in queries)
        self.assertTrue(SearchQuery({
            'forum': 'Otodom',
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'apartment',
        }) in queries)

    def todo_all_keyword_search(self):
        #TODO replace todo in todo_all_keyword_search with test
        searching_instructions = SearchInstruction("all for rent in Poland on Otodom")
        #TODO somehow test this instruction

    def todo_instruction_conjunctions(self):
        #TODO: replace todo in todo_instruction_conjunctions with test
        searching_instructions = SearchInstruction("houses for sell in bialystok and apartments for rent in warsaw on Otodom")
        queries = searching_instructions.get_all_queries()
        self.assertTrue(SearchQuery({
            'forum': 'Otodom',
            'location': 'Bialystok',
            'offer': 'sell',
            'property_type': 'house',
        }) in queries)
        self.assertTrue(SearchQuery({
            'forum': 'Otodom',
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'apartment',
        }) in queries)
        self.assertFalse(SearchQuery({
            'forum': 'Otodom',
            'location': 'Bialystok',
            'offer': 'rent',
            'property_type': 'house',
        }) in queries)
        self.assertFalse(SearchQuery({
            'forum': 'Otodom',
            'location': 'Bialystok',
            'offer': 'sell',
            'property_type': 'apartment',
        }) in queries)
        self.assertFalse(SearchQuery({
            'forum': 'Otodom',
            'location': 'Warsaw',
            'offer': 'sell',
            'property_type': 'apartment',
        }) in queries)
        self.assertFalse(SearchQuery({
            'forum': 'Otodom',
            'location': 'Warsaw',
            'offer': 'rent',
            'property_type': 'house',
        }) in queries)


