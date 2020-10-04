from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://naver.com')

btn_login_elem = browser.find_element_by_class_name('link_login')
btn_login_elem.click()

browser.find_element_by_id('id').send_keys('dung8524')
browser.find_element_by_id('pw').send_keys('pw')
browser.find_element_by_id('log.login').click()