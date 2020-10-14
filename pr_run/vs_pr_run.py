import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_soup(url) :
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	res = requests.get(url, headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	return soup

our_keywords = ['오토플러스', '리본카']
competition_keywords = ['케이카' ,'엔카닷컴' ,'KB차차차' ,'첫차' ,'AJ셀카' ,'직카']
industry_keywords = ['중고차'  ,'국산차' ,'수입차' ,'모빌리티' ,'자동차(시장, 업계, 트렌드)' ,'현대캐피탈' ,'현대캐피탈 인증중고차' ,'중고차(수입, 직영, 매매, 리스, 할부)']

def get_daum_news_recency(keyword, cnt) : 
	url = f'https://search.daum.net/search?w=news&sort=recency&q={keyword}&cluster=n&DA=STC&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=&ed=&period='
	soup = get_soup(url)
	news_list = soup.find('ul', attrs={'id': 'newsResultUL'}).find_all('li', limit = cnt)

	print('-'* 100)
	print()
	print(f'[다음 "{keyword}" 검색결과 >> 최신]')
	print()
	for idx, news in enumerate(news_list) :
		title = news.find('a', attrs={'class': 'f_link_b'}).get_text()
		link = news.find('a', attrs={'class': 'f_link_b'})['href']
		get_created = news.find('span', attrs={'class': 'f_nb date'}).contents
		
		date = get_created[0].strip()
		media = get_created[2].strip()

		print(f'{str(idx +1).zfill(2)}. [{date}] [{media}]')
		print(f'    {title}')
		print(f'    {link}')
	
	print()

def get_daum_news_relation(keyword, cnt) : 
	url = f'https://search.daum.net/search?w=news&sort=accuracy&q={keyword}&cluster=y&DA=PGD&dc=STC&pg=1&r=1&p=1&rc=1&at=more'
	soup = get_soup(url)
	news_list = soup.find('ul', attrs={'id': 'clusterResultUL'}).find_all('li', limit = cnt)

	print('-'* 100)
	print()
	print(f'[다음 "{keyword}" 검색결과 >> 연관]')
	print()
	for idx, news in enumerate(news_list) :
		title = news.find('a', attrs={'class': 'f_link_b'}).get_text()
		link = news.find('a', attrs={'class': 'f_link_b'})['href']
		get_created = news.find('span', attrs={'class': 'f_nb date'}).contents
		
		date = get_created[0].strip()
		media = get_created[2].strip()

		print(f'{str(idx +1).zfill(2)}. [{date}] [{media}]')
		print(f'    {title}')
		print(f'    {link}')
	
	print()

def get_naver_news_recency(keyword, cnt) :
	url = f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3A1d%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
	soup = get_soup(url)
	news_list = soup.find('ul', attrs={'class': 'type01'}).find_all('li', limit = cnt)

	print('-'* 100)
	print()
	print(f'[네이버 "{keyword}" 검색결과 >> 최신]')
	print()
	for idx, news in enumerate(news_list) :
		title = news.find('a', attrs={'class': '_sp_each_title'}).get_text()
		link = news.find('a', attrs={'class': '_sp_each_title'})['href']
		media = news.find('span', attrs={'class': '_sp_each_source'}).get_text()

		get_created_idx = 3
		is_news_paper = news.find('span', attrs={'class': 'newspaper'})
		if is_news_paper : 
			get_created_idx = 7
		
		get_created = news.find('dd', attrs={'class': 'txt_inline'}).contents[get_created_idx].strip()

		print(f'{str(idx +1).zfill(2)}. [{get_created}] [{media}]')
		print(f'    {title}')
		print(f'    {link}')
	
	print()

def get_naver_news_relation(keyword, cnt) :
	today_date = datetime.today().strftime('%Y년%m월%d일')
	# url = f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_srt&sort=0&photo=0&field=0&reporter_article=&pd=0&ds={today_date}&de=&docid=&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
	url = f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=4&ds=&de=&docid=&nso=so%3Ar%2Cp%3A1d%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
	print(url)
	soup = get_soup(url)
	news_list = soup.select('ul.type01 > li')[:cnt]
	print('-'* 100)
	print()
	if news_list :
		total_cnt = soup.find('div', attrs={'class': 'title_desc all_my'}).get_text().replace('1-10 / ', '')
		print(f'[네이버 {today_date} "{keyword}" 검색결과 총 {total_cnt} (연관)]')
		print()

		for idx, news in enumerate(news_list) :
			title = news.find('a', attrs={'class': '_sp_each_title'}).get_text()
			link = news.find('a', attrs={'class': '_sp_each_title'})['href']
			media = news.find('span', attrs={'class': '_sp_each_source'}).get_text()

			get_created_idx = 3
			is_news_paper = news.find('span', attrs={'class': 'newspaper'})
			if is_news_paper : 
				get_created_idx = 7
			
			get_created = news.find('dd', attrs={'class': 'txt_inline'}).contents[get_created_idx].strip()


			print(f'{str(idx +1).zfill(2)}. [{get_created}] [{media}]')
			print(f'    {title}')
			print(f'    {link}')

			# 관련 뉴스의 목록 가져오기 (현재 미사용 예정)
			# is_relation_news_list = news.find('ul', attrs={'class': 'relation_lst'})
			# if is_relation_news_list :
			# 	is_more_news_title = news.find('a', attrs={'class', 'more_news'})
			# 	if is_more_news_title :
			# 		more_news_title = is_more_news_title.get_text()
			# 		more_news_num = is_more_news_title['onclick'].split("option('")[1].split("'")[0]
			# 		print(f'     ㄴ[{more_news_title}]')
			# 		# print(f'       https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_srt&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid={more_news_num}&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=1')
					
			# 		re_soup = get_soup(f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_srt&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid={more_news_num}&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=1')
			# 		re_news_list = re_soup.select('ul.type01 > li')
			# 		for re_idx, re_news in enumerate(re_news_list) :
			# 			re_title = re_news.find('a', attrs={'class': '_sp_each_title'}).get_text()
			# 			re_link = re_news.find('a', attrs={'class': '_sp_each_title'})['href']
			# 			re_media = re_news.find('span', attrs={'class': '_sp_each_source'}).get_text()

			# 			re_get_created_idx = 3
			# 			is_re_news_paper = re_news.find('span', attrs={'class': 'newspaper'})
			# 			if is_re_news_paper : 
			# 				re_get_created_idx = 7
						
			# 			re_get_created_idx = re_news.find('dd', attrs={'class': 'txt_inline'}).contents[re_get_created_idx].strip()

			# 			print(f'       {str(idx +1).zfill(2)}-{str(re_idx +1).zfill(2)}. [{re_get_created_idx}] [{re_media}]')
			# 			print(f'           {re_title}')
			# 			print(f'           {re_link}')
				
			print()
		print()
	else :
		print(f'"{keyword}" 검색결과 없음')
		print()


# 자사뉴스
def autoplus_news() :
	for keyword in our_keywords :
		# get_daum_news_recency(keyword, 10)
		# get_naver_news_recency(keyword, 10)
		# get_daum_news_relation(keyword, 10)
		get_naver_news_relation(keyword, 10)
	
# 경쟁사 뉴스
def competition_news() :
	for keyword in competition_keywords :
		# get_daum_news_recency(keyword, 10)
		# get_naver_news_recency(keyword, 10)
		# get_daum_news_relation(keyword, 10)
		get_naver_news_relation(keyword, 10)

# 업계 뉴스
def industry_news() :
	for keyword in industry_keywords :
		# get_daum_news_recency(keyword, 10)
		# get_naver_news_recency(keyword, 10)
		# get_daum_news_relation(keyword, 10)
		get_naver_news_relation(keyword, 10)



if __name__ == '__main__' :
	autoplus_news()
	competition_news()
	industry_news()