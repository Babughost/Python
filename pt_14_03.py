file = open('input/연락처.txt','rt')
str = file.read()
num = str.count('011')
str = str.replace('011','010')
print(f'총 {num}건의 011 데이터를 찾았습니다.\n모든 데이터를 수정 했습니다.')
print(str)
file = open('./input/수정연락처.txt', 'wt')
file.write(str)
file.close()

# 깃에 붙었나요!?