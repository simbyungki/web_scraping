# scraping default
import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

for i in range(1, 6) : 
	# print('페이지 : ', i)
	
	url = 'https://www.coupang.com/np/search?q=%EC%98%AC%EB%B0%94%EC%8A%A4+%EC%98%A4%EC%9D%BC+%EC%B9%A0%EB%93%9C%EB%9F%B0&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='.format(i)

	res = requests.get(url, headers=headers)
	res.raise_for_status()

	soup = BeautifulSoup(res.text, 'lxml')

	item_group = soup.find('ul', attrs={'class': 'search-product-list'})
	items = item_group.find_all('li', attrs={'class': re.compile('^search-product')})
	# print(items[0].find('div', attrs={'class', 'name'}).get_text())

	for item in items :
		# 제품명 
		name = item.find('div', attrs={'class': 'name'}).get_text()
		# 가격정보
		price = item.find('strong', attrs={'class': 'price-value'}).get_text()
		# 평점
		rate = item.find('em', attrs={'class': 'rating'})
		# 리뷰 수
		rate_cnt = item.find('span', attrs={'class': 'rating-total-count'})
		# 상품 url 
		link_url = item.find('a', attrs={'class': 'search-product-link'})['href']
		# 광고 뱃지
		ad_badge = item.find('span', attrs={'class': 'ad-badge-text'})


		# 광고 제품 제외
		if ad_badge : 
			continue

		# 리뷰 없는 경우
		if rate : 
			rate = rate.get_text()
			rate_cnt = rate_cnt.get_text()[1:-1]
		else :
			continue

		if float(rate) >= 4.5 and int(rate_cnt) >= 50 :
			#print(name, price, rate, rate_cnt)
			print(f'제품명 : {name}')
			print(f'가격 : {price}')
			print(f'평점 : {rate}점 ({rate_cnt}개)')
			print('바로가기 : {0}'.format('https://www.coupang.com' + link_url))
		else :
			continue
				
		
		print('-' *150)

