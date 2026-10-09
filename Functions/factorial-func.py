# Write a function that receives a number and returns its factorial.
# Example input: 5
# Example output: 120

num=int(input("Enter The Number: "))
def factorial():
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    return factorial

print(factorial())