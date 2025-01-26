
from selenium import webdriver

class SeleniumWebDriver:
    driver = None
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)

    def get_outgoing_links(self, url):
        self.driver.get(url)
        links = []
        for a in self.find_elements_by_xpath('.//a'):
            links.append(a.get_attribute('href'))
        return links

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements(by='xpath', value=xpath)