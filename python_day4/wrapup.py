# dictionary
# {}
# key - value 한쌍의 구조!
# 순서는 따로 존재하지 않는다.

numbers = [1,2,3,4,5]
numbers = [1]

numbers_dict = {'name':'alex', 'age':20, 'license': True, 'salary': 7000}

print(numbers_dict[license])
# key의 이름으로 value를 불러오기

# 딕셔너리 -> 변경이 가능 "가변자료형"
numbers_dict['salary'] = 1000
print(numbers_dict)