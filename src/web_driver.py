
from selenium import webdriver as selenium_webdriver
# from bs4 import BeautifulSoup

import requests

import time

class WebDriver:
    selenium_driver = None
    def __init__(self):
        pass
        options = selenium_webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.selenium_driver = selenium_webdriver.Firefox(options=options)


    def get_outgoing_links(self, url):
        print('\t##WebDriver\n\t\tprocessing otodom page:\n- ',url)
        t1 = time.perf_counter(), time.process_time()
        self.selenium_driver.get(url)
        t2 = time.perf_counter(), time.process_time()
        links = []
        my_xpath = './/a'
        kubas_xpath = './/a[@data-cy="listing-item-link"]'

        for a in self.find_elements_by_xpath(kubas_xpath):
            links.append(a.get_attribute('href'))
        t3 = time.perf_counter(), time.process_time()
        
        print(f'\t##WebDriver\n\t\tProfiler: driver get: {t2[0] - t1[0]}')
        print(f'\t##WebDriver\n\t\tProfiler: loop append: {t3[0] - t2[0]}')
        return links

    def find_elements_by_xpath(self, xpath):
        return self.selenium_driver.find_elements(by='xpath', value=xpath)