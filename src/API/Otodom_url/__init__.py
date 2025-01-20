from .url_structure.Location import Location
from .url_structure.Parameters import Parameters

class Otodom_url_generator:
    __static_url_string__ = 'https://www.otodom.pl/pl/wyniki'

    def __init__(self):
        self.__dynamic_url_object__ = Location()
        self.__url_params_object__ = Parameters()

    def generate_url_from_args(self, *args):
        self.__parse_arguments__(args)
        return self.generate_url()

    def __parse_arguments__(self,args):
        arguments = {}
        if len(args) != 0:
            arguments = args[0]

        self.__dynamic_url_object__.set_place(arguments.get('place'),0)
        self.__dynamic_url_object__.set_offer_type(arguments.get('offer_type'))

    def generate_url(self):
        generate_url = self.__static_url_string__
        generate_url += self.__dynamic_url_object__.generate_offer_url()
        generate_url += self.__url_params_object__.parse_search_parameters()
        return generate_url
