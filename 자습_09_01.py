# 내장 함수
# 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수가 내장되어 있으며,
# 이를 내장 함수 built-in function 이라고 함
# 외부에 따로 저장해 둔 모듈에서 불러오는 것이 아니기 때문에 import가 필요없음

# 1. 문자열 내장 함수
# chr() : 특정 문자의 유니코드 값을 전달하면 해당 유니코드 값을 가진 문자를 반환하는 함수
# 유니코드의 유효범위 0~1, 114, 111 / 아스키코드의 유효 범위 0 ~ 127

print(chr(48))  # 0
print(chr(49))  # 1
print(chr(65))  # A
print(chr(66))  # B
print(chr(97))  # a
print(chr(98))  # b


# ord() : 문자를 전달하면 해당 문자의 유니코드 값을 반환

print()
print(ord('A'))     # 65
print(ord('한'))    # 54620


# eval() : 실행하고자 하는 표현식(expression) 을 문자열로 전달하면 표현식의 결과값을 반환
print()
print(eval('100 + 200'))    # 300
a = 10
print(eval('a * 5'))        # 50
print(eval('min(1,2,3)'))   # 1


# format : 전달받은 인수와 포멧 코드에 따라 형식을 갖춘 문자열을 반환
# 포멧 코드를 전달하지 않으면 str()을 호출한 것과 같음
print()
print(format(10000))        # 10000
print(format(10000,'_'))    # 10_000
print(format(10000,','))    # 10,000

