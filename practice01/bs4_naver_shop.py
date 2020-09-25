# scraping default
import requests
import re
from bs4 import BeautifulSoup

url = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex=1&pagingSize=80&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=rel&timestamp=&viewType=list'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all('div', attrs={'class', re.compile('^basicList_title')})
print(items[0].find('a', attrs={'class', re.compile('^basicList_link')}).get_text())