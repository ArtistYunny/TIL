A = [100, 25, 50, 140, 33, 
     40, 420, 1, 4, 12] # 단위 : 만원

# 등급 구하기
amount = 0 # 전체 구매 금액
count = 0  # 전체 구매 횟수

# A 고객의 전체 구매 금액을 구한다.
for purchase in A:
    amount += purchase
    count += 1

print(f'A 고객의 전체 구매 금액은 {amount}만원입니다.')
print(f'A 고객의 구매 횟수는 {count}회입니다.')

condition1 = amount >= 1000 # False
condition2 = count >= 10 # True

# 등급 구하기
if condition1 and condition2:
    grade = 'VIP'
elif condition1 or condition2:
    grade = '우수'
else:
    grade = '일반'

print(f'현재 A고객의 등급은 "{grade}"입니다.')

# 새로 구매할 가방의 가격 : 100 * (1-할인율)

# VIP 할인율 = 0.15
# 우수고객 할인율 = 0.1
# 일반고객 할인율 = 0.05
print('====================================')
price = int(input('새로 구매할 제품의 할인 전 가격:'))

if grade == 'VIP':
    price = price * 0.85
    # price *= 0.85
elif grade == '우수':
    price *= 0.9
else:
    price *= 0.95

print(f'새로 구매할 가방은 {int(price)}만원입니다.')

A.append(price) # 구매 완료후, 구매내역에 반영

amount += price
count += 1

condition1 = amount >= 1000 # False
condition2 = count >= 10 # True

# 등급 구하기
if condition1 and condition2:
    grade = 'VIP'
elif condition1 or condition2:
    grade = '우수'
else:
    grade = '일반'

print(f'A고객의 새로운 등급은 {grade}입니다.')