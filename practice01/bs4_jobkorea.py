import requests
from bs4 import BeautifulSoup

job_name = '웹퍼블리셔'
url = 'http://www.jobkorea.co.kr/Search/?stext='+ 'EC%9B%B9%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%85%94' +'&tabType=recruit&Page_No=1'
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, 'lxml')

# 해당지역 단지 목록 가져오기
job_list = soup.select('.recruit-info .list-default li.list-post .title')


for job in job_list :
	print(job)
	print('*'*100)

