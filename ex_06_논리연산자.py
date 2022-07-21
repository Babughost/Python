# 논리 연산자
# 결과 값은 True 와 False 둘 중 하나
# a and b : a와 b가 모두 참(True)이면 True, 아니면 False
# a or b : a와 b중 하나라도 참(True)이면 True, 아니면 False
# not a : a가 참(True)이면 False, a가 거짓(False)이면 True


a = 10
b = 0
print(f'{a} > 0 and {b} > 0 : { a > 0 and b > 0}')
print(f'{a} > 0 or {b} > 0 : { a > 0 or b > 0}')
print(f'not {a} : {not a}')
print(f'not {b} : {not b}')



print()
print()





print(f'{True} and {True} : { True and True }')
print(f'{True} and {False} : { True and False }')
print(f'{False} and {True} : { False and True }')
print(f'{False} and {False} : { False and False }')

print()
print(f'{True} or {True} : {True or True}')
print(f'{True} or {False} : {True or False}')
print(f'{False} or {True} : {False or True}')
print(f'{False} or {False} : {False or False}')
