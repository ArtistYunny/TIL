# [for 문 실습]
# for문으로 range를 활용하여 1~10 더한값 55 출력하기
# for문과 조건문을 사용하여, 짝수인 경우만 더한 값을 출력하기

answer = 0

for i in range(1,11,1): # 1~10까지 추출, 1은 생략가능
    answer = answer + i # 재할당, 누적해서
    # print(answer)
print(f"1부터 10까지 더한 값은 {answer} 입니다!")

# del answer -> 메모리 할당량에서 많이 차지하고 있는데, 쓰고 싶지 않을 때 쓴다
# print(answer)
# 변수 다시 써도 된다. answer = 0으로 재할당, i도 재할당 된다

even = 0
for j in range(2,11,2):
    #print(j) -> 2,4,6,8,10
    even = even + j
print(f"1부터 10에서 짝수인 경우만 더한 값은 {even} 입니다!")

even_1 = 0
for k in range(1,11):
    if k % 2 == 0:
        even_1 += k
print(even_1)