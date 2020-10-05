import requests
from bs4 import BeautifulSoup

url = 'https://hogangnono.com/search?q=%EA%B2%BD%EA%B8%B0%EB%8F%84%20%EA%B9%80%ED%8F%AC%EC%8B%9C%20%ED%92%8D%EB%AC%B4%EB%8F%99'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# 해당지역 단지 목록 가져오기
area_list = soup.find_all('li', attrs={'class', 'apt'})
print(area_list)