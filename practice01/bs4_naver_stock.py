import csv
import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='

filename = '시가총액_1-200.csv'
f = open(filename, 'w', encoding='utf-8', newline='')
writer = csv.writer(f)

table_title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
writer.writerow(table_title)

for page in range(1, 3) : 

    res = requests.get(url + str(page), headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    data_rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')

    for data_row in data_rows :
        columns = data_row.find_all('td')
        if len(columns) <= 1 :
            continue
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)



