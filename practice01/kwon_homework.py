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

			in_title_elem = in_soup.find('title')
			email_pattern = r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)'
			tel_num_pattern1 = r"/^\d{2,3}-\d{3,4}-\d{4}$/"
			tel_num_pattern2 = r"\d\d\d\d-\d\d\d\d"

			get_email = re.search(email_pattern, str(in_soup))
			get_tel_num1 = re.search(tel_num_pattern1, str(in_soup))
			get_tel_num2 = re.search(tel_num_pattern2, str(in_soup))

			print('ㅡ' *50)
			if get_email or get_tel_num1 or get_tel_num2 :
				print('{0} 사이트에서 정보 수집 성공!'.format(in_title_elem.get_text()))
				if get_email :
					print('이메일 주소 : {0}'.format(get_email.group()))
				if get_tel_num1 :
					print('전화번호 : {0}'.format(get_tel_num1.group()))
				if get_tel_num2 :
					print('전화번호 : {0}'.format(get_tel_num2.group()))
			else :
				print('{0} 사이트에서 정보 수집 실패!'.format(in_title_elem.get_text()))
		except :
			print('사이트 접근 오류!')