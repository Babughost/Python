# % 연산자

name = 'Kai'
print('내 이름은 %s 입니다.' %name)
print('내 이름은 ', name, ' 입니다', sep='')
print('내 이름은 ' + name + ' 입니다')

height = 120.5
print('내 키는 %fcm 입니다.' %height)

weight = 23.55
print('내 몸무게는 %.1fkg 입니다' %weight)

year, month, day = 2014, 8, 25
print('내 생일은 %d년 %d월 %d일 입니다.'%(year, month, day))


print()


# formet 사용법

zipcode = '06236'
print('우편번호 : {}' .format(zipcode))

address = '''서울특별시 강암구
테헤란로 146'''

print('주소 : {addr}' .format( addr = address ))

tel1, tel2, tel3 = '02', '538', '0021'
print('연락처 : {0}-{1}-{2}' .format( tel1, tel2, tel3 ))
# print('연락처 : {}-{}-{}' .format( tel1, tel2, tel3))

print()