# break 문
# while문이나 for문과 같은 반복문을 강제로 종료하고자 할 대 사용 하는 제어문
# 반목문 내에 break문이 나타나면 곧바로 break문이 포함된 반복문은 종료


# n = 1
# while n <= 10 :
#     print(n)
#     n += 1
# print(f'종료 되는 n의 값은 {n} 입니다.')            # n = 11               


# print()


# n = 1
# while True :
#     print(n)
#     if n == 10 :
#         break       # if문에서 break문을 작성 했지만 실제로 종료되는 것은 while문
#     n += 1
# print(f'종료 되는 n의 값은 {n} 입니다.')            # n = 10


# break문 사용 예 1

# while True :            # 무한 루프
#     city = input('대한민국의 수도는 어디인가요? >>> ')
#     city = city.strip()
#     if city == '서울' or city == 'seoul' or city == 'SEOUL' or city == 'Seoul' : 
#         print('정답입니다.')
#         break           # 정답을 맞춰야 종료
#     else :
#         print('오답입니다. 다시 시도하세요.')


# break문 사용 예 2

# hobbies = []
# while True :
#     hobby = input('취미를 입력하세요(종료는 그냥 Q) >> ')
#     if hobby == 'Q':
#         print('입력된 취미가 모두 저장되었습니다.')
#         break
#     else:
#         hobbies.append(hobby)
# print(hobbies)


# break문 없이 코딩 해보기

# hobbies = []
# hobbiy = None
# while hobbiy != 'Q' :
#     hobby = input('취미를 입력하세요(종료는 그냥 Q) >> ')
#     hobbies.append(hobby) if hobbiy != 'Q' else print('입력된 취미가 모두 저장되었습니다.')
# print(hobbies)
