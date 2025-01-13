import time
import WebDriver

driver = None

def InteractWithWebsite(website):
    driver = WebDriver
    driver.start_browser_headless()
    driver.visit(website)
