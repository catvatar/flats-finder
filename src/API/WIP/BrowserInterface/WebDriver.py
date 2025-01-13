import selenium.webdriver as seleniumWebdriver
import selenium.webdriver.support as seleniumSupport
import selenium.webdriver.support.wait as seleniumWait
import selenium.webdriver.common.by as seleniumSelector

options = None
driver = None
browserType = None


def start_browser_headless():
    __set_headless__()
    start_browser()

def start_browser():
    __setOptions__()
    if browserType == 'firefox':
        __create_Firefox_driver__()

def visit(url):
    driver.get(url)

def click_element_when_clickable(lement):
    seleniumWait.WebDriverWait(driver, 10).until(__element_is_clickable__(element)).click()

def type_to_element_by_id(id, keys):
    find_element_by_id(id).send_keys(keys)

def type_to_element_by_xpath(xpath, keys):
    find_element_by_xpath(xpath).send_keys(keys)

def click_element_by_id(id):
    find_element_by_id(id).click()

def click_element_by_xpath(xpath):
    find_element_by_xpath(xpath).click()
    
def click_element_by_css_selector(css_selector):
    find_element_by_xpath(css_selector).click()        

def find_element_by_id(id):
    return __find_element__(seleniumSelector.By.ID, id)

def find_element_by_xpath(xpath):
    return __find_element__(seleniumSelector.By.XPATH, xpath)

def find_element_by_css_selector(css_selector):
    return __find_element__(seleniumSelector.By.CSS_SELECTOR, css_selector)        

def set_cookies(cookies):
    for cookie in cookies:
        set_cookie(cookie)

def set_cookie(cookie):
    driver.add_cookie(cookie)

def get_cookie(name):
    return driver.get_cookie(name)

def quit():
    driver.quit()

def __element_is_clickable__(element):
    return seleniumSupport.expected_conditions.element_to_be_clickable(element)

def __find_element__(By, param):
    return driver.find_element(By, param)

def __setOptions__():
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.webspeech.synth.enabled', False)

def __set_headless__():
    options.add_argument('--headless')    

def __create_Firefox_driver__():
    driver = seleniumWebdriver.Firefox(options=options)

def performActionChain(actions):
    action = seleniumWebdriver.ActionChains(driver)
    for act in actions:
        action.send_keys(act)
    action.perform()


if browser == 'firefox':
    browserType = 'firefox'
    options = seleniumWebdriver.FirefoxOptions()
