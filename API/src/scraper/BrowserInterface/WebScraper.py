import time
import WebDriver as driver
from selenium.webdriver.common.keys import Keys

    

def set_filters(args):
    driver.set_cookie({'name' : 'OptanonAlertBoxClosed', 'value' : '2023-12-11T20:46:16.795Z'})
    driver.type_to_element_by_id('priceMin', args.price_min)
    driver.type_to_element_by_id('priceMax', args.price_max)
    driver.type_to_element_by_id('areaMin', args.min_area)
    driver.type_to_element_by_id('areaMax', args.max_area)
    driver.click_element_by_xpath('/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/button/div[2]')
    driver.type_to_element_by_xpath('//*[@id="location-picker-input"]',get_place())
    inputElement = driver.find_element_by_xpath('/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/div[1]/div/div[2]/ul/li[1]/label[1]')
    driver.click_element_when_clickable(inputElement)
    time.sleep(1)
    driver.click_element_by_xpath('//*[@id="search-form-submit"]')
    searchFormMoreFiltersButton = driver.find_element_by_xpath('//*[@id="search-form-more-filters"]')
    driver.click_element_when_clickable(searchFormMoreFiltersButton)
    
    if args.time_filter == 'any':
        driver.click_element_by_xpath('/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[1]/label[1]')
    elif args.time_filter == 'last24h':
        driver.click_element_by_xpath('/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[2]/label[1]')
    elif args.time_filter == 'last3d':
        driver.click_element_by_xpath('/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[3]/label[1]')
    elif args.time_filter == 'last7d':
        driver.click_element_by_xpath('/html/body/div[1]/div[2]/main/div[2]/div[2]/div/div/form/section/div[2]/div[4]/fieldset/div/div[4]/label[1]')
    
    # TODO remove last call to selenium
    if args.market_type == 'primary':
        driver.click_element_by_css_selector('div.css-1qtzbvd:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)')
        driver.performActionChain([Keys.ARROW_DOWN, Keys.ENTER])
    elif args.market_type == 'secondary':
        driver.click_element_by_css_selector('div.css-1qtzbvd:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)')
        driver.performActionChain([Keys.ARROW_DOWN,Keys.ARROW_DOWN, Keys.ENTER])
    time.sleep(1)
    driver.click_element_by_xpath('//*[@id="search-form-submit"]')

def InteractWithWebsite(website):
    driver = WebDriver()
    driver.start_browser_headless()
    driver.visit(website)
