from OpenWebsite import OpenWebsite
from CheckLinks import CheckLinks
from SaveToXlsx import SaveToXlsx
from Parser import Parser

def main():
    parser = Parser()
    args = parser.parse_args()

    site = OpenWebsite(args.price_min, args.price_max, args.min_area, args.max_area, args.place, args.time_filter)
    site.set_filters_and_search()
    links = CheckLinks(site.get_driver())
    links.open_offers()
    xlsx = SaveToXlsx(links.get_data_about_flat())
    xlsx.export_to_excel()
    site.get_driver().quit()

if __name__ == '__main__':
    main()