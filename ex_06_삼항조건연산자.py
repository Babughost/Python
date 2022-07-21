# 삼항 조건 연산자
# 일반적인 삼항 조건 연산자 : 조건식 ? 참 : 거짓
# 파이썬 삼항 조건 연산자 : 참 if 조건식 else 거짓

a = 10
# a = 20
b = 20
# b = 10

result = ( a - b ) if ( a >= b ) else ( b - a )
print(f'{a}과 {b}의 차이는 {result}입니다.')

print('{}과 {}의 차이는 {}입니다.'.format(a,b,result))