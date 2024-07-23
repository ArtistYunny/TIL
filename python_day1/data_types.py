# 기본 자료형

# 1. 숫자형 : 정수형(int. 양, 음, 0) / 실수형(float) -> 소수점의 유무
print(type(1))
print(-2)
print(0)

# 숫자형 : 실수형(소수점이 있을 때)
# type 함수 자료형을 알려준다

print(type(1.0))
print(-2.0)
print(3.14)

# 2. 문자형 (string, str로 표기): 문자의 형태를 가진 모든 글자들
# 큰 따옴표, 작은 따옴표, 다 가능
print(type("문자열입니다."))
print('문자열입니다')
print(type("1.0"))
print(type("0"))
print("0") #문자형
print(0) #숫자형
print(type(0)) #숫자형
print(type("")) #문자형
print("abcd")
print('!@#$%')

# print('문자열 만들 수 있을까?") 안 된다. 일반적인 작은 따옴표는 작은 따옴표로, 큰 따옴표는 큰 따옴표로 끝나야 한다
# print("""쌍따옴표를 쓰고 싶다면?"") 아래와 같이 하면 된다!
print('"쌍따옴표를 쓰고 싶다면"')
print("'작은 따옴표를 쓰고 싶다면'")
print('\'작은따옴표를 쓰고 싶다면?\'') #이스케이프 문자열을 인식시키지 않을거야

# 3. 불린형 : 연산의 결과. cf) 만약에 네가 3보다 큰 숫자를 가지고 있으면 평균이상이라는 것을 출력해. 그렇지 않으면 평균이하를 출력해
print(True) # 참
print(False) # 거짓
print(type(True)) #class bool
