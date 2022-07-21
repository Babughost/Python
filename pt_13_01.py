import random

dice = random.randint(1,6)
print(dice)

while True :
    user = int(input('주사위 값은 얼마 일까요? >> '))
    if dice == user :
        print(f'{dice}! 정답입니다.')
        break
    
    # else:
    #     print('오답입니다. 다시 선택하세요')

    elif dice < user :
        print('오답입니다. 낮을 숫자를 선택하세요')
    else :
        print('오답입니다. 높은 숫자를 선택하세요')
    # 조건문은 최대한 수를 줄여야된다... 