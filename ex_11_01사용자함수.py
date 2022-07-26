# 사용자 함수
# 사용자가 직접 만든 함수
# 어떤 입력을 받아 특정 연산을 수행한 뒤 결과를 반환하는 기능


# 함수 용어 정리
# 1. 함수 정의 : 사용자가 함수를 새로 만드는 것을 의미
# 2. 인수 : 사용자 함수에 전달할 입력(input)을 의미. argument
# 3. 매개변수 : 인수를 받아서 저장하는 변수를 의미. parameter
# 4. 반환값 : 사용자 함수의 출력(output)을 의미. return
# 5. 함수 호출 : 만들어진 사용자 함수를 실제로 사용하는 것을 의미


# 함수 정의
# 함수를 만드는 것을 의미. def 키워드를 이용

# def 함수이름(매개변수) :
#   본문
#   retune 반환값

# 함수이름을 개발자가 마음대로 결정
# 매개변수, 반환값을 필수 사항이 아님


# 함수 호출
# 변수 = 함수이름(인수)
# 함수의 호출 결과를 저장할 변수를 생략가능


# 4가지 함수 호출 형태

# 1) 인수 : x, 반환값 : x
# 함수이름()

# 2) 인수 : o, 반환값 : x
# 함수이름(인수)

# 3) 인수 : x, 반환값 : o
# 변수 = 함수이름()

# 4) 인수 : o, 반환값 : o
# 변수 = 함수이름(인수)




# # 함수는 선언 후에 코딩 작성

# welcome() 함수 정의

def welcome() :
    print('Hello Python')
    print('Nice to meet you')

welcome()







