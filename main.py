from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def loadDriver():
    return webdriver.Chrome('chromedriver/chromedriver')


def navigate_to_mobile_product_page(driver):
    mobile_button = driver.find_element(By.CLASS_NAME, 'tcom-product-list__item-container')
    mobile_button.send_keys(Keys.RETURN)


def navigate_to_mobile_phones(driver):

    select_1 = Select(driver.find_element(By.NAME, 'select1'))
    select_1.select_by_visible_text('not with Telstra')

    select_2 = Select(driver.find_element(By.NAME, 'select2'))
    select_2.select_by_visible_text('Mobile plan or device')

    select_3 = Select(driver.find_element(By.NAME, 'select3'))
    select_3.select_by_visible_text('Explore mobile phones')

    take_me_there_button = driver.find_element(By.CLASS_NAME, 'tcom-need-based-navigation__submit-btn')
    take_me_there_button.send_keys(Keys.RETURN)


def navigate_device_selection(driver):
    driver.implicitly_wait(2)
    apple_checkbox = driver.find_element(By.ID, 'filter-brand-Apple')
    apple_checkbox.send_keys(Keys.SPACE)

    select_1 = Select(driver.find_element(By.ID, 'deviceSortOptions'))
    select_1.select_by_visible_text('Price: Low to high')

    container = driver.find_element(By.CLASS_NAME, 'device-grid__grid-panel--threeacross')
    lists = container.find_elements(By.TAG_NAME, 'section')
    # for e in lists:
    #     print(e.get_attribute('aria-labelledby'))

    lists[0].click()


def take_screenshot(driver):
    now = datetime.now()
    dt_string = now.strftime("screenshots/%d%m%Y-%H%M%S.png")

    driver.get_screenshot_as_file(dt_string)


if __name__ == '__main__':
    driver = loadDriver()
    driver.get("https://www.telstra.com.au/")
    print(driver.title)
    navigate_to_mobile_product_page(driver)
    print(driver.title)
    navigate_to_mobile_phones(driver)
    print(driver.title)
    # driver.get('https://www.telstra.com.au/mobile-phones/mobiles-on-a-plan')
    navigate_device_selection(driver)
    print(driver.title)
    take_screenshot(driver)
    driver.close()

