import argparse

def get_parsed_arguments():
    return parser.parse_args()

parser = argparse.ArgumentParser()
parser.add_argument('--price_min', type=int, default=0, help='Set minimum price')
parser.add_argument('--price_max', type=int, default=600000, help='Set maximum price')
parser.add_argument('--min_area', type=int, default=0, help='Set minimal area of flat')
parser.add_argument('--max_area', type=int, default=100, help='Set maximal area of flat')
parser.add_argument('--place', type=str, default='Warszawa', help='Set location of flat')
parser.add_argument('--time_filter', type=str, choices=['any', 'last24h', 'last3d', 'last7d'], default='any', help='Set filtering for time of adding offer to Otodom')
parser.add_argument('--market_type', type=str, choices=['any', 'primary', 'secondary'], default='any', help='Set market type of flat')
