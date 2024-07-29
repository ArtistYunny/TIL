# <절댓값 구하기>
# A와 B 정수를 입력받아 두 수의 차의 절댓값을 반환하는 함수를 만드시오.
# 만약 7과 -3을 받았다면 10을 출력해야 한다.

A = int(input())
B = int(input())

def get_absolute_value(x, y):
    diff = x - y    # +, -, 0
    if diff > 0 : # 양수인 경우,
        return diff
    else:   # 산술연산으로 부호 바꾸기
        return -1 * diff

print(get_absolute_value(A, B)) # A, B를 입력받아서 터미널에서 출력