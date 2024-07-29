# break 만나기
names = ['티모시','변우석','이은선','김지민','김태현']
# i = 0 꼭! 할당해야 한다

# while True:
#     print(names[i]) # 무한루프 중. 계속해서 0이기 때문에 i+=1 필요!
#     if names[i] == '이은선':
#         print('우리반 슈퍼스타 영접!')
#         break
#     i += 1
# print(i)

names = ['변우석','김지민','티모시','김태현','김지원','유영채','최은지']
students = ['김지민','김태현','유영채','최은지','유수진','류용윤','김화영']

for name in names: # 컨테이너 안에서
    if name in students: # 컨테이너 비교 (멤버십 연산자)
        print(f'PM 7기 {name}님 등장!') # 필터링
        continue

    print(f'{name}님은 PM 7기가 아닙니다.')