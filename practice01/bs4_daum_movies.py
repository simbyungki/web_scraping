# scraping default
import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

for year in range(2015, 2020) :

	url = 'https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
	res = requests.get(url, headers=headers)
	res.raise_for_status()

	soup = BeautifulSoup(res.text, 'lxml')
	movie_posters = soup.find_all('img', attrs={'class': 'thumb_img'})

	for idx, movie_poster in enumerate(movie_posters) : 
		poster_img_url = movie_poster['src']
		if poster_img_url.startswith('//') :
			poster_img_url = 'https:' + poster_img_url
		
		poster_img_res = requests.get(poster_img_url)
		poster_img_res.raise_for_status()

		with open ('{0}_movie0{1}.jpg'.format(year, idx +1), 'wb') as f : 
			f.write(poster_img_res.content)

		if idx >= 4 :
			break