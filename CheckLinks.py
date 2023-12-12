from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class CheckLinks:
    def __init__(self, driver):
        self.driver = driver
        self.offer_and_title = self.retreive_offer_and_title()

    def get_driver(self):
        return self.driver
    
    def get_offer_and_title(self):
        return self.offer_and_title

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
        return offer_and_title

    def open_offers(self):
        offers_dict = self.get_offer_and_title()
        link = 'https://www.otodom.pl/pl/oferta/odbior-2023-pietro-8-2-pokoje-bezposrednio-ID4nKmQ'
        # for link in offers_dict.keys():
        # print(link)
        self.get_driver().execute_script("window.open('','_blank');")
        self.get_driver().switch_to.window(self.get_driver().window_handles[-1])
        self.get_driver().get(link)
        self.retreive_important_data()

    def retreive_important_data(self):
        adress = self.get_driver().find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/header/div[2]/a')
        price = self.get_driver().find_element(By.CSS_SELECTOR, '[data-cy="adPageHeaderPrice"]')
        size = self.get_driver().find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/div[2]/div')
        floor = self.get_driver().find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div[5]/div[2]/div')
        building_date = self.get_driver().find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[5]/div/div[4]/div[2]/span/span/div')
        building_material = self.get_driver().find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[5]/div/div[12]/div[2]/span/span/div')
        print(adress.text)
        print(price.text)
        print(size.text)
        print(floor.text)
        print(building_date.text)
        print(building_material.text)
