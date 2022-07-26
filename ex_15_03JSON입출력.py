# JSON 파일 입출력

# 1. JSON 파일이란?
# 데어터를 전달 할 때 사람이 읽고 쓰기 쉽도록 텍스트 형식을 정해 놓은 개방형 데이터 표준형식
# 많은 양의 데이터를 처리할 때는 속도가 느린 단점이 있으므로 경량의 데이터를 주고 받을때 주로 사용
# javaScript Object Nataion의 약자로 JavaScript의 객채 표현 방법이라는 뜻

# 2. JSON 데이터의 형식
# 속성 attribute - 값 value


# 3. JSON 파일 생성






# 

# import json
# dict_list = [
#     {
#         'name' : 'james',
#         'age' : 20,
#         'spec' : [
#             175.5,
#             70.5
#         ]
#     },
#     {
#         'name' : 'alice',
#         'age' : 21,
#         'spec' : [
#             168.5,
#             60.5
#         ]
#     }
# ]

# json_string = json.dumps(dict_list)

# with open('./output/dictList_01.json','w') as file :
#     file.write(json_string)

# print('dictList.json 파일이 생성되었습니다.')




################### 


import json
dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [
            175.5,
            70.5
        ]
    },
    {
        'name' : 'alice',
        'age' : 21,
        'spec' : [
            168.5,
            60.5
        ]
    }
]

json_string = json.dumps(dict_list, indent = 4)

with open('./output/dictList_02.json','w') as file :
    file.write(json_string)

print('dictList_02.json 파일이 생성되었습니다.')

