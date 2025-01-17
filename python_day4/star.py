# <별 찍기>
# 자연수 N을 입력받아, N줄까지 별을 출력하는 함수를 만드시오.
# 첫 번째 줄은 별이 1개이며, N번째 줄은 N개의 별이 찍혀야 합니다.

# ex) 만약 N이 3 이라면?
# *
# **
# ***

N = int(input('N을 입력해 주세요.'))

print('N이 입력되었습니다.')
# 유형은 어떻게 되나요?
# 매개변수 0, 반환값 x
# (define) 함수의 선언만! 했기 때문에

def print_stars(N): # 입력으로 들어가야 한다.
    for i in range(1,N+1):
        print('*' * i) 

print('함수 선언이 완료 되었습니다')

# 함수 호출하기
# (call) 호출해서 사용
# 잘못된 케이스
# 에러 발생
# 경우 1 : 입력받아야 하는데, 입력을 받지 못함
# print_stars()

# 경우 2 : 반환값이 없는데, 반환받으려 하는 경우
# p = print_stars(N)
# print(p)                # 반환되는 값이 없음에도 불구하고 받으려고 했기 때문에
                          # 파이썬에서 자체적으로 "없다"라는 None을 할당해 버림

print('함수 호출을 시작합니다')
print_stars(N)   # 정의한 함수를 올바르게 호출한 코드
print('함수가 종료되었습니다')

# print() : print 함수 안에 들어간 리스트, 문자열, 숫자건 "출력"
# return : 함수의 결과를 반환

# y = 2*x + 1

# x = 1
# y?

def func(x):
    return 2*x + 1

print('함수 시작')
y = func(2) # 어? 너 반환되는 값 없는데? 그래도 원한다면... none
# step 1) func(2) 를 수행한다.
    # 1-1) x라는 매개변수(함수 안에서 사용하는 변수)에 2라는 인자(값)를 입력받는다.
    # 1-2) print를 통해 2*x + 1 을 계싼하고, 이를 출력한다.
    # 1-3) 함수에 속해있는 모든 코드가 끝났습니다. 반환 없이 종료합니다.
# step 2) y에 func(2) 함수를 실행한 결과를 할당합니다.
    # func(2)가 반환하는 것은 아무 것도 없습니다.
        # print는 사용자 보기 편하라는 거지, 프로그램이 사용하라고 보여주는 게 아니야!
    # 아무것도 없는데(Nothing), 할당하기 원해?
    # None 을 넣어줄게.
print(y)
print('함수 끝')
print(type(y))