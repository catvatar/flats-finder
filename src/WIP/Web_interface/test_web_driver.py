import unittest
from .Browser.Driver import Driver

class TestDriver(unittest.TestCase):
    def canNavigateToWebsite(self):
        driver = Driver()
        driver.get()
        

if __name__ == '__main__':
    unittest.main()
