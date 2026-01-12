# 24. Armstrong number

def is_armstrong(num):
    n = len(str(num))
    temp = num
    total_sum = 0
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** n
        temp //= 10
    return total_sum == num

print(is_armstrong(370))