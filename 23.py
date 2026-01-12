# 23. Palindrome number

number = int(input("Enter the Number: "))
temp = number
r = 0
while temp > 0:
    r *= 10
    r += temp%10 
    temp //= 10 

if r == number:
    print(f"{number} is Palindrone")
else:
    print(f"{number} is not Palindrone")
