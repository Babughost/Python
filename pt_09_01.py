# p.129

#### 1.1부터 5사이에 존재하는 모든 정수를 역순으로 출력

# for n in range(5,0,-1) :
#     print(n)


#### 2.임의의 양의 정수를 하나 입력 받은 뒤 1부터 입력받은 정수까지 모든 정수의 합계를 출력

sum = 0
num = int(input('임의의 양수를 입력하세요 >>>> '))
for n in range(1,num+1) :
    print(n)
    sum += n
    n += 1
print(f'1 부터 {num}까지 모든 정수의 합계는 {sum} 입니다.')

# # 강사님 풀이

# total = 0
# end = int(input('임의의 양수를 입력하세요 >>>'))
# for n in range(1,end+1):
#     total += n
# print(f'1부터 {end}사이 모든 정수의 합계는 {total}입니다.')


#### 3.사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤 숫자만큼'과일 이름'을 
# 'basket' 리스트에 저장하는 프로그램을 구현하세요

# basket = []
# num = int(input('몇 개의 과일을 보관 할까요? >>> '))

# for n in range(1,num+1) :
#     basket.append(input(f'{n}번째 과일을 입력하세요 >>>' ))

# print(f'입력 받은 과일들은 {basket}입니다.')

# # 강사님 풀이

# count = int(input('몇 개의 과일을 보관 할까요? >>>'))
# basket = []
# # for n in range(count) :
# for n in range(1,count+1) :
# #    frult = input(f'{n+1}번째 과일을 입력하세요 >>> ')
#     frult = input(f'{n}번째 과일을 입력하세요 >>> ')
#     basket.append(frult)
# print(f'입력 받은 과일들은 {basket}입니다.')





#### 4. 





#### 5.
