# 20. Reverse a number

Number = int(input("Enter a number: "))


def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r


print(funcition(123))