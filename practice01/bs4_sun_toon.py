# scraping default
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=sun'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# 제목과 링크 가져오기
cartoons = soup.find_all('td', attrs={'class':'title'})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a.get('href')
# print(title, 'https://comic.naver.com/' + link)

# result_list = []
# for cartoon in cartoons :
# 	title = cartoon.a.get_text()
# 	link = 'https://comic.naver.com/' + cartoon.a.get('href')
# 	result_list.append({'title': title, 'url': link})


# print(result_list)

# 평점 구하기
cartoons = soup.find_all('div', attrs={'class', 'rating_type'})
total_rate = 0
for cartoon in cartoons : 
	rate = cartoon.find('strong').get_text()
	print(rate)
	total_rate += float(rate)

print('총점 : ' + '%0.2f' % total_rate)
print('평균 평점 : ' + '%0.2f' % (total_rate / len(cartoons)))