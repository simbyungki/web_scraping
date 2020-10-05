import requests
import re
from bs4 import BeautifulSoup 

# p = re.compile('ca.e')
# . ('ca.e') : 하나의 문자 > care, cafe, case (O) | caffe (X)
# ^ ('^de')  : 문자열의 시작 > desk, destination (O) | fade (X)
# $ ('de$')  : 문자열의 끝 > shade, fade (O) | desk (X)

# 매칭
# m = p.match('cafe')
# #print(m.group())
# if m :
# 	print('매칭 : ',m.group())
# else : 
# 	print('매칭되지 않음')

def print_match(m) :
	if m :
		print('m.group() : ', m.group())
		print('m.string : ', m.string)
		print('m.start() : ', m.start())
		print('m.end() : ' , m.end())
		print('m.span() : ', m.span())
	else : 
		print('매칭되지 않음')
# match()
# m = p.match('cafe')
# m = p.match('cafeless')
# # match : 주어진 문자열의 처음부터 일치하는지 확인 > cafeless가 일치하는 이유
# print_match(m)

# search()
# m = p.search('good care')
# search : 주어진 문자열 중 일치하는게 있는지 확인
# print_match(m)

#findall()
#  l = p.findall('care carelist cafe cave ')
# findall : 일치하는 모든 것을 리스트 형태로 반환
# print(l)

# 왜 오류나지??
p = re.compile('xyz$')
m = p.match('111xyz')
# print(m.string)





headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
 
in_res = requests.get('http://www.3pl.co.kr/?n_media=122875&n_query=3PL&n_rank=1&n_ad_group=grp-a001-01-000000012855818&n_ad=nad-a001-01-000000076547024&n_keyword_id=nkw-a001-01-000002403903323&n_keyword=3PL&n_campaign_type=1&n_ad_group_type=1&NaPm=ct%3Dkfvw0qwo%7Cci%3D0A80001htBDtRSj8CLpd%7Ctr%3Dsa%7Chk%3D4ce00f13e1e80fb5d1c7e4de1c74b99b10ca7ce5#5', headers=headers)
in_res.raise_for_status()

in_soup = BeautifulSoup(in_res.text, 'lxml')

in_title_elem = in_soup.find('title')

email_pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
get_email = re.search(email_pattern, str(in_soup))
if get_email:
	print('{0}사이트에서 이메일 수집 성공! \n 이메일 주소는 : {1}'.format(in_title_elem.get_text(), get_email.group()))