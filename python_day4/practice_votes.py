# 반장선거 or 인기투표!
# 후보가 없는 반장선거

votes = ['세연', '지민', '수진', '유진', '화영', '민정',
         '세연', '수진', '수진', '유진','유진', '유진',
          '화영', '민정', '화영', '민정', '지원' ]

print(len(votes))

# result = {'세연':0, '지민':0} 할 수 없다
result = {}

for vote in votes:
    if vote in result:  # 안에 있다면 하나를 셀게
        result[vote] += 1   # 아무것도 없어 Key Error

    else:
        result[vote] =1     # 셀게

print(result)