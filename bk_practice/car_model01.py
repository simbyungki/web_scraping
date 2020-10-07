import requests
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(r'C:\Users\PC\Documents\simbyungki\git\web_scraping\chromedriver.exe', options=options)
browser.maximize_window()

# 엔카
url = 'http://www.encar.com/fc/fc_carsearchlist.do?carType=for&searchType=model&TG.R=B#!%7B%22action%22%3A%22%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D'
# K카
# url = 'https://kbchachacha.com/public/search/main.kbc#!?_menu=buy'
browser.get(url)


# 화면 바닥
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
interval = 2

# 현재 문서 높이
prev_height = browser.execute_script('return document.body.scrollHeight')

while True :
	# 스크롤 바닥으로 내림 
	browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

	# 로딩 대기
	time.sleep(interval)

	# 현재 문서 높이
	curr_height = browser.execute_script('return document.body.scrollHeight')

	if prev_height == curr_height :
		break
	
	prev_height = curr_height

print('모든 데이터 로드 완료')

time.sleep(5)

soup = BeautifulSoup(browser.page_source, 'lxml')


car_list = soup.select('#sr_normal > tr')
# car_list = soup.select('.generalRegist > list-in > .area')

for car_row in car_list :
	car_names = car_row.find_all('span', attrs={'class': 'newLink _link'})
	for car_name in car_names :
		print(car_name.get_text())
	

# https://ngee.tistory.com/955