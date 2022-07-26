# 인수와 매개변수
# 함수로 전달되는 인수(argument)를 저장하는 변수를 매개변수(prameter)라고 함



# 1. 인수가 있는 함수 (기본적인 형태)

def introduce(name, age) :
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')

introduce('james',25)                   # 전통적인 방법

introduce(age=25, name='james')         # 최근 언어에서 지원 하는 방법




# 2. 가변 매개변수

# 함수로 전달해야 하는 인수의 개수가 정해지지 않아도 매개변수를 선언할 수 있음
# 가변 매개변수를 만드는 키워드는 애스터리스크(*)
# 매개변수 앞에 *를 붙이면 곧바로 가변 매개 변수가 되면서 전달되는 모든 인수를 하나의
# 튜플(tuple)로 만들어 줌

def show(*args) :
    for item in args :
        print(item)

show('Python')
show('happy','birthday')




# 3. 디폴트 매개변수
# 매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용할 수 있도록
# 매개변수에 기본값을 설정할 수 있음

print()
def greet(message = '안녕하세요.') :
    print(message)

greet('반갑습니다.')        # 반갑습니다.
greet()                     # 안녕하세요 _ 기본값으로 출력됨.


# 디폴트 매개변수가 있는 경우 뒤로 배치

def greet(name, message = '안녕하세요') :
    print(f'{name}님 {message}')

greet('김철수')


print()


def greet2(name = '이철수', message = '안녕하세요.') :
    print(f'{name}님 {message}')

greet2()
greet2('김철수')
greet2('김철수','반갑습니다.')
# 매개변수는 좌측부터 매칭을 시켜준다