def coffee_machine(money, pick) : 
    print(f'\n{money}원에 {pick}를 선택하셨습니다.')
    # 커피와 가격을 하나의 테이터로 처리하기 위해 딕셔너리 dict를 사용

    menu = {
        '아메리카노' : 1000,
        '카페라떼' : 1500,
        '카푸치노' : 2000
    }
    if pick not in menu : # 없는 커피는 주문하는 경우
        print(f'\n{pick}는 판매하지 않습니다.')
        return money, '없는 메뉴'
        # 입력한 금액을 반환, pick -> 입력메뉴 -> '없는 메뉴' 으로 반환

    elif menu[pick] > money : # 구매할 금액이 부족한 경우
        print(f'\n{pick}는{menu[pick]}원 입니다.')
        return money, '금액 부족'
        # 입력한 금액을 반환, pick -> 입력메뉴 -> '금액 부족' 으로 반환

    else : # 정상 주문이면 잔돈과 선택한 커피를 반환
        return money - menu[pick], pick
        # 입력한 금액 - 메뉴 금액을 반환, pick -> 입력메뉴 반환


    # 1) 선택한 커피가 메뉴 안에 있는지 확인 
    # 2) 제출한 금액이 커피 값 보다 큰지 확인
    # 3) 선택한 커피가 메뉴에 있고 제출한 금액이 커피 값보다 크면 처리 후 반환


order = input('\n커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노) >>> ')
pay = int(input('\n얼마를 내시나요? >>>> '))

change, coffee = coffee_machine(pay, order)
print(f'\n잔돈 {change}원, 커피 : {coffee}\n')

# 커피 입력 -> order -> coffee_machine(order) -> def coffee_machine(pick) -> coffee 로 반환
# 금액 입력 -> pay -> coffee_machine(pay) -> def coffee_machine(money) -> change 로 반환