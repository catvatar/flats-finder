class SearchQuery:
    property_type = ''
    offer = ''
    location = ''

    def __init__(self, query):
        self._throw_on_missing_arguments(query)
        self.property_type = query['property_type']
        self.offer = query['offer']
        self.location = query['location']

    def _throw_on_missing_arguments(self, query):
        mandatory_arguments = ['property_type', 'offer', 'location']
        self._check_arguments_in_query(mandatory_arguments, query)
        return
    
    def _check_arguments_in_query(self, arguments, query):
        for argument in arguments:
            if(argument not in query):
                raise ValueError(f'Missing argument: {argument}')
        return

    def __str__(self):
        return f'{self.location} {self.offer} {self.property_type}'

    def __eq__(self, other):
        return self.__str__() == other.__str__()