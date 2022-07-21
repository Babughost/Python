# 문자열 변환

# print(str(100))     # '100' / 정수 100을 문자열 '100'으로 변환
# print(str(True))    # 'True' / 논리 True를 문자열 'True'로 변환
# print(str(False))   # 'False' / 논리 False를 문자열 'False'로 변환
# print(str(3.14))    # '3.14' / 실수 3.14를 문자열 '3.14'로 변환

# 문자열 인덱스 indexing

# print()
# s = 'hello'
# print(s[0])     # h
# print(s[1])     # e
# print(s[2])     # l
# print(s[3])     # l
# print(s[4])     # o
# print('\n')
# print(s[-1])     # o
# print(s[-2])     # l
# print(s[-3])     # l
# print(s[-4])     # e
# print(s[-5])     # h


# # 마이너스(-)인덱스 문자열 뒤에서 부터 부여, 마지막 인덱스는 -1이 됨

# print(s[3] == s[-2])    # True


# 문자열 슬라이싱
# 문자열 인덱스를 활용하여 한 문자 이상으로 
# s[ start : stop : step ]
# start : 시작 인덱스를 지정, 생략하면 처음부터 추출
# stop : 종료 인덱스를 지정, 생략하면 끝까지 추출
# step : 인덱스의 증감값, 생략하면 1씩 변화

# print()
# s = 'banana'
# print(s[0:3])       #
# print(s[0:6:2])
# print()