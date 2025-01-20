class Otodom_url_generator:
    __url_static_part__ = 'https://www.otodom.pl/pl/wyniki'
    __url_params__ = None
    __url_dynamic_part__ = None

    def __init__(self):
        self.__url_dynamic_part__ = Offer_type()
        self.__url_params__ = Search_parameters()

    def parse_arguments(self,*args):
        arguments = {}
        if len(args) != 0:
            arguments = args[0]

        self.__url_dynamic_part__.set_place(arguments.get('place'),0)
        self.__url_dynamic_part__.set_offer_type(arguments.get('offer_type'))

    def get_url_with_search_params(self):
        generate_url = self.__url_static_part__
        generate_url += self.__url_dynamic_part__.generate_offer_url()
        generate_url += self.__url_params__.parse_search_parameters()
        return generate_url


class Search_parameters:
    __search_parameters__ = []

    def parse_search_parameters(self):
        if len(self.__search_parameters__) == 0:
            return ''

        searchParametersString = '?'
        for parameter in self.__search_parameters__:
            searchParametersString += f'${parameter}&'
        return searchParametersString


class Offer_type:
    __market_location__ = ''
    __realestate_market_type__ = ''
    __property_market_type__ = ''
    __offer_type__ = ''

    def __init__(self):
        self.__realestate_market_type__ = 'mieszkanie'
        self.__offer_type__ = 'sprzedaz'

    def generate_offer_url(self):
        generate_url = ''
        generate_url += self.__parse_offer_type__()
        generate_url += self.__parse_markets__()
        generate_url += self.__parse_location__()
        return generate_url

    def set_place(self, place, distanceRadius):
        if(distanceRadius != 0):
            self.__add_search_parameters__(f'distanceRadius=${distanceRadius}')
        if(place == 'ALL' or place == None):
            self.__market_location__ = 'cala-polska/'
        elif(place == 'Warsaw'):
            self.__market_location__ = 'mazowieckie/warszawa/warszawa/warszawa/'
        elif(place == 'Bialystok'):
            self.__market_location__ = 'podlaskie/bialystok/bialystok/bialystok/'
        
    def set_offer_type(self, offer_type):
        if(offer_type == None):
            return
        self.__offer_type__ = offer_type.lower()
    
    def __parse_offer_type__(self):
        return f'/{self.__offer_type__}'

    def __parse_markets__(self):
        marketType = ''
        if self.__property_market_type__ != '':
            marketType = f',{self.__property_market_type__}'
        return f'/{self.__realestate_market_type__}{marketType}'

    def __parse_location__(self):
        return f'/{self.__market_location__}'
