# Read a number and print its digits in reverse order.
# Example input: 123
# Example output: 321

num=input("Enter the Number: ")
num_box=[]
for i in num:
    num_box.append(i)
for j in range(1,len(num)+1):
    print(num_box[-j],end="")