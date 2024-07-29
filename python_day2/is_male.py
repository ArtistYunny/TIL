is_male = input('남성인가요 (Y/N): ' )      # str, 어떻게 형변환 할 것인가?

print(is_male) # False 인 경우, 어떻게 할 것인가 bool(input) -> 값이 있어서 true.

if is_male in ['True', 'TRUE', 'true', 'Y', 'y']:
    is_male = True #재할당 bool 값은 if문으로 가정문으로 할당시킨다!
elif is_male == 'N' or is_male == 'n':
    is_male = False
else:
    print("잘못 입력하셨습니다")

print(is_male)
print(type(is_male)) # bool