class Location:
    def __init__(self):
        self.__realestate_market_type__ = 'mieszkanie'
        self.__offer_type__ = 'sprzedaz'
        self.__market_location__ = 'cala-polska'

    def generate_offer_url(self):
        generate_url = ''
        generate_url += self.__parse_offer_type__()
        generate_url += self.__parse_markets__()
        generate_url += self.__parse_location__()
        return generate_url

    def __parse_offer_type__(self):
        return f'/{self.__offer_type__}'

    def __parse_markets__(self):
        return f'/{self.__realestate_market_type__}'

    def __parse_location__(self):
        return f'/{self.__market_location__}/'
        
    def set_place(self, place, distanceRadius):
        if(distanceRadius != 0):
            self.__add_search_parameters__(f'distanceRadius=${distanceRadius}')
        if(place == 'ALL' or place == None):
            self.__market_location__ = 'cala-polska'
        elif(place == 'Warsaw'):
            self.__market_location__ = 'mazowieckie/warszawa/warszawa/warszawa'
        elif(place == 'Bialystok'):
            self.__market_location__ = 'podlaskie/bialystok/bialystok/bialystok'
        
    def set_offer_type(self, offer_type):
        if(offer_type == None):
            return
        self.__offer_type__ = offer_type.lower()
    



