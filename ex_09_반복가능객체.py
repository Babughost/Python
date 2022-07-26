
# # 반복가능객체
# # 1. 시퀀스 자료형 : 순서를 가지고 있는 자료형
# #   문자열, 리스트, 튜플, range
# # 2. 비시퀀스 자료형 : 순서를 가지고 있지 않은 자료형
# #   세트, 딕셔너리


# # 1. 문자열
# # for 문자 in 문자열 :
# #   반복실행문

# for ch in 'hello' :
#     print(f'{ch}')

# # 2. 리스트
# # for 요소 in [리스트] :
# #   반복실행문

# for item in ['가위', '바위', '보'] :
#     print(f'{item}')


# # 리스트 내포
# # 리스트 생성할 때 for문을 유용하게 사용할 수 있음
# # 기본형식
# # 리스트 = [ n *2 for n in [1, 2, 3,] ]

# li = [n*2 for n in [1,2,3,]]
# print(f'{li}')


# # 조건에 맞는 데이터만 추출 가능
# # 리스트 = [ 표현식 for 변수 in 반복가능객체 if 조건식 ]

# li = [ n*2 for n in [1,2,3,4,5] ]
# print(li)

# li = [ n*2 for n in [1,2,3,4,5] if n % 2 == 1 ]
# print(li)




# # 3. 튜플
# # 기본 형식 
# # for 요소 in (튜플) :
# #   반복실행문

# # 예제 p.122 하단




# # 4. range() 함수
# # 정수 범위를 만들어 낼때 유용한 함수
# # 기본 구조
# # range(초기값, 종료값, 증감값)

# # 특징
# # 1. 초깃값부터 종료값 이전까지 숫자(n)들의 컬렉션을 만듬(초깃값 <= n < 종료값)
# # 2. 초깃값을 생략하면 0부터 시작
# # 3. 종료값은 생략 할 수 없음
# # 4. 증감값을 생략하면 1씩 증가

# # 예
# # range(5) : 0, 1, 2, 3, 4                      # range(5) == range(0, '5', 1)과 같음
# # range(1, 11) : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# # range(1, 10, 2) : 1, 3, 5, 7, 9

# print()
# print(list(range(1,6)))
# print(tuple(range(1,6)))

# print()

# for n in [1,2,3,4,5,6,7,8,9,10] :
#     print(n)


# # 아래와같이 변경 가능
# for n in range(1,11) :
#     print(n)


# # range() 함수를 이용해 생성한 값을 사용하지 않는 경우
# for n in range(10) :
#     print('Hello')

# ---------- 08_반복가능객체 내용 끝 --------------- #



# 1. 셋트 set
# 비시퀀스 자료형이기 때문에 저장된 요소들 사이에 순서가 겂음

# 기본 형식
# for 요소 in {세트} :
#   반복 실행문

for item in {'가위', '바위', '보'} :        # 순서가 지켜지지 않음
# for item in ['가위', '바위', '보'] :      # 순서가 지켜짐
    print(item)


# 2. 딕셔너리
# key와 value의 조합이라 다른 자료형과 다른 방식으로 사용을 함
# 키만 출력

print()
person = { 'name' : '에밀리', 'age' : 20 }
for item in person : 
    print(item)     # name age

print()

# value 출력
for key in person :
    print(person[key])  # 에밀리 20 => 주로 사용

print()

for key in person : # get() 메소드를 이용해서 해당 key에 해당하는 value를 가져옴
    print(person.get(key)) # 에밀리 20 => 이렇게 사용하는 경우도 있다


# 영어 사전을 딕셔너리 자료형으로 구현하고
# 연어 사전에 등록된 모든 단어와 그 단어의 의미를 출력

eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'

}

for word in eng_dict :
    print(f'{word} 의 뜻 : {eng_dict.get(key)}')
    print(f'{word} 의 뜻 : {eng_dict[word]}')