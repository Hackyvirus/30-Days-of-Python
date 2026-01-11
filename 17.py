# 17. Sum of first N numbers

N = int(input("Enter the value of N: "))

sum = 0
for i in range(N):
    sum+=i+1 

print(f"Sum of first {N} Number: {sum}")