import numpy as np

print(f'=============== [2] 기술통계의 활용 ===============' )

prices = [300000, 350000, 400000, 450000, 500000, 550000, 600000, 5000000]

print('(1) 중앙값의 적용')
print('- 중앙값을 사용해야 하는 이유 : 이상치에 영향을 덜 받기 때문에')

print(f'평균 : {sum(prices)/len(prices)}') # 영향을 많이 받음
print(f'중앙값 : {(prices[3]+prices[4])/2}') # 영향을 덜 받음

answer = np.median(prices)
print(f'numpy로 구하는 중앙값 : {answer}')
print()

print("(2) 최빈값의 활용")
subjects = ["Python", "Java", "Python", "C++", "Python", "Java", "C++", "Python", "Data Science", "Data Science", "Python"]

subjects_count = {}

for subject in subjects:
    if subject not in subjects_count:
        subjects_count[subject] = 1
    else:
        subjects_count[subject] += 1

best_sub = "" 
best_cnt = 0

for sub, cnt in subjects_count.items():
    if cnt > best_cnt:
        best_cnt = cnt
        best_sub = sub

print(f'최빈 과목은 {best_sub}, 나타난 횟수는 {best_cnt}')

from collections import Counter

result = Counter(subjects)
print(result)
print(result.most_common(1))
print()

print("(3) 범위와 사분위수 범위")
scores = [55, 60, 65, 70, 75, 80, 85, 90, 95]
print(f'범위 : {max(scores) - min(scores)}')

# 사분위수 범위
Q1 = np.percentile(scores,25)
Q3 = np.percentile(scores,75)

print(Q3 - Q1)

print("(4) 분산과 표준편차의 이해")
A = [70, 75, 80, 85, 90]
B = [70, 80, 80, 80, 90]

A_mean = sum(A)/len(A)
A_var = 0
for a in A:
    A_var += (a - A_mean) ** 2

A_var /= len(A)
print(f'A의 분산 : {A_var}')

B_var = np.var(B)
print(f'B의 분산 : {B_var}')

A_std = np.std(A)
B_std = np.std(B)

print(f'A 표준편차 : {A_std}')
print(f'B 표준편차 : {B_std}')

print()
print("(5) 왜도와 첨도의 적용")