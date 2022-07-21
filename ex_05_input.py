# 표준입력
# input() 함수 : 표준 입력 장치(키보드)로 부터 입력받을 때 사용

# 변수 = 형변환 ( input ('입력멘트') )


n = input('')
print(n)


n = input('정수를 입력하세요.')
print(n)
print(type(n))  # <class 'str'> / input 함수는 모든 입력을 '문자열 str'로 저장

n = int(input('정수를 입력하세요.')) # 정수로 형변환
print(type(n)) # <class 'int'>


