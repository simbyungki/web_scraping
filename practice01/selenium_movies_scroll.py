import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser = webdriver.Chrome(r'C:\Users\PC\Documents\simbyungki\git\web_scraping\chromedriver.exe')
browser.maximize_window()

url = 'https://play.google.com/store/movies/top'
browser.get(url)

# 브라우저 스크립트 실행
# browser.execute_script('window.scrollTo(0, 1080)')

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
# browser.quit()

# scraping
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
# 	'Accept-Language': 'ko-KR,ko'
# }
soup = BeautifulSoup(browser.page_source, 'lxml')
movies = soup.find_all('div', attrs={'class', 'ImZGtf mpg5gc'})

for movie in movies :
	title = movie.find('div', attrs={'class', 'WsMG1c nnK0zc'}).get_text()
	print(title)


# 4:03:52