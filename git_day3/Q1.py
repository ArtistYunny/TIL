scores = [85, 90, 78, 95, 88]

print(f'=============== [1] 기초 계산 ===============' )
print(f'(1) 평균 : {sum(scores)/len(scores)}')

# 중앙값 계산하기
# 정렬 -> 중간을 찾아서 본다!
scores.sort() # 오름차순 정렬

print(f'(2) 중앙값 : {scores[2]}')

score_count = {}

for score in scores:
    if score not in score_count:
        score_count[score] = 1
    else:
        score_count[score] += 1

print(f'(3) 최빈값 : {score_count}')

print('=> 없음')