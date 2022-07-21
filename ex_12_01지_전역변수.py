# 지역변수와 전역변수

# 1. 지역번수 local variable
# 함수 내부에서 선언한 변수는 함수 내부에서만 사용. 함수 외부에서는 지역변수에 접근 할수 없음

def f() :
    a = 10
    print(f'f() 내부 : {a}')

f()             # f() 내부 : 10

#print(f'f() soqn : {a}') # 함수 외부에서는 a 변수를 사용 할 수 없슴

# 2. 전역변소 global variable
# 함수 외부에서 선언한 변수는 함수 내부나 함수 외부에서 모두 사용 할 수 있음

print()
def f() :
    print(f'f() 내부 : {b}')
b = 10

f()             # f() 내부 : 10
print(f'f() 내부 : {b}')    # f() 내부 : 10


# 1) 전역 변수 를 단순히 참조만 하는 경우

print()
a = 0
def f() : 
    print(a)
f()
print(a)


# 2) 전역 번수의 값을 변경하는 경우

print()
a = 0
def f() :
    global a            # 전역변수 a를 사용
    a = 10              # 전역변수 a의 값을 변경
f()
print(a)                # 10 / 전역변수의 변경되 값을 확인


# 3) global을 사용 하지 않으면

print()
a = 0
def f() :
    a = 10              # 지역변수 a를 선언 후 초기화
f()
print(a)                # 0 / 지역변수a의 값에는 영향이 없음



