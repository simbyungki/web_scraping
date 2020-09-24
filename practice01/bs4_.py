import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a.get('onclick'))

# print(soup.find('a', attrs={'class': 'Nbtn_upload'}))
# print(soup.find(attrs={'class': 'Nbtn_upload'}))
# print(soup.find('li', attrs={'class', 'rank01'}))
# rank01 = soup.find('li', attrs={'class', 'rank01'})
# print(rank01.a.get('href'))
# print(rank01.a.get_text())
# rank02 = rank01.next_sibling.next_sibling
# or
# rank02 = rank01.find_next_sibling()
# rank03 = rank02.next_sibling.next_sibling
# # print(rank03.a.get_text())
# rank02 = rank03.previous_sibling.previous_sibling
# print(rank03.a.get_text())
# print(rank01.parent)
# rank02 = rank01.find_next_sibling('li')
# print(rank02.a.get_text())
# number = 1
# for li in rank01.find_next_siblings('li') :
# 	print('{0} : {1}'.format(number, li.a.get_text()))
# 	number += 1

webtoon = soup.find('a', text='남주의 첫날밤을 가져버렸다-12화')
print(webtoon)



# with open('./practice01/naver_webtoon.html', 'w', encoding='utf8') as f :
# 	f.write(res.text)