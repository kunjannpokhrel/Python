# Read a string and count how many vowels it contains.
# Example input: education
# Example output: 5

word=input("Enter Word: ")
vowels=['a','e','i','o','u']
count=0
for i in word:
    if i in vowels:
        count+=1
print(count)