age = int(input('몇 살 입니까? >>> '))  # int() 함수를 이용해서 정수로
if age >= 20 :
    print('성인')
else :
    print('미성년자')





# 조건문
# 1.if문
# if 조건시 :
#   조건식의 결과가 True일 때 실행문

num = 10
if num > 0:
    print('양수')

if True :
    print('양수')

if False :
    print('양수1')


# 들여쓰기 insentation 규칙
# 1. 공백(space)이나 탭(tab) 을 이용하여 들여쓰기를 수행
# 2. 공백의 개수는 상관이 없음
# 3. 탭은 1개만 사용
# 4. 동일 구역에서 들여쓰기는 통일해야 함. 공백과 탭을 혼용하여 사용 할 수 없고 들여쓰기 수준도 동일해야 함
# 5. 주로 사용하는 들여쓰기는 공백 1개, 공백 2개, 탭 1개




# 2. if-else 문
# if 조건시 :
#   조건식의 결과가 True일때 실행문
# else :
#   조건식의 결과가 False일대 실행문


print()
num = 6
if num >= 0 :
    print('양수')
else :
    print('음수')





# 3. if-elif 문
# if 조건식 1 :
#   조건식 1의 결과가 True일때 실행문
# elif 조건식 2 :
#   조건식 1의 결과가 False이고 조건식 2의 결과가 True일 때 실행문
# else :
#   조건식 1의 결과가 False이고 조건식 2의 결과가 False일 때 실행문


print()
print('성적 등급을 알려 드립니다')

important = 56
# important = int(input('성적을 입력 하세요 >>> '))
print()

if important >= 100 :
    print('상')
else :
    if important >= 50 :
        print('중')
    else :
        print('하')

print()

if important >= 100 :
    print('상')
elif important >= 50 :
    print('중')
else :
    print('하')

print()


# if문 예제


age = int(input('몇 살 입니까? >>> '))

if age <= 7 :
    print('미취학')
elif age <= 13 :
    print('초등학생')
elif age <= 16 :
    print('중학생')
elif age <= 19 :
    print('고등학생')
else :
    print('성인')








