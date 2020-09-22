import re

p = re.compile('ca.e')
# . ('ca.e') : 하나의 문자 > care, cafe, case (O) | caffe (X)
# ^ ('^de')  : 문자열의 시작 > desk, destination (O) | fade (X)
# $ ('de$')  : 문자열의 끝 > shade, fade (O) | desk (O)

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
