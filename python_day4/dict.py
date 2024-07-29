# 딕셔너리 (dict)
# 사전 -> 쌍으로 이루어져 있는 형태를 가진다.
# {}  # 중괄호로 만든다!

# key:value -> 매핑되어 있다
user = {'name':'alex', 'age':15, 'license':False,
        'consume':[10,2,30,4,3]}
print(user)
print(type(user))   # dict 자료형

# 특징 1: 순서가 없는 자료형
# print(user[0])    # 입력된 순서로 불러낼 수 없다
print(user['name']) # key로 value를 데리고 옴 -> 조회가능

# value의 의미를 key 로 나타낼 수 있다.

# 주의!
# 1. key는 유일해야 한다.
# 2. key는 바뀌면 안된다.

# 특징 2 : 가변 자료형
# 가능하다. 변경이
user['name'] = 'kyle'   # Key를 기준으로 value는 바꿀 수 있다, 재정의
print(user)

print(sum(user['consume'])) # 예습 : 합계를 구하는 함수 sum
user['grade'] = '일반'
print(user)

# user_list = ['alex', 15, False, [10,2,30,4,3]]
# print(user_list[0]) #리스트 위치로 뽑았었다

# 기초 자료 구조와 로직 설계