# Read a number and count how many digits it has.
# Example input: 12345
# Example output: 5

count=0
num=input("Number: ")
for i in num:
    count+=1
print(count)