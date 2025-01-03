import unittest
from WebDriver import *

class TestBrowser(unittest.TestCase):
    def test_setOptions(self):
        browser = WebDriver()
        self.assertTrue(browser.options)
        self.assertFalse(browser.options.headless)
        self.assertFalse(browser.options.preferences['dom.webnotifications.enabled'])
        self.assertFalse(browser.options.preferences['media.webspeech.synth.enabled'])

    def test_set_headless(self):
        browser = WebDriver()
        browser.set_headless()
        self.assertTrue(browser.options.headless)

    def test_start_browser(self):
        browser = WebDriver()
        self.assertTrue(browser.driver)

    def test_set_cookies(self):
        browser = WebDriver()
        cookies = [{'name': 'name', 'value': 'value'}]
        browser.set_cookies(cookies)
        self.assertEqual(browser.driver.get_cookie('name'), cookies[0])

    def test_set_cookie(self):
        browser = WebDriver()
        cookie = {'name': 'name', 'value': 'value'}
        browser.set_cookie(cookie)
        self.assertEqual(browser.driver.get_cookie('name'), cookie)

    def test_open_website(self):
        browser = WebDriver()
        browser.open_website('https://www.google.com')
        self.assertEqual(browser.driver.current_url, 'https://www.google.com')

    def test_quit(self):
        browser = WebDriver()
        browser.quit()
        self.assertFalse(browser.driver)

if __name__ == '__main__':
    unittest.main()
