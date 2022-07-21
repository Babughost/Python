
# 문자열 슬라이싱
# 문자열 인덱스를 활용하여 한 문자 이상으로 
# s [ start : stop : step ]
# start : 시작 인덱스를 지정, 생략하면 처음부터 추출
# stop : 종료 인덱스를 지정, 생략하면 끝까지 추출
# step : 인덱스의 증감값, 생략하면 1씩 변화

print()
s = 'banana'
print(s[0:3])       # ban / 종료 인덱스는 포함(출력)하지 않음
print(s[0:6:2])     # bnn
print(type(s))      # <class 'str'>

