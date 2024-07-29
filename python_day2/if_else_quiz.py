# 백화점 VIP 판별 프로그램
# VIP  : 1000만원 이상 소비, 구매 횟수 10번 이상
# 우수 : 둘중 하나라도 만족하면, 우수
# 일반 : 둘다 없으면 일반 고객
# 비교연산자 - True / False
# 논리연산자 - and, or

money = int(input('소비금액: (단위: 만원)'))
count = int(input('구매 횟수'))

# 코드를 입력하세요

money_check = money >= 1000
count_check = count >= 10

if money_check and count_check: # 논리연산으로 모두 만족하는가
    print("VIP 고객입니다")
elif money_check or count_check: # 논리연산으로 하나라도 만족하는가
    print("우수 고객입니다")
else:
    print("일반 고객입니다")