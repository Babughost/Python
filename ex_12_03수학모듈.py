# 표준 모듈의 활용
# 파이썬에 기본적으로 설치되어 있는 모듈을 의미
# 표준 모듈들을 별도로 설치하지 않고 import 후 바로 사용 가능

# 1. 수학 모듈 math

import math

# ceil() 함수와 floor() 함수
# 전달된 값을 정수로 올림 처리하거나 내림 처리
print(math.ceil(1.1))       # 2 / 정수로 올림 처리
print(math.floor(1.9))      # 1 / 정수로 내림 처리


# trunc() 함수
# 전달된 값을 정수로 절사
# 양수를 처리할 때는 차이가 없지만, 음수를 처리할 때는 겨로가의 차이가 있음

print(math.trunc(-1.9))     # -1 / 절사이므로 소수점 이하를 잘라버림
print(math.floor(-1.9))     # -2 / 내림이므로 -1.9 보다 작은 정수로 내림


