import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(r'C:\Users\PC\Documents\simbyungki\git\web_scraping\chromedriver.exe', options=options)
browser.maximize_window()

url = 'https://play.google.com/store/movies/top'
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
browser.get_screenshot_as_file('play_google_movie.png')
# browser.quit()

# scraping
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
# 	'Accept-Language': 'ko-KR,ko'
# }
soup = BeautifulSoup(browser.page_source, 'lxml')
# movies = soup.find_all('div', attrs={'class', ['ImZGtf mpg5gc', 'Vpfmgd']})
movies = soup.find_all('div', attrs={'class', 'Vpfmgd'})

print(len(movies))
for movie in movies :
	title = movie.find('div', attrs={'class', 'WsMG1c nnK0zc'}).get_text()

	# 할인 전 가격
	origin_price = movie.find('span', attrs={'class', 'SUZt4c djCuy'})
	if origin_price :
		origin_price = origin_price.get_text()
	else :
		# print(title, ' >> 할인하지 않는 영화')
		continue

	# 할인 후 가격
	price = movie.find('span', attrs={'class', 'VfPpfd ZdBevf i5DZme'}).get_text()

	# 링크
	href = movie.find('a', attrs={'class', 'JC71ub'})['href']
	link = 'https://play.google.com' + href

	print(f'제목 : {title}')
	print(f'할인 전 금액 : {origin_price}')
	print(f'할인 후 금액 : {price}')
	print(f'링크 : {link}')
	print()
	print('ㅡ' *60)
	print()

browser.quit()