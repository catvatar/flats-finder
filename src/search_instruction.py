from search_query import SearchQuery

class SearchInstruction:
    real_estate_types = []
    offer_types = []
    locations = []

    _index = 0
    _max_index = 0;

    def get_all_queries(self):
        queries = []
        for query in self:
            queries.append(query)
        return queries

    def __init__(self, searching_instruction):
        self.clear()
        self._figure_out_search_params_from_search_instruction(searching_instruction)
        self._calculate_number_of_queries()

    def _figure_out_search_params_from_search_instruction(self, instruction):
        instruction = instruction.lower()
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
        number_of_queries *= len(self.real_estate_types)
        number_of_queries *= len(self.offer_types)
        number_of_queries *= len(self.locations)
        self._max_index = number_of_queries

    def __iter__(self):
        return self

    def __next__(self):
        self._check_if_run_out_of_queries()
        real_estate, offer, location = self._getSearchParametersCombination(self._index)
        self._index = self._increment(self._index)
        return SearchQuery({
            'location': location,
            'property_type': real_estate,
            'offer': offer,
        })

    def _getSearchParametersCombination(self, index):
        real_estate, index = self._getElementFromList(self.real_estate_types, index)
        offer, index = self._getElementFromList(self.offer_types, index)
        location, index = self._getElementFromList(self.locations, index)
        return real_estate, offer, location

    def _getElementFromList(self, input_list, index):
        list_length = len(input_list)
        list_element = input_list[index % list_length]
        return list_element, index // list_length

    def _increment(self, index):
        index = index + 1
        return index

    def _check_if_run_out_of_queries(self):
        if self._index >= self._max_index:
            raise StopIteration

    def __str__(self):
        return f'{self.real_estate_types} {self.offer_types} {self.locations}'

    def clear(self):
        self.real_estate_types = []
        self.offer_types = []
        self.locations = []
        self._index = 0
        self._max_index = 0