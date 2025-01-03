from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class WebDriver:
    self.options = None
    self.driver = None

    def __init__(self, headless=False):
        self.setOptions(headless)
        self.start_browser()

    def setOptions(self):
        self.options = Options()
        self.options.set_preference('dom.webnotifications.enabled', False)
        self.options.set_preference('media.webspeech.synth.enabled', False)
        if headless:
            self.set_headless()

    def set_headless(self):
        self.options.add_argument('--headless')

    def start_browser(self):
        self.driver = webdriver.Firefox(options=self.options)

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

