numbers = [1,2,3,4,5,6] 
print(len(numbers)) 

# 내장함수 len이 없었다면,

def len_func(numbers):
    num_len = 0
    for num in numbers:
        num_len +=1
    
    return num_len

print(len_func(numbers))