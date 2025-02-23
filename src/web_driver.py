from selenium import webdriver as selenium_webdriver

class WebDriver:
    selenium_driver = None
    def __init__(self):
        options = selenium_webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.selenium_driver = selenium_webdriver.Firefox(options=options)


    def get_outgoing_links(self, url, *arg):
        xpath = './/a'
        if len(arg) > 0:
            xpath = arg[0]

        self.selenium_driver.get(url)
        links = []

        for a in self.find_elements_by_xpath(xpath):
            links.append(a.get_attribute('href'))        
        return links

    def find_elements_by_xpath(self, xpath):
        return self.selenium_driver.find_elements(by='xpath', value=xpath)