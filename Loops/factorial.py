# Read a number and calculate its factorial.
# Example input: 5
# Example output: 120

num=int(input("Factorial Of The Number: "))
ans=1
for i in range(1,num+1):
    ans*=i
print(ans)