# Read a number and add all of its digits together.
# Example input: 123
# Example output: 6

num=input("Enter the Number: ")
ans=0
for i in num:
    ans+=int(i)
print(ans)