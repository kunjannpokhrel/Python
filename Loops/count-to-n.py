# Read a number and print every number from 1 up to that number.
# Example input: 5
# Example output: 1 2 3 4 5

num=int(input("Enter The Number: "))
for i in range(1,num+1):
    print((num+i)-num , end=" ")