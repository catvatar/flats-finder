from OpenWebsite import OpenWebsite
from CheckLinks import CheckLinks

def main():
    price_min = 0
    price_max = 600000
    min_area = 35
    max_area = 100

    site = OpenWebsite(price_min, price_max, min_area, max_area)
    driver = site.setup_webdriver()
    site.set_filters_and_search(driver)
    links = CheckLinks(driver)
    links.retreive_offer_and_title()
    links.open_offers()

if __name__ == '__main__':
    main()