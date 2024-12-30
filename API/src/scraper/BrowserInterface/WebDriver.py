from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class WebDriver:
    def __init__(self):
        options = Options()
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference('media.webspeech.synth.enabled', False)
        # options.add_argument('--headless')

        self.driver = webdriver.Firefox(options=options)
        driver.get("https://www.otodom.pl/")
        driver.add_cookie({'name' : 'OptanonAlertBoxClosed', 'value' : '2023-12-11T20:46:16.795Z'})
        
    def get_webdriver(self):
        # driver.maximize_window()
        return driver

