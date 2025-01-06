import selenium.webdriver as seleniumWebdriver
import selenium.webdriver.support as seleniumSupport
import selenium.webdriver.support.wait as seleniumWait
import selenium.webdriver.common.by as seleniumSelector

class WebDriver:
    options = None
    driver = None
    browserType = None

    def __init__(self, browser='firefox'):
        if browser == 'firefox':
            self.browserType = 'firefox'
            self.options = seleniumWebdriver.FirefoxOptions()
        else:
            pass

    def start_browser_headless(self):
        self.__set_headless__()
        self.start_browser()

    def start_browser(self):
        self.__setOptions__()
        if self.browserType == 'firefox':
            self.__create_Firefox_driver__()

    def visit(self, url):
        self.driver.get(url)

    def click_element_when_clickable(self,element):
        seleniumWait.WebDriverWait(self.driver, 10).until(__element_is_clickable__(element)).click()
    
    def type_to_element_by_id(self, id, keys):
        self.find_element_by_id(id).send_keys(keys)

    def type_to_element_by_xpath(self, xpath, keys):
        self.find_element_by_xpath(xpath).send_keys(keys)

    def click_element_by_id(self, id):
        self.find_element_by_id(id).click()

    def click_element_by_xpath(self, xpath):
        self.find_element_by_xpath(xpath).click()
     
    def click_element_by_css_selector(self, css_selector):
        self.find_element_by_xpath(css_selector).click()        

    def find_element_by_id(self, id):
        return self.__find_element__(seleniumSelector.By.ID, id)

    def find_element_by_xpath(self, xpath):
        return self.__find_element__(seleniumSelector.By.XPATH, xpath)
    
    def find_element_by_css_selector(self, css_selector):
        return self.__find_element__(seleniumSelector.By.CSS_SELECTOR, css_selector)        

    def set_cookies(self, cookies):
        for cookie in cookies:
            self.set_cookie(cookie)

    def set_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def quit(self):
        self.driver.quit()

    def __element_is_clickable__(self, element):
        return seleniumSupport.expected_conditions.element_to_be_clickable(element)

    def __find_element__(self, By, param):
        return self.driver.find_element(By, param)
    
    def __setOptions__(self):
        self.options.set_preference('dom.webnotifications.enabled', False)
        self.options.set_preference('media.webspeech.synth.enabled', False)

    def __set_headless__(self):
        self.options.add_argument('--headless')    

    def __create_Firefox_driver__(self):
        self.driver = seleniumWebdriver.Firefox(options=self.options)

    def performActionChain(self, actions):
        action = seleniumWebdriver.ActionChains(self.driver)
        for act in actions:
            action.send_keys(act)
        action.perform()

