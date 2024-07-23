# 변수 만들기 : 변수 a 에 문자열 456 을 할당하고, 변수 b 에 정수 789 를 할당하세요.
# 연산자 : a 와 b를 더하려 하였을 때, 어떠한 일이 일어나나요? 코드를 추가하여, <수리적 연산을 완료>해 봅시다.

# TypeError: can only concatenate str (not "int") to str
a = "456" # 문자열
b = 789   # 정수형
a = int(a) # 재정의, 목적에 따라 다름. "계속 쓸거라고 한다면 재정의 하라!"
# print(int(a) + b) # 한번만 쓰면 직관적인 코드가 될 수 있다

print(a+b)

print(type(a))
print(type(b))
# print(type(int(a) + b))

# 3. 식별자와 리터럴
# 변수의 이름을 식별자라고 합니다. 
# 아래는 변수를 할당하는 코드인데, 각각 어떠한 문제점이 있을까요? 
# 왜 이렇게 식별자 이름을 설정하면 안될지 생각해 봅시다

# 1number = 1.0
# print(1number) 
# 식별자의 이름은 숫자로 시작하면 안 된다
# 숫자로 시작하면 숫자로 인식하려함

number_1 = 1.0
print(number_1)

# print = "출력을 위한 함수" 
# # 기존에 파이썬에서 쓰고 있는 내장 함수를 덮어쓰고 있기 때문에
# 더 이상 print 함수의 기능을 하지 못함
# print(print)

print_ex = "출력을 위한 함수"
print(print_ex)


# 4. 비교 연산자 / 논리 연산자
# 변수 c는 " " 공백이 있는 문자열이고, d 는 a에서 b를 나눈 몫입니다.
# 두 변수를 가지고 논리 연산자, 비교 연산자를 사용해서 True를 반환하는 2개 이상의 케이스를 만들어 내세요.

# a=456 b=789

c = " "      #str 공백이 있는 문자열
d = a//b     #int a에서 b를 나눈 몫 0. 비어있다

print(c)    
print(d)   

print(type(c))  #str
print(type(d))  #int

#비교 연산자
# ==, != : 단순 비교 ->(값이 일치하는지 판단)
# >, <, >=, <= : 대소 비교 (자료형 일치)

# print(c>d) x
print(c == d) # False
print(c != d) # True
print(d == 0)

# 논리 연산자
print(not c == d) # True
print(not d) # True 비어있다

# and
# or

print(bool(c)) # 공백 값이 있다 True
print(bool(d)) # False 0, 0.0은 False. 1, -1은 True


print(bool(c) or bool(d))