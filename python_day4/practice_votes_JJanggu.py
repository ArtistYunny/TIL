# 반장선거 or 인기투표!
# 후보가 없는 반장선거

votes = ['짱구', '철수', '수지', '짱구', '훈이', '맹구',
         '수지', '수지', '수지', '짱구', '유리', '철수']

print(len(votes))

# result = {'세연':0, '지민':0} 할 수 없다
result = {}

for vote in votes:
    if vote in result:  # 안에 있다면 하나를 셀게
        result[vote] += 1   # 아무것도 없어 Key Error

    else:
        result[vote] =1     # 처음발견 1로 카운트
    print(result)

print(result)