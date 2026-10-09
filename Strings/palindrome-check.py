# Read a string and check whether it reads the same forward and backward.
# Example input: level
# Example output: Palindrome

word=input("Enter Word: ")
for i in range(len(word)):
    if word[i]==word[-i-1]:
        Palidrome=True
    else:
        Palidrome=False
if Palidrome:
    print("ITS A PALIDROME")
else:
    print("ITS NOT A PALIDROME")