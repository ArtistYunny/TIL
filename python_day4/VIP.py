A = [100, 25, 50, 140, 33, 
     40, 420, 1, 4, 12] # 단위 : 만원

x = sum(A)
y = len(A)

print(f'A 고객의 전체 구매 금액은 {x}만원입니다.')
print(f'A 고객의 구매 횟수는 {y}회입니다.')

def grade_classifer(amount, count):
    condition1 = amount >= 1000
    condition2 = count >= 10
    
    if condition1 and condition2:
        return 'VIP'
    elif condition1 or condition2:
        return '우수'
    else:
        return '일반'

grade = grade_classifer(x, y)
print(f'현재 A고객의 등급은 "{grade}"입니다.')

print('====================================')
price = int(input('새로 구매할 제품의 할인 전 가격:'))

if grade == 'VIP':
    price *= 0.85
elif grade == '우수':
    price *= 0.9
else:
    price *= 0.95

print(f'새로 구매할 가방은 {int(price)}만원입니다.')

A.append(price)
new_grade = grade_classifer(sum(A),len(A))

print(f'구매 후 등급은 "{new_grade}" 입니다.')











