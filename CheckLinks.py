from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class CheckLinks:
    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def find_offers(self):
        WebDriverWait(self.get_driver(), 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-form-more-filters"]')))
        elements = self.get_driver().find_elements(By.XPATH, '//span[@data-cy="listing-item-title"]')
        for element in elements:
            parent_element = element.find_element(By.XPATH, './ancestor::a')
            link = parent_element.get_attribute('href')
            title = element.text

            print(f"Title: {title}, Link: {link}")