# 대입 연산자

from re import A


c = 100

a, b = 10, 20
print('a = %d, b = %d' % (a, b))

a, b = b, a
print('a = %d, b = %d' % (a, b))

# P .75 실습하기

c = int(10)
d = int(20)
temp = int(0) 

print(f'c는 {c}, d는 {d}')

temp = c
c = d
d = temp

print(f'c는 {c}, d는 {d}')