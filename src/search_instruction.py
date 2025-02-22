from search_query import SearchQuery

#TODO adding a new parameter to the search instruction should require a change
# in a single place only, right now it requires updating:
# - SearchInstruction variables
# - _clear
# - _figure_out_search_params_from_search_instruction
# - _calculate_number_of_queries
# - _getCurrentSearchQuery
# - __str__
# and all tests but that may be unavoidable


class SearchInstruction:
    """
    Example of a search instruction:
    - "Apartments for sell in Warsaw and Bialystok on Otodom"
    ---
    This class n an iterator for search queries based on the search instruction.
    It takes a search instruction and generates all possible search queries based on it.
    """
    forums = []
    real_estate_types = []
    offer_types = []
    locations = []

    _index = 0
    _max_index = 0;

    def get_all_queries(self):
        """
        Gathers all search queries and returns them as a list.
        """
        queries = []
        for query in self:
            queries.append(query)
        return queries

    def __init__(self, searching_instruction):
        self._clear()
        self._figure_out_search_params_from_search_instruction(searching_instruction)
        self._calculate_number_of_queries()

    def _clear(self):
        self.forums = []
        self.real_estate_types = []
        self.offer_types = []
        self.locations = []
        self._index = 0
        self._max_index = 0

    def _figure_out_search_params_from_search_instruction(self, instruction):
        instruction = instruction.lower()
        if 'otodom' in instruction:
            self.forums.append('Otodom')
        if 'apartments' in instruction:
            self.real_estate_types.append('apartment')
        if 'houses' in instruction:
            self.real_estate_types.append('house')
        if 'sell' in instruction:
            self.offer_types.append('sell')
        if 'rent' in instruction:
            self.offer_types.append('rent')
        if 'warsaw' in instruction:
            self.locations.append('Warsaw')
        if 'bialystok' in instruction:
            self.locations.append('Bialystok')

    def _calculate_number_of_queries(self):
        number_of_queries = 1
        number_of_queries *= len(self.forums)
        number_of_queries *= len(self.real_estate_types)
        number_of_queries *= len(self.offer_types)
        number_of_queries *= len(self.locations)
        self._max_index = number_of_queries

    def __next__(self):
        if self._run_out_of_queries():
            raise StopIteration
        search_query = self._get_current_search_query(self._index)
        self._index = self._index + 1
        return search_query

    def _run_out_of_queries(self):
        return self._index >= self._max_index

    def _get_current_search_query(self, index):
        forum, index = self._get_element_from_list(self.forums, index)
        real_estate, index = self._get_element_from_list(self.real_estate_types, index)
        offer, index = self._get_element_from_list(self.offer_types, index)
        location, index = self._get_element_from_list(self.locations, index)
        return SearchQuery({
            'forum': forum,
            'location': location,
            'property_type': real_estate,
            'offer': offer,
        })

    def _get_element_from_list(self, input_list, index):
        list_length = len(input_list)
        list_element = input_list[index % list_length]
        return list_element, index // list_length

    def __str__(self):
        return f'{self.real_estate_types} {self.offer_types} {self.locations}'

    def __iter__(self):
        return self
