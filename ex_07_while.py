# while 문
# 특정 조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할 때 사용
# while 조건식 :
#   반복실행문

n = 1
# if n <= 10 :
while n <= 10 :
    print(n)
    n += 1      # n = n + 1 을 단순화


n = 100
# if n <= 10 :
while n >= 50 :
    if n % 2 == 0 :
        print(n)
        n -= 1
    else :
        n -= 1      # n = n - 1 을 단순화



# while문의 중첩
# while문 내부에 또 다른 while문이 나타내는 것

day = 1

