import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from src.OpenWebsite import OpenWebsite
from src.CheckLinks import CheckLinks

app = FastAPI()

@app.get("/")
def retreive_data(price_min, price_max, min_area, max_area, place, time_filter, market_type):
    site = OpenWebsite(price_min, price_max, min_area, max_area, place, time_filter, market_type)
    site.set_filters_and_search()
    links = CheckLinks(site.get_driver())
    links.open_offers()
    site.get_driver().quit()
    return links.get_data_about_flat()
