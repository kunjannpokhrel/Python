# Read a number and find the sum of all numbers from 1 up to it (no direct fromula)
# Example input: 5
# Example output: 15

num=int(input("Enter the Number: "))
ans=0
for i in range(num+1):
    ans+=i
print(ans)