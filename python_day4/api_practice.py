# [API 분석 실습 1]

users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}
# Q1. 라이센스가 있는 인원들의 숫자 구하기 licnese == true
print(users['information']) # list
print(type(users['information']))

license_cnt = 0

for info in users['information']:   # information 중 license 출력
    # print(info)
    # print(type(info)) dict

    print(info['license'])
    if info['license'] == True :
        license_cnt += 1
        print(f"라이센스 가진 사람은 {license_cnt}명 입니다!")
    else:
        print(f"{info['license']}는 라이센스가 없습니다!")


# Q2. 모든 사람의 나이의 평균 구하기

users_sum = 0
for info in users['information']:
    print(info['age']) # 3, 7, 4 가져왔다
    users_sum += info['age']    # info['age']를 값을 가져와 더한다!
    print(users_sum) 
print(round(users_sum/users['total_user'], 1 ))    # users 참조하여 total_user값을 가져와 3명으로 나눈다


# Q3. 라이센스가 없는 사람들의 이름 모으기
for info in users['information']:   # 인포메이션을 인포에 저장하고
    print(info['name']) # 인포alex, june, peter 가져왔다
    if info['license'] == False:    # 라이센스가 없다면
        print(f'{info['license']} 없습니다')

       
no_license = []

for info in users['information']:
    if info['license'] == False:
        no_license.append(info['name'])

print(f'운전면허가 없는 사람은 {no_license} 입니다')
    
    # print(info['license'])  # True/False -> 3개의 값을 출력한다
    # if info in users[] == True:
    #     count += 1
    #     print(count)

# 한번에도 가능

    # 라이센스 보유 여부에 따라, 
    # license == True : 라이센스가 있는 인원들의 숫자 구하기
    # license == False : 라이센스가 없는 사람들의 이름 모으기