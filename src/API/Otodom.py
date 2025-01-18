class Otodom:
    __otodom_sprzedaz__ = 'https://www.otodom.pl/pl/wyniki/sprzedaz'
    __search_parameters__ = []
    __market_location__ = ''
    __realestate_market_type__ = ''
    __property_market_type__ = ''

    def __init__(self):
        self.__realestate_market_type__ = 'mieszkanie'

    def parse_arguments(self,*args):
        arguments = {}
        if len(args) != 0:
            arguments = args[0]

        self.__set_place__(arguments.get('place'),0)

        # __set_price_per_real_estate__(args.price_min,args.price_max)
        # __set_area__(args.min_area,args.max_area)
        # __set_place__(args.place,0)
        # __set_age__(args.time_filter)
        # __set_market_type__(args.marketType)

    def get_url_with_search_params(self):
        generate_url = self.__otodom_sprzedaz__
        generate_url += self.__parse_markets__()
        generate_url += self.__parse_location__()
        generate_url += self.__parse_search_parameters__()
        return generate_url

    def __parse_markets__(self):
        marketType = ''
        if self.__property_market_type__ != '':
            marketType = f',{self.__property_market_type__}'
        return f'/{self.__realestate_market_type__}{marketType}'

    def __parse_location__(self):
        return f'/{self.__market_location__}'

    def __parse_search_parameters__(self):
        if len(self.__search_parameters__) == 0:
            return ''

        searchParametersString = '?'
        for parameter in self.__search_parameters__:
            searchParametersString += f'${parameter}&'
        return searchParametersString

    def __set_realestate_market_type__(realestate_market):
        realestate_market_type = realestate_market
        
    def __set_market_type__(self, marketTypeArgument):
        if marketTypeArgument == 'primary':
            marketType = 'rynek-pierwotny'
        elif marketTypeArgument == 'secondary':
            marketType = 'rynek-wtorny'

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