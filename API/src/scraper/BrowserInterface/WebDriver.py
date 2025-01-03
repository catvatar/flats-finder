from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class WebDriver:
    options = None
    driver = None

    def start_browser_headless(self):
        self.__set_headless__()
        self.start_browser()

    def start_browser(self):
        self.__setOptions__()
        self.driver = webdriver.Firefox(options=self.options)
    
    def __setOptions__(self):
        self.options = Options()
        self.options.set_preference('dom.webnotifications.enabled', False)
        self.options.set_preference('media.webspeech.synth.enabled', False)

    def __set_headless__(self):
        self.options.add_argument('--headless')    

    def set_cookies(self, cookies):
        for cookie in cookies:
            self.set_cookie(cookie)

    def set_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def open_website(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

