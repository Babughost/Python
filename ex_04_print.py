# print() 함수
# end : value 출력 후 출력할 문자
# end 속성을 사용하지 않고 print()함수를 사용하면 출력 후 자종으로 줄 바꿈
# sep : 출력할 value의 구분자
# sep 속성을 사용하지 않고 print()함수를 사용하면 출력 대상은 공백으로 구분
# file : 출력 방향 지정
# file 속성을 사용하지 않고 print()함수를 사용하면 출력 대상은 모니터에 출력

print('재미있는','파이썬')              # 재미있는 파이썬
print('Python','Java','C', sep=':')     # Python:Java:C

print()
print('영화 타이타닉')                  
print('평점',end=':')                   
print('5점')            # 평점:5점 / value 출력 후 end 속성

# fos = open('sample.py',mode='wt')
# print('print("Hello World")',file=fos)
# 