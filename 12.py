# 12. Find largest of three numbers

A, B, C = map(int,input("Enter 3 Number (Use Spaces): ").split())

print('A is Greater than B and C') if A > B and A > C else print('A is not Max')
print('B is greater than A and C') if B > C and B >  A else print('B is not max')
print('C is greater than A and B') if C > A and C > B else print('C is not max')