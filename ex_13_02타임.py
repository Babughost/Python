# time 모듈

import time

# 1) time() 함수
# 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과된 사간 timestamp을 반환
# 소수점 이하는 마이크로 초를 의미

# print(time.time())                  # 1658292264.26822


# 2) ctime() 함수
# 인수로 전달된 시간 timestamp을 형식으로 갖춰 반환

# print(time.ctime(time.time()))      # Wed Jul 20 13:44:24 2022



# 3) strftime() 함수
# 인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘 날짜 데이터가 문자열로 반환
# 년 : %y : 2자리 날짜로 표시
# 년 : %y : 4자리 날짜로 표시
# 월 : %m : 2자리 숫자로 표시 (01 ~ 12)
# 월 : %b : 3자리 영문으로 표시 (Jan ~ Dec)
# 월 : %B : 전체 영문으로 표시 (January ~ December)
# 일 : %d : 2자리 숫자로 표시 (01 ~ 31)
# 요일 : %a : 3자리 영문으로 표시 (Sun ~ Sat)
# 요일 : %A : 전체 영문으로 표시 (Sunday ~ Saturday)
# 시 : %l : 12시간제로 표시 (01 ~ 12)
# 시 : %H : 24시간제로 표시 (01 ~ 24)
# 분 : %M : 2시간제로 표시 (00 ~ 59)
# 초 : %S : 2시간제로 표시 (00 ~ 59)
# 오전/오후 : %p : AM 또는 PM






from datetime import*

start = datetime.now()              # 계산을 시작하기 직전 시간
print(start)

total = 0

for num in range (1, 10000001) :
    total += num

end = datetime.now()                # 계산이 끝난 직후 시간

print(end)

elapse = end - start
elapse = elapse.total_seconds()     # 총 초수 반환

print(f'총 합은 {total}입니다.')
print(f'총 {elapse}초가 소요 되었습니다.')