import time
from WebDriver import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class InteractWithWebsite:
    driver = None
    
    def __init__(self, website):
        self.driver = WebDriver()
        self.driver.start_browser_headless()
        self.driver.visit(website)
    
    def set_filters(self, args):
        self.driver.set_cookie({'name' : 'OptanonAlertBoxClosed', 'value' : '2023-12-11T20:46:16.795Z'})
        self.driver.type_to_element_by_id('priceMin', args.price_min)
        self.driver.type_to_element_by_id('priceMax', args.price_max)
        self.driver.type_to_element_by_id('areaMin', args.min_area)
        self.driver.type_to_element_by_id('areaMax', args.max_area)
        self.driver.click_element_by_xpath('/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/button/div[2]')
        self.driver.type_to_element_by_xpath('//*[@id="location-picker-input"]',self.get_place())
        inputElement = self.driver.find_element_by_xpath('/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/div[1]/div/div[2]/ul/li[1]/label[1]')
        self.driver.click_element_when_clickable(inputElement)
        time.sleep(1)
        self.driver.click_element_by_xpath('//*[@id="search-form-submit"]')
        searchFormMoreFiltersButton = self.driver.find_element_by_xpath('//*[@id="search-form-more-filters"]')
        self.driver.click_element_when_clickable(searchFormMoreFiltersButton)
        
        if args.time_filter == 'any':
            self.driver.click_element_by_xpath('/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[1]/label[1]')
        elif args.time_filter == 'last24h':
            self.driver.click_element_by_xpath('/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[2]/label[1]')
        elif args.time_filter == 'last3d':
            self.driver.click_element_by_xpath('/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[3]/label[1]')
        elif args.time_filter == 'last7d':
            self.driver.click_element_by_xpath('/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[4]/label[1]')
        
        # TODO remove last call to selenium
        if args.market_type == 'primary':
            self.driver.click_element_by_css_selector('div.css-1qtzbvd:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)')
            self.driver.performActionChain([Keys.ARROW_DOWN, Keys.ENTER])
        elif args.market_type == 'secondary':
            self.driver.click_element_by_css_selector('div.css-1qtzbvd:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)')
            self.driver.performActionChain([Keys.ARROW_DOWN,Keys.ARROW_DOWN, Keys.ENTER])
        time.sleep(1)
        self.driver.click_element_by_xpath('//*[@id="search-form-submit"]')
