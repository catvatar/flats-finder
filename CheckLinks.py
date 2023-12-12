from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class CheckLinks:
    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def retreive_offer_and_title(self):
        offer_and_title = {}
        while True:
            WebDriverWait(self.get_driver(), 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-form-more-filters"]')))
            elements = self.get_driver().find_elements(By.XPATH, '//span[@data-cy="listing-item-title"]')
            next_page = self.get_driver().find_element(By.CSS_SELECTOR, '[data-cy="pagination.next-page"]')
            for element in elements:
                parent_element = element.find_element(By.XPATH, './ancestor::a')
                link = parent_element.get_attribute('href')
                title = element.text
                offer_and_title[link] = title
            if not next_page.is_enabled():
                break
            next_page.click()
        print(offer_and_title)