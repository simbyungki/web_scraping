import requests
from bs4 import BeautifulSoup

def create_soup(url) :
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	res = requests.get(url, headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	return soup

def get_daum_news(keyword, cnt) : 
	url = f'https://search.daum.net/search?w=news&sort=recency&q={keyword}&cluster=n&DA=STC&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=&ed=&period='
	soup = create_soup(url)
	news_list = soup.find('ul', attrs={'id': 'newsResultUL'}).find_all('li', limit = cnt)

	print('-'* 100)
	print()
	print(f'[다음 "{keyword}" 검색결과]')
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

def get_naver_news(keyword, cnt) :
	url = f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
	soup = create_soup(url)
	news_list = soup.find('ul', attrs={'class': 'type01'}).find_all('li', limit = cnt)

	print('-'* 100)
	print()
	print(f'[네이버 "{keyword}" 검색결과]')
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

def get_news_list() :
	get_naver_news('오토플러스', 5)
	get_naver_news('리본카', 5)

	get_daum_news('오토플러스', 5)
	get_daum_news('리본카', 5)


if __name__ == '__main__' : 
	get_news_list()