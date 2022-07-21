# 응용예제 1)

# def vending_machine(money) :
#     price = 700
#     count = money // price
#     for drink in range (count + 1) :
#         change = money - drink * price
#         print(f'음료수 = {drink}, 잔돈은 {change}')
      

# vending_machine(3000)


# 강사님 힌트(로직)
# # money = 3000
# # price = 700
# # count = money // price
# # for drink in range(count + 1) :
# #     change = money - drink * price 
# #     print(f'(음료수 = {drink}개, 잔돈 = {change}')


# 응용예제 2)


# def get_average(marks) :
#     total = 0
#     for subjet in marks :
#         total += marks[subjet]




#     # sum = 0
#     # for key in marks : 
#     #     sum += marks[key]
#     #     return sum / len(marks[key])


# marks = {'국어' : 90, '영어' : 80, '수학' : 85}
# average = get_average(marks)
# print(f'평균은 {average}점 입니다.')



# # 강사님 힌트 (로직)

# sum = 0
# for key in marks :
#     sum += marks[key]
    

# print(f'총점 : {sum}')
# print(f'평균 : {sum / len(marks)}')