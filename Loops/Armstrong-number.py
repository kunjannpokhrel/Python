# Read a number and check whether the sum of the cubes of its digits equals the original number.
# Example input: 153
# Example output: Armstrong number

num=input("Enter the Digit: ")
ans=0
for i in num:
    ans+=int(i)**3
if ans == int(num):
    print(f"{num} is a Armstrong number")
else:
    print(f"{num} is not a Armstrong number")