from OpenWebsite import OpenWebsite
from CheckLinks import CheckLinks
from SaveToXlsx import SaveToXlsx
import CLIParser

def main():
    listing_filter_arguments = CLIParser.ListingFilterArguments().get_parsed_arguments()

    # Open website and set filters
    site = OpenWebsite(args)
    site.set_filters_and_search()

    # Check links and save
    links = CheckLinks(site.get_driver())
    links.open_offers()

    # Save to xlsx
    xlsx = SaveToXlsx(links.get_data_about_flat())
    xlsx.export_to_excel()

    # Close browser
    site.get_driver().quit()


if __name__ == '__main__':
    main()