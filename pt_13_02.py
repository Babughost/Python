# # p.222 응용 예제

# import random
# import time
# from datetime import*


# print('\nUpDown 게임을 시작 합니다.')

# start = datetime.now()             

# num = random.randrange(1,101)
# print(num)

# while True :
#     user = int(input('어떤 값일 까요? >> '))
#     if num == user :
#         print(f'{num}! 정답입니다.')
#         break
#     elif num < user :
#         print('오답입니다. 낮을 숫자를 선택하세요')
#     else :
#         print('오답입니다. 높은 숫자를 선택하세요')



# end = datetime.now() 
# elapse = end - start
# elapse = elapse.total_seconds()   

# print(f'총 {elapse}초가 소요 되었습니다.')



## 사진 보고 강사님 풀이 입력하기

import random
import time
import math

answer = random.randint(1, 100)

print('UpDown게임을 시작합니다.')

start = time.time()

print(answer)

while True :
    n = int(input('어떤 값일까요? >>> '))
    if answer == n :
        print('정답입니다.')
        break
    elif answer < n :
        print('Down')
    else :
        print('Up')

end = time.time()

elapse = end - start
print(f'{math.floor(elapse)}초 만에 성공했습니다.')






# # p.221 예제 숙제










