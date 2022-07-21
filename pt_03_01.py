# 5자로 구성된 학번 '31025'를 학년, 반, 번호로 나누어 출력하는 프로그램

student = '31025'
grade_no = student[0:1]
class_no = student[1:3]
stu_no = student[3:5]   # stu_no = student[-2:] 도 가능함
# print(grade_no,'학년',class_no,'반',stu_no,'번')
print(f'{grade_no}학년 {class_no}반 {stu_no}번')


stu_num = '31025'
print(f'{stu_num[0:1]}학년 {stu_num[1:3]}반 {stu_num[3:5]}번')

# 문자    [ 3, 1, 0, 2, 5 ]
# 인덱    [ 0, 1, 2, 3, 4 ]
# 인덱    [ -5, -4, -3, -2, -1 ]
