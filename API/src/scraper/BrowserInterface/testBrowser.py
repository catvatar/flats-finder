import unittest
from WebDriver import *

# TODO - Test start_browser, start_browser_headless and quit methods
class TestBrowser(unittest.TestCase):
    def test_start_browser(self):
        browser = WebDriver()
        browser.start_browser()
        self.assertIsNotNone(browser.driver)
        browser.quit()

    def test_start_browser_headless(self):
        browser = WebDriver()
        browser.start_browser_headless()
        self.assertIsNotNone(browser.driver)
        browser.quit()


    def test_open_website(self):
        browser = WebDriver()
        browser.start_browser_headless()
        browser.visit('https://www.google.com')
        self.assertEqual(browser.driver.current_url, 'https://www.google.com/')
        browser.quit()
    

    def test_set_and_get_cookie(self):
        browser = WebDriver()
        browser.start_browser_headless()
        browser.visit('https://www.google.com')
        cookie = {'name': 'cookie1', 'value': 'value1'}
        browser.set_cookie(cookie)
        self.assertEqual(browser.get_cookie('cookie1')['value'], 'value1')
        browser.quit()

    def test_set_cookies(self):
        browser = WebDriver()
        browser.start_browser_headless()
        browser.visit('https://www.google.com')
        cookies = [
            {'name': 'cookie1', 'value': 'value1'},
            {'name': 'cookie2', 'value': 'value2'}
        ]
        browser.set_cookies(cookies)
        self.assertEqual(browser.get_cookie('cookie1')['value'], 'value1')
        self.assertEqual(browser.get_cookie('cookie2')['value'], 'value2')
        browser.quit()

if __name__ == '__main__':
    unittest.main()
