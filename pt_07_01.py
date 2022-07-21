# p.99

# # 문제 1번
# print('학점을 알려드립니다')

# score = int(input('점수를 입력하세요 >>> '))
# garde = ''

# if score >= 90 :
#     grade = 'A'
# elif score >= 80 :
#     grade = 'B'
# elif score >= 70 :
#     grade = 'C'
# elif score >= 60 :
#     grade = 'D'
# else :
#     grade = 'F'

# print(f'점수는 {score}점이고, 학점은 {grade}학점 입니다.')


# 문제 2번

num = int(input('정수를 입력하세요 >>> '))

if num % 3 == 0 :
    print(f'{num}은 3의 배수 입니다.')
else :
    print(f'{num}은 3의 배수가 아닙니다.')


# 문제 3번

num1 = int(input('정수1 입력>>>'))
num2 = int(input('정수2 입력>>>'))
num3 = int(input('정수3 입력>>>'))

max = num1
if num2 > max :
    max = num2
if num3 > max :
    max = num3

print(f'가장 큰 수는 {max} 입니다')




# 문제 4번
car_no = input('차량번호를 입력하세요 >>> ')
drive = ''

if int(car_no[-1]) % 2 == 0 :
    drive = '운행가능'
else :
    drive = '운행불가'

print(f'차량번호 {car_no}는 오늘 {drive} 입니다.')