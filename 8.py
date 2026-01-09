# 8. Check even or odd

print("Check Even Or Odd ---------")

num = float(input("Enter a Number: "))

if(num == 1):
    print(f"{num} is Not even nor Odd")
elif(num/2 == 0):
    print(f"{num} is Even Number.")
elif(num/2 != 0):
    print(f"{num} is Odd Number")
