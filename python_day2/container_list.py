# 리스트 (list)
# 대괄호 []
students = ['용윤', '수정', '은선']
print(students)
print(type(students))
print(len(students))

# 가장 먼저 온 사람!
# 순서가 가장 이른 사람 -> 첫번째 사람
print(students[0]) 
print(students[1]) # 두번쨰 사람
print(students[2]) # 세번째 사람

# 가장 마지막 온 사람!

# 리스트 조회
print(len(students)-1) #가능하지만
print(students[-1])

grade1 = ['용윤', '수정', '은선'] # 3등
grade2 = ['수진', '민정', '지민'] # 4~6등

print(grade1 + grade2)
print(grade1 * 2)
# print(grade1 * grade2) -> 리스트, 문자열은 가능하지만. 문장끼리는 불가능하다

