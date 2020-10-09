# 출력 예시
# [오늘의 풍무동 날씨]
# 흐림, 어제보다 00˚ 높아요
# 현재 00˚ (최저 00˚ / 최고 00˚)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 24㎍/㎥ 좋음
# 초미세먼지 16㎍/㎥ 보통

# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
#   (링크 : https://...)
# 2. 무슨 무슨 일이...
#   (링크 : https://...)

# [IT 뉴스]
# 1. 무슨 무슨 일이...
#   (링크 : https://...)
# 2. 무슨 무슨 일이...
#   (링크 : https://...)

# [오늘의 한줄 명언]
# eng) ....
# kor) ....


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
	# 날씨정보
	if url == url_wether :
		w_infos01 = soup.find_all('div', attrs={'class': 'main_info'})
		summary = w_infos01[0].find('p', attrs={'class': 'cast_txt'}).get_text()
		temp01 = w_infos01[0].find('span', attrs={'class': 'todaytemp'}).get_text()
		temp02 = w_infos01[0].find('span', attrs={'class': 'min'}).find('span', attrs={'class': 'num'}).get_text()
		temp03 = w_infos01[0].find('span', attrs={'class': 'max'}).find('span', attrs={'class': 'num'}).get_text()
		w_info02 = soup.find('div', attrs={'class': 'sub_info'})
		dust01 = w_info02.find('dl', attrs={'class': 'indicator'}).find_all('dd', attrs={'class':'lv1'})[0].get_text()
		dust02 = w_info02.find('dl', attrs={'class': 'indicator'}).find_all('dd', attrs={'class':'lv1'})[1].get_text()

		print('[오늘의 풍무동 날씨]')
		print(summary)
		print(f'현재 {temp01}˚ (최저 {temp02}˚ / 최고 {temp03}˚)')
		#print(f'오전 강수확률 00% / 오후 강수확률 00%')
		print(f'미세먼지 {dust01}')
		print(f'초미세먼지 {dust02}')

	elif url == url_headline_news :

		
# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
#   (링크 : https://...)
# 2. 무슨 무슨 일이...
#   (링크 : https://...)
	elif url == url_it_news :
		print(33)
	else : 
		print(44)



