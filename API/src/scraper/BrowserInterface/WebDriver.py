from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class WebDriver:
    options = None
    driver = None

    def __init__(self):
        self.options = Options()


    def start_browser_headless(self):
        self.__set_headless__()
        self.start_browser()

    def start_browser(self):
        self.__setOptions__()
        self.__create_Firefox_driver__()
    
    def __setOptions__(self):
        self.options.set_preference('dom.webnotifications.enabled', False)
        self.options.set_preference('media.webspeech.synth.enabled', False)

    def __set_headless__(self):
        self.options.add_argument('--headless')    

    def __create_Firefox_driver__(self):
        self.driver = webdriver.Firefox(options=self.options)

    def visit(self, url):
        self.driver.get(url)

    def set_cookies(self, cookies):
        for cookie in cookies:
            self.set_cookie(cookie)

    def set_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def get_cookie(self, name):
        return self.driver.get_cookie(name)


    def quit(self):
        self.driver.quit()

