# 추가 문제
# 다음은 천재 마트의 일자별 매출일에 대한 리스트입니다.
# sales = [2000, 3000, 4000, 1000, 1500, 3800, 200, 2900, 1300]
# for문을 돌며, 최고 매출이 일어난 일자와 최저 매출이 일어난 일자를 각각 파악하세요.
# # 예시
# 최고 매출 : 3일차, 4000만원
# 최저 매출 : 7일차, 200만원
# :압정: 힌트 : answer와 같이 최고 매출 / 최저 매출을 기록할 수 있는 max_sales, min_sales를 정의하여 사용하세요.

sales = [2000, 3000, 4000, 1000, 1500, 3800, 200, 2900, 1300]

max_sales = sales[0] # 초기화 처음 리스트 가져와 인덱싱
min_sales = sales[0] # 초기화 처음 리스트 가져와 인덱싱

max_day = 1
min_day = 1

# 반복문을 통해 최고 매출과 최저 매출을 갱신
for i in range(len(sales)): #range(0->초기값, 9(9-1[8]), 1->초기값)
    if sales[i] > max_sales: #[0]~[8] 방 돌아서 기존보다 큰거 찾아줘
        max_sales = sales[i] # 그리고 재정의
        max_day = i + 1  # 일자는 1부터 시작, 1을 더함
    if sales[i] < min_sales: #[0]~[8] 방 돌아서 기존보다 작은거 찾아줘
        min_sales = sales[i] #재정의
        min_day = i + 1  # 일자는 1부터 시작, 1을 더함

print(f"최고 매출: {max_day}일차, {max_sales}만원")
print(f"최저 매출: {min_day}일차, {min_sales}만원")