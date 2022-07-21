file = open('input/엄마돼지아기돼지.txt','rt')

line_list = file.readlines()
print(line_list)
count = 0
for line in line_list :
    for ch in line :
        # print(ch)
        if ch == '꿀' :
            count += 1

print(f'꿀은 전체 {count}번 나타납니다.')