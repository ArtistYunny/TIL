user1 = {'name':'alex','age':37,'license':True}
user2 = {'name':'kyle','age':19,'license':True}
user3 = {'name':'peter','age':5,'license':False}

# 정보를 복잡하게 구조화 (API 예시)

user= {
    'total_user':3,
    'information': [
        {'name':'alex','age':37,'license':True},
        {'name':'kyle','age':19,'license':True},
        {'name':'peter','age':5,'license':False}
    ]
}
print(type(user))
# dictionary [key] 를 통해 value를 확인한다
print(len(user))

print(user['total_user'])   # 키 값을 가져와 벨류 확인. key 문자열, 벨류 리스트
print(user['information'])
print(type(user['information']))

#info = user['information']

for info in user['information']:   # information 중 name
    print(info['name'])

user_sum_age = 0

for info in user['information']:    # information 중 age
    print(info['age'])
    user_sum_age += info['age']
print(user_sum_age)
print(user_sum_age/user['total_user'])  #user에 찾아서 값을 가져와!


# print(info[0]) # type <dict>
# print(info[1])
# print(info[2])
# print(info[3]) # 길이 - 1 까지 인덱싱 가능 -> 없음

# 사실은 아래와 같다!
 