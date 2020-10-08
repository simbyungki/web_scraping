import requests
import time
from bs4 import BeautifulSoup

headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0'

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

land_list = soup.find('div', attrs={'class', 'wrap_tbl tbl_trade'}).find('tbody').find_all('tr')

for idx, row in enumerate(land_list) :
	_type = row.find('td', attrs={'class': 'col1'}).get_text()
	_size = row.find('td', attrs={'class': 'col2'}).get_text()
	_price = row.find('td', attrs={'class': 'col3'}).get_text()
	_dong = row.find('td', attrs={'class': 'col4'}).get_text()
	_floor = row.find('td', attrs={'class': 'col5'}).get_text()
	
	print(f'===================매물 {idx +1}=====================')
	print(f'거래 : {_type}')
	print(f'면적 : {_size}')
	print(f'가격 : {_price}')
	print(f'동 : {_dong}')
	print(f'층 : {_floor}')


# https://youtu.be/yQ20jZwDjTE?t=16347