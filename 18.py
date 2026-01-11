# 18. Print even numbers till N

N  = int(input("Enter the Value of N: "))

for i in range(N):
    if i == 0:
        continue
    elif i == 1:
        print(f"{i} is Not Even Nor Odd")
    elif i%2 == 0 and i>1:
        print(f"{i} is Even Number")
    elif i%2 != 0:
        print(f"{i} is Odd Number")
