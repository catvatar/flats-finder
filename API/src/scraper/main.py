from OpenWebsite import OpenWebsite
from CheckLinks import CheckLinks
from SaveToXlsx import SaveToXlsx
import CLIParser
import BrowserInterface

def main():
    listing_filter_arguments = CLIParser.RealEstateSearchCriteria().get_parsed_arguments()

    # Open website and set filters
    scraper = BrowserInterface.WebScraper.InteractWithWebsite("https://www.otodom.pl/").set_filters();

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