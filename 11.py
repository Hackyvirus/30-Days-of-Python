# 11. Check positive, negative, or zero

A = float(input('Enter A number: '))

if A == 0:
    print(f'{A} is 0')
elif A > 0:
    print(f'{A} is Positive Number')
elif A < 0:
    print(f'{A} is Negative Number')
else:
    print(f'{A} is Not a Digit')