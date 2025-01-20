class Parameters:
    __search_parameters__ = []

    def parse_search_parameters(self):
        if len(self.__search_parameters__) == 0:
            return ''

        searchParametersString = '?'
        for parameter in self.__search_parameters__:
            searchParametersString += f'${parameter}&'
        return searchParametersString

    # Untested and broken functionality below
    def __set_price_per_real_estate__(min, max):
        addSearchParameters(formatMinMaxParameters(min,max,'price'))

    def __set_price_pre_meter__(min,max):
        addSearchParameters(formatMinMaxParameters(min,max,'pricePerMeter'))

    def __set_area__(min,max):
        addSearchParameters(formatMinMaxParameters(min,max,'area'))

    def __set_place__(self, place, distanceRadius):
        if(distanceRadius != 0):
            self.__add_search_parameters__(f'distanceRadius=${distanceRadius}')
        if(place == 'ALL' or place == None):
            self.__market_location__ = 'cala-polska/'
        elif(place == 'Warsaw'):
            self.__market_location__ = 'mazowieckie/warszawa/warszawa/warszawa/'
        elif(place == 'Bialystok'):
            self.__market_location__ = 'podlaskie/bialystok/bialystok/bialystok/'
        
    def __set_age__(self,age):
        if age == 'any':
            None
        elif age == 'last24h':
            addSearchParameters(f'daysSinceCreated=1')
        elif age == 'last3d':
            addSearchParameters(f'daysSinceCreated=3')
        elif age == 'last7d':
            addSearchParameters(f'daysSinceCreated=7')

    def __format_min_max_parameters__(min, max, name):
        return f'${name}Min=${min}',f'${name}Max=${max}'

    def __add_search_parameters__(self, parameters):
        self.__search_parameters__.append(parameters)