# 2. Take user input and print it
import sys

# Normal Input
print(input("Enter Your Age: "))


# Multileple Inputs at on time
a,b = map(int,input("Enter two Numbers:  ").split())
lists = list(map(int,input("Enter two Numbers:  ").split()))
print(f"A: {a}\nB: {b}\n")
print(f"List: {lists}")


# Taking input from Command Line
if len(sys.argv) > 1:
    print(sys.argv[1])

# from system stdinput
line = sys.stdin.readline().strip()
int_number = int(sys.stdin.readline().strip())

print(int_number)