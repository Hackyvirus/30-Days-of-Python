# 4. Swap two variables

print("We are swapint 2 Numbers")

A , B= map(int,input("Enter 2 Numbers: ").split())

print("Before Swapping---------")
print(f"A: {A}\nB: {B}\n")

print("After Swapping-----------")
temp = A
A = B 
B = temp 
print(f"A: {A}\nB: {B}")


