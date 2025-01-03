from OpenWebsite import OpenWebsite
from CheckLinks import CheckLinks
from SaveToXlsx import SaveToXlsx
import CLIParser
import BrowserInterface

def main():
    listing_filter_arguments = CLIParser.RealEstateSearchCriteria().get_parsed_arguments()

    browser = BrowserInterface.WebDriver()
    browser.start_browser()

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
    browser.quit()


if __name__ == '__main__':
    main()