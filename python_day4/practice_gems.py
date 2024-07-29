# 각각 등급 별로, 몇개의 보석이 있는지 알아 봅시다.
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {} # 빈 딕셔너리로 만들 것!

# grades = {1:0, 2:0, 3:0}

# for gem in gems:
#     grades[gem] += 1    # 1:2, 2:3, 3:5 개수 세기

# print(grades[1]) keyError. 인덱스 에러와 같은 형태!

for gem in gems:
    #if gem in grades: #grades dict에 있으면 이미 값이 있음
    if gem not in grades: # gem이라는 녀석에 key 값이 없으면?
        grades[gem] = 1   # gem에 1을 넣어줄 거야, (색인 안에 넣어줄거야 value 값)
                          # 보석의 등급이 처음 나타나면,
                          # 처음 센다. (1을 할당). 1을 값으로 넣는다.
    else:                 # key 값이 있으면, -> 이미 한 번은 세어졌다.
        grades[gem] += 1  # 보석 이미 한번은 세어졌으면,
                          # 복합연산자를 통해 1번 더 세어 준다

#    grades[1] = 1   # 키1에 1을 넣을거야
# print(grades[1])    # {1:1}

# 코드를 작성해 봅시다.
# print(gems)
# print(type(gems))   #리스트.

#for gem in gems: # 돌려 int
#    if gem in grades:   # 제어하기 
#        grades[gem] = grades[gem] + 1
#    else:
#        grades[gem] = 1


#결과
print(grades)
#{3:5,1:2,2:3}