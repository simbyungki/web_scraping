from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://flight.naver.com/flights/'
browser.get(url)

# 도착지
browser.find_element_by_link_text('도착').click()
browser.find_element_by_link_text('제주').click()

# 날짜선택
browser.find_element_by_link_text('가는날 선택').click()
browser.find_elements_by_link_text('29')[0].click()
browser.find_elements_by_link_text('30')[0].click()

# 인원선택
browser.find_element_by_link_text('성인 1명').click()
browser.find_elements_by_class_name('btn_increase')[0].click()
browser.find_elements_by_class_name('btn_increase')[1].click()
browser.find_element_by_class_name('btn_trip_person').click()

# 검색
browser.find_element_by_link_text('항공권 검색').click()

try : 
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
finally : 
    browser.quit()