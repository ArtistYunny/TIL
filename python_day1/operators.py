# 연산자
# "처리"

a = 5
b = 2

# 1. 산술 연산자
print(a + b) # 7 / int
print(a - b) # 3 / int
print(a * b) # 10 / int
print(a / b) # 2.5 / float

a = 4
print(a + b) # 6 / int
print(a - b) # 2 / int
print(a * b) # 8 / int
print(a / b) # 2.0 / int 정수 / 정수 0이 온다는 것을 검사하지 않는다. 어떤 값 나누던지 Float

# 몫 / 나머지 / 제곱  (모두 다 int) 정수라는 조건이 있어서. 몫은 항상 정수.
print(a // b) # 2 / int
print(a % b) # 0 / int
print(a ** b) # 16 / int

a = 5
print(a // b) # 2 / int
print(a % b) # 0 / int
print(a ** b) # 16 / int

a = 5.1
print(a // b) # 2 / int
print(a % b) # 0 / int
print(a ** b) # 16 / int

# 복합 연산자
# 산술연산자와 할당 연산자를 함께 쓰는 것
# +=, -=, *=, /=

a=5

# a= a+b
a += b
print(a)

# 3. 비교 연산자 (값과 값을 비교한다!)
# <. >, <=, >=, ==, !=
# 비교 연산의 결과는 True 혹은 False -> bool 자료형
a = 5
b = 2
print(type(a < b))
print(type(a != b))

a = 'a'
b = 'b'

print(a != b) # True / False (아스키코드 값)
print(a > b) # False(알파벳에도 순서가 있기 때문에)
print(a >= b)

# 문자와 숫자는 비교하지 못한다

b = 'a'
print(a == b)

a = 'aa'
b = 'ab'

print(a < b)

# 논리연산자 (and, or, not)
# a and b : a와 b, 둘다 True 여야만 True
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

a = 'a'
b = ''

print(a and b) #빈 문자, False 
a = 20 > 10             #비교연산자 -> T 
b = 'hello' == 'Hello'  #비교연산자 -> F
print(a and b) # False
print(a or b) # True
print(not a) # False