# 13. Check leap year

Year = int(input("Enter Year: "))

if Year%4 == 0:
    print(f"{Year} is Leap Year")
else:
    print(f"{Year} is Not Leap Year")