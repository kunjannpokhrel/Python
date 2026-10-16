# Read a number and print a square multiplication table using that number of rows and columns.
# Example input: 3
# Example output: 1 2 3
#                 2 4 6
#                 3 6 9

num=int(input("Enter the Number: "))
for i in range(1,num+1):
    print(i,end=" ")
    print(2*i,end=" ")
    print(3*i,end="\n")