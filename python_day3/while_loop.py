# 반복문
# while : 조건이 만족하는 동안 반복

# while 조건:
    # 조건에 따라 반복하고자 하는 코드
    # (중요!) while문 안에서 조건을 변화해 나갈 수 있어야 함

greetings = ['안녕', '니하오', '봉주르', '올라'] # 리스트

i = 0
while i < len(greetings):
    print(i)
    print(greetings[i])
    i += 1

print('반복이 중단되었습니다')
print(i)

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = list(range(1,11))

print(numbers)

# for i in numbers:
#     print(i)

i = 0 # 인덱스의 초기화

while i < len(numbers):
    print(numbers[i])   #numbers의 위치를 가져와 주세요!
    i += 1

