from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def sale_page():
    browser = webdriver.Chrome()
    browser.get('https://magento.softwaretestingboard.com/')
    sleep(1)
    sale_link = browser.find_element(By.ID, 'ui-id-8' )
    sale_link.click()
    sale_title = browser.find_element(By.TAG_NAME, 'h1')
    assert sale_title.text == 'Sale'


sale_page()