import unittest
from WebDriver import *

class TestBrowser(unittest.TestCase):
    def test_start_browser(self):
        browser = WebDriver()
        browser.start_browser()
        self.assertIsNotNone(browser.driver)
        browser.quit()
    
    def test_quit(self):
        browser = WebDriver()
        browser.start_browser()
        self.assertIsNotNone(browser.driver)
        browser.quit()
        self.assertIsNone(browser.driver)

    def test_start_browser_headless(self):
        browser = WebDriver()
        browser.start_browser()
        browser.start_browser_headless()
        self.assertIsNotNone(browser.driver)
        browser.quit()

    def setUp(self):
        self.browser = WebDriver()
        self.browser.start_browser()
    
    def tearDown(self):
        self.browser.quit()

    def test_set_cookies(self):
        cookies = [
            {'name': 'cookie1', 'value': 'value1'},
            {'name': 'cookie2', 'value': 'value2'}
        ]
        self.browser.set_cookies(cookies)
        self.assertEqual(self.browser.get_cookie('cookie1')['value'], 'value1')
        self.assertEqual(self.browser.get_cookie('cookie2')['value'], 'value2')

    def test_set_and_get_cookie(self):
        cookie = {'name': 'cookie1', 'value': 'value1'}
        self.browser.set_cookie(cookie)
        print(self.browser.get_cookie('cookie1'))
        self.assertEqual(self.browser.get_cookie('cookie1'), cookie)

    def test_open_website(self):
        self.browser.open_website('https://www.google.com')
        self.assertEqual(self.browser.driver.current_url, 'https://www.google.com/')

if __name__ == '__main__':
    unittest.main()
