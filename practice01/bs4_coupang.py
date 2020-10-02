# scraping default
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

item_group = soup.find('ul', attrs={'class': 'search-product-list'})
items = item_group.find_all('li', attrs={'class': re.compile('^search-product')})
# print(items[0].find('div', attrs={'class', 'name'}).get_text())

print('-' *150)
idx = 1
for item in items :
	# 제품명 
	name = item.find('div', attrs={'class': 'name'}).get_text()
	# 가격정보
	price = item.find('strong', attrs={'class': 'price-value'}).get_text()
	# 평점
	rate = item.find('em', attrs={'class': 'rating'})
	# 리뷰 수
	rate_cnt = item.find('span', attrs={'class': 'rating-total-count'})
	# 광고 뱃지
	ad_badge = item.find('span', attrs={'class': 'ad-badge-text'})


	# 광고 제품 제외
	if ad_badge : 
		continue

	# Apple 제품 제외
	if 'Apple' in name : 
		continue

	# 리뷰 없는 경우
	if rate : 
		rate = rate.get_text()
		rate_cnt = rate_cnt.get_text()[1:-1]
	else :
		continue

	if float(rate) >= 4.5 and int(rate_cnt) >= 50 :
		print(idx)
		print(name, price, rate, rate_cnt)
		idx += 1
	else :
		continue
			
	
	print('-' *150)

