# fruits = ['사과', '감귤']
# count = 3               # 입력 가능한 횟수

# while count > 0 :
#     fruit = input('어떤 과일을 저장 할까요? >>> ')
#     if fruit in fruits :                   # 리스트에 중복 값이 있는지 확인
#         print('동일한 과일이 있습니다.')
#         continue        # while문의 시작 지점으로 돌아가서 다시 과일 이름을 입력
#     fruits.append(fruit)    # 입력된 과일 이름을 리스트에 저장
#     count -= 1              # 입력 가능 횟수가 줄어듬
#     print(f'입력이 {count}번 남았습니다')

# print(f'5개 과일은 {fruits} 입니다.')



# #-------------------

# 0이하의 값이 입력되면 사용자에게 재입력을 요구

# count = 0
# total = 0         # 연산에 이용이 되기 때문에 0으로 초기화
# while count < 5 :
#     n = int(input(f'{count+1}번째 정수를 입력하세요 >>>>'))
#     if n <= 0 :
#         print('0 이하의 정수는 처리 할 수 없습니다.')
#         continue  # 반복문의 이하 명령문은 실행이 되지 않음
#     total += n
#     count += 1
# print(f'입력된 5개의 양수의 총 합은 {total} 입니다.')


# # p.141 응용예제
## 1번


# total = 10000

# print(f'현재 {total}이 있습니다')

# while total >= 0 :
#     coin = int(input(f'사용할 금액 입력 >>> '))
#     if coin > total :
#         print(f'{coin-total}원이 부족합니다.')
#     elif coin < 0 :
#         print('0이하의 금액은 사용 할 수 없습니다.')
#     else :
#         total -= coin
        
# print(f'현재 {total}이 있습니다.')

# 강사님 풀이 1)

# money = 10000
# while True :
#     print(f'현재 {money}원이 있습니다.')
#     if money == 0 :
#         break
#     spend = int(input('사용할 금액 입력 >>> '))
#     if spend <= 0 :
#         print('0이하의 금액은 사용 할 수 없습니다.')
#     elif spend > money :
#         print(f'{spend-money}원이 부족합니다.')
#     else:
#         money -= spend


# 강사님 풀이 2)

# money = 10000
# while money != 0 :
#     print(f'현재 {money}원이 있습니다.')
#     use_money = int(input('사용할 금액 입력 >>>> '))
#     if (use_money <= 0) :
#         print('0이하의 금액은 사용 할 수 없습니다')
#         continue
#     if (use_money > money) :
#         print(f'{use_money-money}원이 부족합니다.')
#         continue
#     money -= use_money
# print('현재 0원이 있습니다.')



## 2번

# rate = int(input('이번 영화의 평점을 입력하세요 >>> '))

# while True :
#     if rate >= 1 or rate <= 5 :
#         break
#     else :
#         print('평점을 1~5 사이만 입력할 수 있습니다.')

# print(f'평점 : ('*' * {rate})' )


# 강사님 풀이

# while True :
#     score = int(input('이번 영화의 평점을 입력하세요 >>>>'))
#     if score < 1 or score > 5 :
#         print('평점은 1~5 사이만 입력 할 수 있습니다.')
#     else : 
#         print("평범 : " + ("*" * score))
#         break




## 3번


# password = ['qwerty']
# count = 5               

# while count > 0 :
#     word = input('비밀번호를 입력하세요 >>> ')
#     if word in password :                   
#         print('비밀번호를 맞혔습니다')
#         break       
#     elif count > 0 :
#         count -= 1
#         continue              
   
# print(f'비밀번호 입력 횟수를 초과 했습니다.')


## 강사님 풀이 1)

# answer = 'qwerty'
# count = 0 
# while True :
#     if count == 5 :
#         print('비밀번호 입력 횟수를 초과했습니다.')
#         break
#     pw = input('비밀번호를 입력하세요 >>> ')
#     if pw == answer :
#         print('비밀번호를 맞혔습니다.')
#         break
#     count += 1


## 강사님 풀이 2)

# pass_str = 'qwerty'
# cnt = 5

# for i in range(cnt) : 
#     try_pass = input('비밀번호를 입력하세요 >>> ')
#     if pass_str == try_pass :
#         print('비밀번호를 맞혔습니다.')
#         break

#     elif i + 1 == cnt :
#         print('비밀번호 입력 횟수를 초과했습니다.')

