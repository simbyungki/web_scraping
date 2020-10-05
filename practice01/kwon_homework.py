import requests
import re
from bs4 import BeautifulSoup 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

for i in range(1, 5):
	url = 'https://ad.search.naver.com/search.naver?where=ad&sm=svc_nrs&query=3pl&referenceId=U35rudprvN8ssdjqizlsssssses-215187&pagingIndex={0}'.format(i)
	res = requests.get(url, headers=headers)
	res.raise_for_status()

	soup = BeautifulSoup(res.text, 'lxml')

	results = soup.find_all('a', attrs={'class':'lnk_tit'})
	
	for result in results : 
		try :
			in_url = result['href']
			in_res = requests.get(in_url, headers=headers)
			in_res.raise_for_status()

			in_soup = BeautifulSoup(in_res.text, 'lxml')

			email_pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
			in_title_elem = in_soup.find('title')
			get_email = re.search(email_pattern, str(in_soup))
			if get_email:
				print('{0}사이트에서 이메일 수집 성공! \n 이메일 주소는 : {1}'.format(in_title_elem.get_text(), get_email.group()))
		except :
			print('사이트 접근 오류!')