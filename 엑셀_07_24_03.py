import openpyxl

# 전체 열과 전체 행을 객체로 접근
# 열(columns), 행(rows) 객체를 튜플로 처리

file = './input/df.xlsx'    # Excel 파일 경로 지정
workbook = openpyxl.load_workbook(file)
worksheet = workbook['Sheet1']

# 시트 객체에서 columns 속성을 이용해 전체 열, rows 속성을 이용해 전체 행을 가져옴.
cols = tuple(worksheet.columns)
rows = tuple(worksheet.rows)

# 각 0번 인덱스만 출력
print(cols[0]) # <Cell 'Sheet1'.A1>, <Cell 'Sheet1'.A2>, <Cell 'Sheet1'.A3>, <Cell 'Sheet1'.A4>
print(rows[0]) # <Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>

# for문을 이용해서 모든 데이터 출력
for col_idx, col in enumerate(cols) :
    for each_cell in col :
        print(f'{col_idx + 1}번째 열 : {each_cell} : {each_cell.value}')
print('-' * 20)
for row_idx, row in enumerate(rows) :
    for each_cell in row :
        print(f'{row_idx + 1}번째 행 : {each_cell} : {each_cell.value}')

# 인덱스 값을 이용해서 값 출력
a3 = cols[0][2] # 열 기준으로 생성이 되었기 때문에 [열][행] 순서로 인덱스 사용
print(a3.value) # r1
a3 = rows[2][0] # 행 기준으로 생성이 되었기 때문에 [행][열] 순서로 인덱스 사용
print(a3.value) # r1

# 데이터 값 변경
a3.value = 'row1'
print(a3.value) # row1

# 워크북의 변경내용을 새로운 파일에 저장
workbook.save('./output/df3.xlsx')
