from OpenWebsite import OpenWebsite
from CheckLinks import CheckLinks

def main():
    price_min = 0
    price_max = 600000
    min_area = 35
    max_area = 100

    site = OpenWebsite(price_min, price_max, min_area, max_area)
    site.set_filters_and_search()
    links = CheckLinks(site.get_driver())
    links.open_offers()
    print(links.get_data_about_flat())

if __name__ == '__main__':
    main()