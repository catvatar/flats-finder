import unittest
from selenium import webdriver
class TestBrowser(unittest.TestCase):
    def can_open_example_com(self):
        driver = webdriver.Firefox()
        driver.get('https://example.com')
        # TODO verify the connection is established

if __name__ == '__main__':
    unittest.main()
