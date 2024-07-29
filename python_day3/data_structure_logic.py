# # dicionary
# # {}
# # key - value 한쌍의 구조!
# # 순서는 따로 존재하지 않는다.

numbers = ['alex',20,True,7000]
print(numbers[2])

numbers_dict = {'name':'alex','age':20,
                'license':True,'salary':7000}
 
print(numbers_dict['salary'])
# # key의 이름으로 value를 불러오기

# # 딕셔너리 -> 변경이 가능 "가변자료형"
numbers_dict['salary'] = 1000
print(numbers_dict)

gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0, 2:0, 3:0}

for i in gems:
    grades[i] += 1

print(grades)
# print(f'1등급 광물은 {grades[1]}개입니다.')
# print(f'2등급 광물은 {grades[2]}개입니다.')
# print(f'3등급 광물은 {grades[3]}개입니다.')

# salary  = [1,2,4,5,6,200,500,260]

# print(min(salary))
# print(max(salary))

# "python"