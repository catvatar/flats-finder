from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class CheckLinks:
    def __init__(self, driver):
        self.driver = driver
        self.data_about_flat = self.retrieve_basic_data_about_flat()

    def get_driver(self):
        return self.driver
    
    def get_data_about_flat(self):
        return self.data_about_flat
    def set_data_about_flat(self, data_about_flat):
        self.data_about_flat = data_about_flat

    def retrieve_basic_data_about_flat(self):
        data_about_flat = {}
        while True:
            WebDriverWait(self.get_driver(), 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.css-nxvlyk:nth-child(1) > span:nth-child(2)')))
            elements = self.get_driver().find_elements(By.XPATH, '//span[@data-cy="listing-item-title"]')
            for element in elements:
                try:
                    link_element = element.find_element(By.XPATH, './ancestor::a')
                    link = link_element.get_attribute('href')
                    title = element.text
                    data_about_flat[link] = {'title': title}
                except StaleElementReferenceException:
                    continue

            next_page = self.get_driver().find_element(By.CSS_SELECTOR, '[data-cy="pagination.next-page"]')
            if not next_page.is_enabled():
                break
            next_page.click()

        return data_about_flat

    def open_offers(self):
        offers_dict = self.get_data_about_flat()
        for link in offers_dict.copy().keys():
            self.get_driver().execute_script("window.open('','_blank');")
            self.get_driver().switch_to.window(self.get_driver().window_handles[-1])
            self.get_driver().get(link)
            self.retreive_important_data(link)
            self.get_driver().close()
            self.get_driver().switch_to.window(self.get_driver().window_handles[0])

    def retreive_important_data(self, link):
        if self.get_with_selectors(['div.css-tpkder:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)', 'div.css-tpkder:nth-child(1) > div:nth-child(2) > div:nth-child(1)', 'div.css-tpkder:nth-child(1) > div:nth-child(2) > span:nth-child(1) > span:nth-child(1) > div:nth-child(1) > a:nth-child(1)']).text == 'pierwotny':
            offers = self.get_data_about_flat()
            del offers[link]
            self.set_data_about_flat(offers)
            return
            
        address = self.get_with_selectors(['.css-z9gx1y > a:nth-child(1)'])
        price = self.get_with_selectors(['.css-t3wmkv > button:nth-child(1)', '[data-cy="adPageHeaderPrice"]'])
        size = self.get_with_selectors(['div.css-1ivc1bc:nth-child(1) > div:nth-child(3) > span:nth-child(1) > span:nth-child(1) > div:nth-child(1)', 'div.css-1ivc1bc:nth-child(1) > div:nth-child(3) > div:nth-child(1)'])
        floor = self.get_with_selectors(['div.css-1ivc1bc:nth-child(5) > div:nth-child(3) > div:nth-child(1)'])
        building_date = self.get_with_selectors(['div.css-tpkder:nth-child(4) > div:nth-child(2) > span:nth-child(1) > span:nth-child(1) > div:nth-child(1)'])
        building_material = self.get_with_selectors(['div.css-tpkder:nth-child(12) > div:nth-child(2) > span:nth-child(1) > span:nth-child(1) > div:nth-child(1)', 'div.css-tpkder:nth-child(12) > div:nth-child(2) > div:nth-child(1)'])
        offers_dict = self.get_data_about_flat()

        address_value = address.text if address else '-'
        price_value = price.text if price else '-'
        size_value = size.text if size else '-'
        floor_value = floor.text if floor else '-'
        building_date_value = building_date.text if building_date else '-'
        building_material_value = building_material.text if building_material else '-'

        offers_dict[link]['address'] = address_value
        offers_dict[link]['price'] = price_value
        offers_dict[link]['size'] = size_value
        offers_dict[link]['floor'] = floor_value
        offers_dict[link]['building_date'] = building_date_value
        offers_dict[link]['building_material'] = building_material_value

        self.set_data_about_flat(offers_dict)

    def retreive_photos(self):
        try:
            if self.get_driver().find_element(By.CSS_SELECTOR, ".e1qwkykw1").click():
                print("yes")
        except:
            pass
        photos_number = self.get_driver().find_element(By.CSS_SELECTOR, ".image-gallery-index-total").text
        self.get_driver().find_element(By.CSS_SELECTOR, "div.image-gallery-slide:nth-child(1) > img:nth-child(1)").click()
        for i in range(1, int(photos_number) + 1):
            img = self.get_driver().find_element(By.CSS_SELECTOR, f"div.image-gallery-slide:nth-child({i}) > img:nth-child(1)")
            photo_link = img.get_attribute("src")
            print(f"Link to photo number {i}:", photo_link)
            action = ActionChains(self.get_driver())
            action.send_keys(Keys.ARROW_RIGHT).perform()
            time.sleep(1)


    def get_with_selectors(self, selectors):
        for selector in selectors:
            try:
                element = self.get_driver().find_element(By.CSS_SELECTOR, selector)
                return element
            except:
                pass
        return False

