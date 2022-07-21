# # P.29

# '''
# 파일명: Ex02-1.py
# 개요 : 반지름을 전달하면 원의 넓이를 반환하는 get_area() 함수
# 작성자 : 홍길동
# 최초작성일 : 2020-08-25
# '''


# # math 모듈 포함
# import math

# # get_area() 함수 정의
# def get_area(radius):
#     """반지름을 입력받아 원의 넓이를 반환하는 get_area() 함수"""
#     area = math.pi *math.pow(radius, 2)
#     return area

# radius = 1.5
# # get_area() 함수 호출 결과를 area 변수에 저장
# area = get_area(radius)
# print(area)
# print(get_area.__doc__)



# # P.32

# name = 'Alice'
# age = 25
# address = '''우편번호 12345
# 서울시 영등포구 여의도동
# 서울빌딩 501호'''
# boyfriend = None
# height = 168.5

# print(f'이름은 {name} 입니다')
# print(f'나이는 {age} 세 입니다')
# print(f'제 주소는 {address} 입니다')
# print(f'만나는 남자친구는 {boyfriend}')
# print(f'제 키는 {height}cm 입니다.')

# # p.49

# # 1번 문제
# # 5자리로 구성된 학번 '31025'를 학년, 반, 번호로 나누어 출력하는 프로그램
# stu_num = '31025'
# print(f'{stu_num[0:1]}학년 {stu_num[1:3]}반 {stu_num[3:5]}번')


# # 2번 문제
# 전체 차량번호에서 뒤에 숫자 4자리만 추력하는 프로그램을 구현하세요
# 전체 차량번호는 '서울2가1234', '10가1234', '288가1234' 입니다
# 모두 차량번호 4자리는 '1234' 입니다

# car_no = '서울2가1234'
# print(f'{car_no}의 차량번호 4자리는 {car_no[-4:]} 입니다.')


# # 3번 문제
# 문자열 s에 'maple'이 저장되어 있습니다. 문자열 s의 가운데 글자를 출력하는
# 프로그램을 구현하세요.

# s = 'maple'
# print(f'{s}의 가운데 글자는 {s[2]} 입니다.')


# # 4번 문제
# 리스트 [10,20,30,40,50,60,70,80,90,100]의 3번째 요소부터 7번째 요소만
# 추출한 결과 리스트에서 2번째 요소를 출력하는 프로그램을 구현

# li = [10,20,30,40,50,60,70,80,90,100]
# li_cut = li[2:7:1]

# print(f'3번째 요소부터 7번째 요소 = {li_cut}')
# print(f'3번째 요소부터 7번째 요소 중 2번째 요소 = {li_cut[1]}')


# # 5번 문제
# 금요일은 탕수육, 토요일은 유산슬, 일요일은 팔보채, 할인을 출력

# dis_menu = {'금요일':'탕수육','토요일':'유산슬','일요일':'팔보채'}
# print(f'금요일 : {dis_menu["금요일"]}')
# print(f'토요일 : {dis_menu["토요일"]}')
# print(f'일요일 : {dis_menu["일요일"]}')


# # p.53

# print('Hello \'world\'')
# print("Hello \"World\"")
# print('*\n**\n***')
# print('이름\t연락처')
# print('제시카\t02-123-4567')
# print('마틴\t010-8765-1234')



# # p.55

# print('재미있는','파이썬')
# print('python','java','C',sep=",")

# print()

# print('영화 타이타닉')
# print('평점',end=':')
# print('5점')



# # p.58

# name = 'Kai'
# print('내 이름은 %s 입니다.' %name)
# print(f'내 이름은 {name} 입니다.')

# height = 120.5
# print('내 키는 %fcm 입니다.' %height)
# print(f'내 키는 {height}cm 입니다.')

# weight = 23.55
# print('내 몸무게는 %.1fkg 입니다.' %weight)
# print(f'내 몸무게는 {weight}kg 입니다.')

# year, month, day = 2014, 8, 25
# print('내 생일은 %d년 %d월 %d일 입니다.' %(year,month,day))
# print(f'내 생일은 {year}년 {month}월 {day}일 입니다.')



# # p.60
# zipcode = '06236'
# print('우편번호 : {}'.format(zipcode))
# print(f'우편번호 : {zipcode}')


# address = '''서울특별시 강남구
# 테헤란로 146'''
# print('주소 : {addr}'.format(addr=address))
# print(f'주소 : {address}')


# tel1, tel2, tel3 = '02', '538', '0021'
# print('연락처 : {0}-{1}-{2}'.format(tel1,tel2,tel3))
# print('연락처 : {}-{}-{}'.format(tel1,tel2,tel3))
# print(f'연락처 : {tel1}-{tel2}-{tel3}')



# # p.63

# name = input('이름을 입력하세요 >>> ')
# age = input('나이를 입력하세요 >>> ')
# print('입력된 이름은 {} 입니다'.format(name))
# print('입력된 나이는 {} 입니다'.format(age))
# print()
# print(f'입력된 이름은 {name} 입니다')
# print(f'입력된 나이는 {age} 입니다')


# # p.65

# price = 50000
# n = int(input('할부 개월 입력 >>> '))
# print('매달 내는 돈은 {}원 입니다.'.format(price/n))
# print(f'매월 내는 돈은 {price/n}원 입니다.')



# # p.66
# # 문제 1번
# num1 = float(input('첫 번째 실수를 입력하세요 >>> '))
# num2 = float(input('두 번째 실수를 입력하세요 >>> '))

# print(f'{num1}와 {num2}의 합은 {num1+num2} 입니다.')



# # 문제 2번

# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month = int(input('1~12 사이의 월을 입력하세요 >>> '))

# print(f'{month}월은 {days[month-1]}일까지 있습니다')



# # 문제 3번

# english_dict = {'flower':'꽃', 'fly':'날다', 'floor':'바닥'}

# word = str(input('영어 단어를 입력하세요 >>> '))

# print(f'{word} : {english_dict[word]}')



# # 문제 4번

# math_trip = set()    # 빈 set 변수 선언시 무조건 set()로 선언!
#                      # 아니면 null 값이 생성됨
# math_trip.add(str(input('희망하는 수학여행지를 입력하세요 >>> ')))
# math_trip.add(str(input('희망하는 수학여행지를 입력하세요 >>> ')))
# math_trip.add(str(input('희망하는 수학여행지를 입력하세요 >>> ')))

# print(f'조사된 수학여행지는 {math_trip} 입니다.')


# # P.85
# 문제 1번
# num1 = int(input('10~99 사이의 정수를 입력하세요 >>> '))
# print(f'십의 자리 : {num1//10}')
# print(f'일의 자리 : {num1%10}')