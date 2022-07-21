# 반환값
# 함수 호출 결과를 반환값(return value)
# 반환값이 있으면 함수 내부에서 return 문을 통해 값을 반환 할 수 있고,
# 반환값이 없으면 함수 내부에 return문을 작성할 필요가 없슴



# 1. 반환값이 있는 함수

def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

print(address())




# 2. 다중 반환
# 하나의 반환값도 처리 할 수 있고 여러 개의 반환값도 처리 할 수 있음

print()
def calculator(*args):
    return sum(args), sum(args)/len(args), max(args), min(args)

a, b, c, d = calculator(1,2,3,4,5)
# a = sum(args)                 에 반환값을 받음
# b = sum(args)/len(args)       에 반환값을 받음
# c = max(args)                 에 반환값을 받음
# d = min(args)                 에 반환값을 받음

print('합계',a)         # 합계 15
print('평균',b)         # 평균 3.0
print('최댓값',c)       # 최댓값 5
print('최솟값',d)       # 최솟값 1

print()

result = calculator(1,2,3,4,5)
print('합계',result[0])         # 합계 15
print('평균',result[1])         # 평균 3.0
print('최댓값',result[2])       # 최댓값 5
print('최솟값',result[3])       # 최솟값 1





# 3. 함수의 종류를 위한 retune
# 반환값이 있으면 return문을 사용해 반환하고, 반환값이 없으면 return문을 생각하면 됨
# 반환값이 없을 때도 return문을 작성하는 경우 -> 함수를 종료 할 때

print()
def charge(energy) :
    if energy < 0 :
        print('0보다 작은 에너지는 충전 할 수 없습니다.')
        return                              # charge() 함수를 탈출 함
    print('에너지가 충전되었습니다.')

charge(1)
charge(-1)


def charge(energy) :
    if energy < 0 :
        print('0보다 작은 에너지는 충전 할 수 없습니다.')
    else : 
        print('에너지가 충전 되었습니다.')


charge(10)
charge(-10)