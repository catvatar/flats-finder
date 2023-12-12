from OpenWebsite import OpenWebsite
from CheckLinks import CheckLinks
from SaveToXlsx import SaveToXlsx

def main():
    price_min = 0
    price_max = 600000
    min_area = 35
    max_area = 100
    place = 'Warszawa'

    site = OpenWebsite(price_min, price_max, min_area, max_area, place)
    site.set_filters_and_search()
    links = CheckLinks(site.get_driver())
    links.open_offers()
    xlsx = SaveToXlsx(links.get_data_about_flat())
    xlsx.export_to_excel()
    site.get_driver().quit()

if __name__ == '__main__':
    main()