# Read a number and print its multiplication table from 1 to 10.
# Example input: 5
# Example output: 5 x 1 = 5 ... 5 x 10 = 50

number=input("Enter Your Number: ")
for j in range(1,11):
 print(f"{number}*{j}={int(number)*j}")