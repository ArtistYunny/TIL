# 변수
# 할당 연산자 (=)
#     형태 : 변수이름 = 변수의 값

# name = "류용윤" #문자열
# age = 34        #숫자 -> 정수형
# is_male = True  #불린형

# print("이름은 : ")
# print(type(name)) #자료형 type함수

# print("나이는 : ")
# print(type(age))

# print('남자인가요? : ')
# print(type(is_male))

# 변수 이름 짓기
# 이름 = '류용윤'
# print(이름) 권장하지 않는다. 글로벌한 유저들, 통용언어. 영어를 권장
# 1name(x), 띄어쓰기도 안된다. 언더바 대체
name_1 = '류용윤'
print(name_1)

del name_1 #변수를 삭제하는 예약어
# del = '삭제를 의미함' 예약어로 할당할 수 없다

# print = '출력을 의미함'
# print(print) 이미쓰고 있는 함수에 덮으면 안된다. 못쓰게 된다
print_meaning = '출력을 의미함'
print(print_meaning)

# number = 1
# number = 2
# number = 3 # 재할당. 마지막에 넣은 값이 출력이 된다. 반복문도 마지막 값이 남아있다

# print(number)

x = 10
y = x # 모든 것은 객체이다. 주소값 참조 개념. 가지고 오는 것.
print(x)
print(y)

x = 20 #재할당된 값으로 출력
print(x)
print(y)