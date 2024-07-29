#while문으로 1부터 10까지 더한 값 출력하기

# 인덱스 j : 0,1,2,3...9
numbers = [1,2,3,4,5,6,7,8,9,10]

j = 0
answer = 0 # 반복문을 돌면서 각 값을 더해줄 변수

while j < len(numbers): # 인덱스가 numbers 리스트의 길이보다 작을 때 (n-1) 반복해줘 # range는 자료형이므로. 비교할 수가 없다. int형이랑
    answer = answer + numbers[j]
    j += 1
print(answer)

# 오류 사례 <= 하면. 인덱스 10이 없어서 찾지 못한다


# for number in numbers:
#     answer += number
#     print(answer)

# i = 0
# sum = 0

# while i < len(numbers):
#     sum = sum + numbers[i]
#     i += 1

# print(sum) sum은 함수이다. 변수로 쓰는 것 지양

