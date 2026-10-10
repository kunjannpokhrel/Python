# Read a number of rows and print a star pattern that grows by one star on each row.
# Example input: 4
# Example output: *
#                 **
#                 ***
#                 ****

num=int(input("Enter the Number: "))
for i in range(1,num+1):
    print("*"*i)