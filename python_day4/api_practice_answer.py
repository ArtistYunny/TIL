# [API 분석 실습 1]
users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}

# Q1. 라이센스가 있는 인원들의 숫자 구하기
license_cnt = 0

for info in users['information']:
    if info['license'] == True:
        license_cnt += 1
# print(license_cnt)

# Q2. 모든 사람의 나이의 평균 구하기
# 평균  = 총합 / 갯수

age_sum = 0
for info in users['information']:
    age_sum += info['age']

# print(age_sum) # 총합 구하기 완료
# print('나이의 평균 : ')
# print(round(age_sum/users['total_user'],1))

# Q3. 라이센스가 없는 사람들의 이름 모으기

no_license = []

for info in users['information']:
    if info['license'] == False:
        no_license.append(info['name'])

# print(f'운전면허가 없는 사람은 {no_license} 입니다.')

# 한번에도 가능?
license_count = 0
no_license = []
age_sum = 0

for info in users['information']:
    # 라이센스 보유 여부에 따라, 
        # license == True : 라이센스가 있는 인원들의 숫자 구하기
        # license ==False : 라이센스가 없는 사람들의 이름 모으기
    if info['license'] == True:
        license_count += 1
    else:
        no_license.append(info['name'])
    
    # 조건이 없이! "모든" 사람의 나이의 평균 구하기
    age_sum += info['age']

# 1
print(f'운전면허를 보유하고 있는 사람은 {license_count}명입니다.')
print()

# 2
age_mean = age_sum/users['total_user']
print(f'평균 유저의 나이는 {round(age_mean,1)}살입니다.')
print()

# 3 
print(f'운전면허가 없는 사람은 {no_license} 입니다.')