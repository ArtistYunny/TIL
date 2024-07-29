# 조건문
# 만약 조건을 만족하면, (조건 == True), 코드블럭1을 실행하고,
# 만약 조건을 만족하지 않는다면 (조건 == False), 코드블럭 2를 실행
# if 조건:
#   코드블럭
# else:
#   코드블럭

sale_rate = float(input('현재 할인율'))
price = 10000

condition = sale_rate >= 0.3 # 할인률이 30%가 넘으면

if condition:
    print('구매')
    print(price*(1-sale_rate))
else:
    print('구매하지 않음')