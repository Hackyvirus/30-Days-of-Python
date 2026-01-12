# 22. Sum of digits

sum = 0

number = input("Enter a Number: ")

for i in number:
    sum += int(i)

print(f"Sum of Digits in {number}: {sum}")