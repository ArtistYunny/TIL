# 리스트

numbers = [10,20,30,40,50] # list(range(10,51,10))
print(type(numbers))

# 리스트 = 순서가 있는 자료형
print(numbers[2]) # 인덱싱 = 순서, 위치로 값을 조회
print(numbers[3])

# 인덱스        0, 1, 2, 3, 4
# 음수 인덱스   -5,-4,-3,-2,-1 (n-1)

# start:end:step
# start ~ end-1, step 동안

print(numbers[2:4:1])   # 양수 인덱싱 / 슬라이싱
print(numbers[-3:-1])   # 음수 인덱싱 / 슬라이싱
print(numbers[::-1])    # 뒤집기

# 삽입
numbers.append(60)
print(numbers)

# 삭제
last_value = numbers.pop()
print(last_value)   # 원소 추출
print(numbers)

# 리스트 = 가변 자료형 (mutable) 모든 자료형을 담을 수 있다
numbers[2] = '30 입니다.'
print(numbers)

# 문자열 = 컨테이너 자료형
# 문자를 연속된 공간에 순서있게 모아 놓은 집합체

# 인덱스 조회 -> 가능
# 슬라이싱 -> 가능

# (주의) 문자열 = 불변자료형 (immutable) 불변
s = 'python'
# s[0] = 'P' 'str' not support. 불가능하다 자료형 일부이기 때문에

# 방법1 : 슬라이싱
s = 'P'+ s[1:] # 재할당
print(s)

# 방법2 : 메소드 이용
new_s = s.capitalize() # 새로운 문자열 반환
print(new_s)

# 형변환: 문자열 -> 리스트
# 문자열 -> 불변
# 리스트 -> 가변
print(list(new_s))