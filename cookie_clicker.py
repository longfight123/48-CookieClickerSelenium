"""

This script plays the cookie clicker game and obtains a high score.

This script requires that 'selenium' be installed within the Python
environment you are running this script in.

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time

chrome_driver_path = 'C:\Development\chromedriver'

time_5_minutes = time.time() + 60*5
driver = webdriver.Chrome(chrome_driver_path)
driver.get(url='http://orteil.dashnet.org/experiments/cookie/')
cookie_element = driver.find_element_by_id(id_='cookie')

cursor_element = driver.find_element_by_id('buyCursor')
grandma_element = driver.find_element_by_id('buyGrandma')
factory_element = driver.find_element_by_id('buyFactory')
mine_element = driver.find_element_by_id('buyMine')
shipment_element = driver.find_element_by_id('buyShipment')
alchemy_lab_element = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]')
portal_element = driver.find_element_by_id('buyPortal')
time_machine_element = driver.find_element_by_xpath('//*[@id="buyTime machine"]')

while time.time() < time_5_minutes:
    money = int(driver.find_element_by_id('money').text)
    time_machine_cost = int(''.join(driver.find_element_by_xpath('//*[@id="buyTime machine"]/b').text.split(' ')[3].split(',')))
    portal_cost = int(''.join(driver.find_element_by_css_selector('#buyPortal b').text.split(' ')[2].split(',')))
    alchemy_lab_cost = int(''.join(driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b').text.split(' ')[3].split(',')))
    shipment_cost = int(''.join(driver.find_element_by_css_selector('#buyShipment b').text.split(' ')[2].split(',')))
    mine_cost = int(''.join(driver.find_element_by_css_selector('#buyPortal b').text.split(' ')[2].split(',')))
    factory_cost = int(''.join(driver.find_element_by_css_selector('#buyFactory b').text.split(' ')[2].split(',')))
    grandma_cost = int(''.join(driver.find_element_by_css_selector('#buyGrandma b').text.split(' ')[2].split(',')))
    cursor_cost = int(''.join(driver.find_element_by_css_selector('#buyCursor b').text.split(' ')[2].split(',')))
    while money > time_machine_cost:
        time_machine_element = driver.find_element_by_xpath('//*[@id="buyTime machine"]')
        time_machine_element.click()
        money -= time_machine_cost
        time.sleep(1.5)
        time_machine_cost = int(''.join(driver.find_element_by_xpath('//*[@id="buyTime machine"]/b').text.split(' ')[3].split(',')))
    while money > portal_cost:
        portal_element = driver.find_element_by_id('buyPortal')
        portal_element.click()
        money -= portal_cost
        time.sleep(1.5)
        portal_cost = int(''.join(driver.find_element_by_css_selector('#buyPortal b').text.split(' ')[2].split(',')))
    while money > alchemy_lab_cost:
        alchemy_lab_element = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]')
        alchemy_lab_element.click()
        money -= alchemy_lab_cost
        time.sleep(1.5)
        alchemy_lab_cost = int(''.join(driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b').text.split(' ')[3].split(',')))
    while money > shipment_cost:
        shipment_element = driver.find_element_by_id('buyShipment')
        shipment_element.click()
        money -= shipment_cost
        time.sleep(1.5)
        shipment_cost = int(''.join(driver.find_element_by_css_selector('#buyShipment b').text.split(' ')[2].split(',')))
    while money > mine_cost:
        mine_element = driver.find_element_by_id('buyMine')
        mine_element.click()
        money -= mine_cost
        time.sleep(1.5)
        mine_cost = int(''.join(driver.find_element_by_css_selector('#buyPortal b').text.split(' ')[2].split(',')))
    while money > factory_cost:
        factory_element = driver.find_element_by_id('buyFactory')
        factory_element.click()
        money -= factory_cost
        time.sleep(1.5)
        factory_cost = int(''.join(driver.find_element_by_css_selector('#buyFactory b').text.split(' ')[2].split(',')))
    while money > grandma_cost:
        grandma_element = driver.find_element_by_id('buyGrandma')
        grandma_element.click()
        money -= grandma_cost
        time.sleep(1.5)
        grandma_cost = int(''.join(driver.find_element_by_css_selector('#buyGrandma b').text.split(' ')[2].split(',')))
    while money > cursor_cost:
        cursor_element = driver.find_element_by_id('buyCursor')
        cursor_element.click()
        money -= cursor_cost
        time.sleep(1)
        cursor_cost = int(''.join(driver.find_element_by_css_selector('#buyCursor b').text.split(' ')[2].split(',')))
    time_5_seconds = time.time() + 5
    while time.time() < time_5_seconds:
        cookie_element.click()
cookies_per_second = driver.find_element_by_id('cps').text
print(cookies_per_second)
driver.quit()