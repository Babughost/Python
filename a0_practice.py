# #애완동물을 소개 해 주세요 ~
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = '공놀이'
# #print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))


# Quiz)변수르 이용하여 다음 문장을 출력하시오

# 내 답
# station = "사당"

# print ( station,"행 열차가 들어오고 있습니다." )

# station = "신도림"
# print ( station,"행 열차가 들어오고 있습니다." )

# station = "인천공항"
# print ( station,"행 열차가 들어오고 있습니다." )


# 풀이
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3)
# print(5%3)
# print(10%3)
# print(5//3)
# print(10//3)

# print( 10 > 3 )
# print( 4 >= 7 )
# print( 10 < 3 )
# print(5 <= 5)

# print(3 == 3)
# print(4 == 2)
# print(3+4 == 7)

# print(1 != 3)
# print(not(1 != 3))

# print((3>0)and(3<5))
# print((3 > 0) & (3<5))

# print((3>0)or(3>5))
# print((3>0) | (3>5))

# print(5>4>3)
# print(5>4>7)

# print(2 + 3 * 4)
# print((2 + 3)*4)
# number = 2+3*4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)
# number %= 2
# print(number)

# print(abs(-5))
# print(pow(4, 2))
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14))
# print(round(4.99))

# from math import *
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))


# from random import *

# print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10)
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10)+1)
# print(int(random() * 10)+1)
# print(int(random() * 10)+1)
# print(int(random() * 10)+1)
# print(int(random() * 10)+1)
# print(int(random() * 10)+1)

# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))

# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성


# Quiz 2) 
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1: 랜덤으로 날짜를 뽑아야 함
# 조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정 되었습니다.

# from random import *

# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정")


# sentence = '나는 소년입니니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)


# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #필요 정보 직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6]) #처음부터 6 직전까지

# print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지 

# print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])