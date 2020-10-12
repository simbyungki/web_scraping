import requests
from bs4 import BeautifulSoup

def create_soup(url) :
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	res = requests.get(url, headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	return soup

def print_news(idx, title, link) : 
	print(f'{idx}. {title}')
	print(f'  ({link})')

def scrape_weather() :
	print('-' *150)
	print()

	url = 'https://search.naver.com/search.naver?ie=UTF-8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8&sm=chr_hty'
	soup = create_soup(url)

	w_infos01 = soup.find_all('div', attrs={'class': 'main_info'})
	location = soup.find('div', attrs={'class': '_areaSelectLayer'}).get_text().strip()
	summary = w_infos01[0].find('p', attrs={'class': 'cast_txt'}).get_text()
	curr_temp = w_infos01[0].find('span', attrs={'class': 'todaytemp'}).get_text()
	min_temp = w_infos01[0].find('span', attrs={'class': 'min'}).find('span', attrs={'class': 'num'}).get_text()
	max_temp = w_infos01[0].find('span', attrs={'class': 'max'}).find('span', attrs={'class': 'num'}).get_text()
	morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip()
	afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip()
	w_info02 = soup.find('div', attrs={'class': 'sub_info'})
	dust01 = w_info02.find('dl', attrs={'class': 'indicator'}).find_all('dd')[0].get_text()
	dust02 = w_info02.find('dl', attrs={'class': 'indicator'}).find_all('dd')[1].get_text()
	
	print(f'[{location} 오늘의 날씨]')
	print()
	print(summary)
	print(f'현재 {curr_temp}˚ (최저 {min_temp}˚ / 최고 {max_temp}˚)')
	print(f'오전 {morning_rain_rate} / 오후 {afternoon_rain_rate}')
	print()
	print(f'미세먼지 {dust01}')
	print(f'초미세먼지 {dust02}')
	print()

def scrape_headline_news() :
	print('-' *150)
	print()

	url = 'https://news.naver.com/'
	soup = create_soup(url)

	print('[헤드라인 뉴스]')
	print()
	headlines = soup.find('ul', attrs={'class':'hdline_article_list'}).find_all('li', limit = 5)
	for idx, headline in enumerate(headlines) :
		title = headline.find('div', attrs={'class':'hdline_article_tit'}).get_text().strip()
		link = 'https://news.naver.com' + headline.find('div', attrs={'class':'hdline_article_tit'}).find('a', attrs={'class':'lnk_hdline_article'})['href']
		print_news(idx +1, title, link)
	print()

def scrape_it_news() :
	print('-' *150)
	print()

	url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
	soup = create_soup(url)

	print('[IT 뉴스]')
	print()

	it_normals = soup.find('ul', attrs={'class':'type06_headline'}).find_all('li', limit = 5) 	
	for idx, it_normal in enumerate(it_normals) :
		a_idx = 0
		is_img = it_normal.find('dt', attrs={'class': 'photo'})
		if is_img :
			a_idx = 1
		a_tag =  it_normal.find_all('a')[a_idx]
		title = a_tag.get_text().strip()
		link = a_tag['href']
		print_news(idx +1, title, link)

	print()

def scrape_study_eng() :
	print('-' *150)
	print('[오늘의 한줄명언]')
	print()

	url = 'https://www.hackers.co.kr/?c=s_lec/lec_study/lec_B_others_wisesay&keywd=haceng_submain_lnb_lec_B_others_wisesay&logger_kw=haceng_submain_lnb_lec_B_others_wisesay'
	soup = create_soup(url)

	eng_wise_sayings = soup.find('div', attrs={'class':'text_en'}).find('p').get_text().strip()
	eng_writer = soup.find('div', attrs={'class':'text_en'}).find('p', attrs={'class':'writer'}).get_text().strip()
	kor_wise_sayings = soup.find('div', attrs={'class':'text_ko'}).find('p').get_text().strip()
	kor_writer = soup.find('div', attrs={'class':'text_ko'}).find('p', attrs={'class':'writer'}).get_text().strip()
	
	print(f'{eng_wise_sayings}')
	print(f'- {eng_writer} -')
	print()
	print(f'{kor_wise_sayings}')
	print(f'- {kor_writer} -')

	print()

if __name__ == '__main__' :
	scrape_weather()
	scrape_headline_news()
	scrape_it_news()
	scrape_study_eng()
