

# n = 100
# # if n <= 10 :
# while n >= 50 :
#     if n % 2 == 0 :
#         print(n)
#         n -= 1
#     else :
#         n -= 1      # n = n - 1 을 단순화



# # # 강사님 풀이.... 동작의 단순화 된 코드
# n = 100
# while n >= 50 :
#     print(n)
#     n -= 2 # n = n - 2



# my_list = []

# n = int(input('정수를 입력하세요 (종료는 0 입니다.) >>>>> ')) # 한번만 실행

# while n != 0 : # n이 0 이 아니면 계속 실행
#     my_list.append(n)
#     n = int(input('정수를 입력하세요 (종료는 0 입니다.) >>>>> '))

# print(my_list)




# # # while문의 중첩
# # # while문 내부에 또 다른 while문이 나타내는 것

day = 1

while day <= 5 :
    hour = 1
    while hour <= 3 :
        print(f'{day}일차 {hour}교시 입니다.')
        # print(f'{day} X {hour} = {day*hour}')
        hour += 1
    # print('-'*15)
    day += 1





# # # 구구단 2단 부터 9단 까지 출력
# # # 단 사이에 구분선을 넣어 볼 것

dan = 2
while dan <= 9 :
    n = 1
    while n <= 9 :
        print(f'{dan} X {n} = {dan*n}')
        n += 1
    print('=' * 15)
    dan += 1


# a = int(2)
# b = float(1.8)
# c = float(2.5)
# d = '3.9'
# print(type(d))

# flo_sum = int(b+c)
# print(type(flo_sum))

# d_ex1 = float(d)
# d_int = int(d_ex1)
# print(type(d_int))

# print(f'{flo_sum + a + d_int}')