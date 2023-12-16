import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class OpenWebsite:
    def __init__(self, price_min, price_max, min_area, max_area, place, time_filter, market_type):
        self.price_min = price_min
        self.price_max = price_max
        self.min_area = min_area
        self.max_area = max_area
        self.driver = self.setup_webdriver()
        self.place = place
        self.time_filter = time_filter
        self.market_type = market_type

    def get_time_filter(self):
        return self.time_filter
    
    def get_place(self):
        return self.place

    def get_price_min(self):
        return self.price_min
    
    def get_price_max(self):
        return self.price_max
    
    def get_min_area(self):
        return self.min_area
    
    def get_max_area(self):
        return self.max_area
    
    def get_driver(self):
        return self.driver
    
    def get_market_type(self):
        return self.market_type

    def setup_webdriver(self):
        options = Options()
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference('media.webspeech.synth.enabled', False)
        options.add_argument('--headless')

        driver = webdriver.Firefox(options=options)
        driver.get("https://www.otodom.pl/")
        driver.add_cookie({'name' : 'OptanonAlertBoxClosed', 'value' : '2023-12-11T20:46:16.795Z'})
        # driver.maximize_window()
        return driver
        
    def set_filters_and_search(self):
        input_min_price = self.get_driver().find_element(By.ID, 'priceMin').send_keys(self.get_price_min())
        input_max_price = self.get_driver().find_element(By.ID, 'priceMax').send_keys(self.get_price_max())
        input_min_area = self.get_driver().find_element(By.ID, 'areaMin').send_keys(self.get_min_area())
        input_max_area = self.get_driver().find_element(By.ID, 'areaMax').send_keys(self.get_max_area())
        input_location = self.get_driver().find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/button/div[2]').click()
        input_location = self.get_driver().find_element(By.XPATH, '//*[@id="location-picker-input"]')
        input_location.send_keys(self.get_place())
        WebDriverWait(self.get_driver(), 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/div[1]/div/div[2]/ul/li[1]/label[1]'))).click()
        time.sleep(1)
        self.get_driver().find_element(By.XPATH, '//*[@id="search-form-submit"]').click()
        WebDriverWait(self.get_driver(), 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search-form-more-filters"]'))).click()
        if self.get_time_filter() == 'any':
            self.get_driver().find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[1]/label[1]').click()
        elif self.get_time_filter() == 'last24h':
            self.get_driver().find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[2]/label[1]').click()
        elif self.get_time_filter() == 'last3d':
            self.get_driver().find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[3]/label[1]').click()
        elif self.get_time_filter() == 'last7d':
            self.get_driver().find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[4]/label[1]').click()
        
        if self.get_market_type() == 'primary':
            self.get_driver().find_element(By.CSS_SELECTOR, 'div.css-1qtzbvd:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)').click()
            action = ActionChains(self.get_driver())
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ENTER).perform()
        elif self.get_market_type() == 'secondary':
            self.get_driver().find_element(By.CSS_SELECTOR, 'div.css-1qtzbvd:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)').click()
            action = ActionChains(self.get_driver())
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ENTER).perform()

        
        
        time.sleep(1)
        self.get_driver().find_element(By.XPATH, '//*[@id="search-form-submit"]').click()



