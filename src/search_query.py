class SearchQuery:
    real_estate = ''
    offer = ''
    location = ''

    def __init__(self, query):
        self._throw_on_missing_arguments(query)
        self.real_estate = query['real_estate']
        self.offer = query['offer']
        self.location = query['location']

    def _throw_on_missing_arguments(self, query):
        mandatory_arguments = ['real_estate', 'offer', 'location']
        _check_arguments_in_query(mandatory_arguments, query)
        return
    
    def _check_arguments_in_query(self, arguments, query):
        for argument in arguments:
            if(argument not in query):
                raise ValueError
        return
