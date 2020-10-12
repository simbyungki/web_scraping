import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
url_wether = 'https://search.naver.com/search.naver?ie=UTF-8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8&sm=chr_hty'
url_headline_news = 'https://news.naver.com/'
url_it_news = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
url_study_eng = 'https://www.hackers.co.kr/?c=s_lec/lec_study/lec_B_others_wisesay&keywd=haceng_submain_lnb_lec_B_others_wisesay&logger_kw=haceng_submain_lnb_lec_B_others_wisesay'
urls = [url_wether, url_headline_news, url_it_news, url_study_eng]

for url in urls :
	res = requests.get(url, headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	if url == url_wether : # 날씨정보
		w_infos01 = soup.find_all('div', attrs={'class': 'main_info'})
		location = soup.find('div', attrs={'class': '_areaSelectLayer'}).get_text().strip()
		summary = w_infos01[0].find('p', attrs={'class': 'cast_txt'}).get_text()
		temp01 = w_infos01[0].find('span', attrs={'class': 'todaytemp'}).get_text()
		temp02 = w_infos01[0].find('span', attrs={'class': 'min'}).find('span', attrs={'class': 'num'}).get_text()
		temp03 = w_infos01[0].find('span', attrs={'class': 'max'}).find('span', attrs={'class': 'num'}).get_text()
		w_info02 = soup.find('div', attrs={'class': 'sub_info'})
		dust01 = w_info02.find('dl', attrs={'class': 'indicator'}).find_all('dd')[0].get_text()
		dust02 = w_info02.find('dl', attrs={'class': 'indicator'}).find_all('dd')[1].get_text()
		print('-' *150)
		print(f'[{location} 오늘의 날씨]')
		print(summary)
		print(f'현재 {temp01}˚ (최저 {temp02}˚ / 최고 {temp03}˚)')
		#print(f'오전 강수확률 00% / 오후 강수확률 00%')
		print(f'미세먼지 {dust01}')
		print(f'초미세먼지 {dust02}')
	elif url == url_headline_news :	# 헤드라인 뉴스
		headlines = soup.find('ul', attrs={'class':'hdline_article_list'}).find_all('li')
		print('-' *150)
		print('[헤드라인 뉴스]')
		for idx, headline in enumerate(headlines) :
			headline_title = headline.find('div', attrs={'class':'hdline_article_tit'}).get_text().strip()
			headline_link = 'https://news.naver.com' + headline.find('div', attrs={'class':'hdline_article_tit'}).find('a', attrs={'class':'lnk_hdline_article'})['href']
			print(f'{idx +1}. {headline_title}')
			print(f'  ({headline_link})')
	elif url == url_it_news : # IT 헤드라인 뉴스
		it_normals = soup.find('ul', attrs={'class':'type06_headline'}).find_all('li')
		print('-' *150)
		print('[IT 뉴스]')
		for idx, it_normal in enumerate(it_normals) :
			if it_normal.find('dt', attrs={'class': 'photo'}) :
				it_normal_title = it_normal.find_all('dt')[1].get_text().strip()
			else :
				it_normal_title = it_normal.find('dt').get_text().strip()
			it_normal_link = it_normal.find('dt').find('a')['href']
			print(f'{idx +1}. {it_normal_title}')
			print(f'  ({it_normal_link})')
	else : # 오늘의 한줄명언(영/한)
		eng_wise_sayings = soup.find('div', attrs={'class':'text_en'}).find('p').get_text().strip()
		eng_writer = soup.find('div', attrs={'class':'text_en'}).find('p', attrs={'class':'writer'}).get_text().strip()
		kor_wise_sayings = soup.find('div', attrs={'class':'text_ko'}).find('p').get_text().strip()
		kor_writer = soup.find('div', attrs={'class':'text_ko'}).find('p', attrs={'class':'writer'}).get_text().strip()
		print('-' *150)
		print('[오늘의 한줄명언]')
		print(f'{eng_wise_sayings}')
		print(f'- {eng_writer} -')
		print(f'{kor_wise_sayings}')
		print(f'- {kor_writer} -')