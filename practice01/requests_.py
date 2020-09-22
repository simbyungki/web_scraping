import requests
res = requests.get('https://google.com')

# 접속 체크
# print('응답코드 : ', res.status_code)	# 200 : 정상

# if res.status_code == requests.codes.ok :
# 	print('정상')
# else :
# 	print('error :', res.status_code)

# OR

res.raise_for_status()	# 문제 발생시 프로그램 즉시 종료

print(len(res.text))
# print(res.text)

with open('./bkgoogle.html', 'w', encoding='utf8') as f : 
	f.write(res.text)