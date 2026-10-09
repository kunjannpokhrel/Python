# Keep reading numbers until 0 is entered, then print the largest number entered.
# Example input: 4 9 2 0
# Example output: 9

max=0
num=1
while num != 0:
    num=int(input("Input Your Number: "))
    if num>max:
        max=num
    else:
        max=max
print(max)    