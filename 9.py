# 9. Find largest of two numbers

A, B = map(float, input("Enter Two Number: ").split())

if (A == B):
    print(f"{A} and {B} both are equal.")
elif (A < B):
    print(f"{B} is Greater than {A}")
elif (A > B):
    print(f"{A} is Greater than {B}")
else:
    print("Enter Numberical Values")