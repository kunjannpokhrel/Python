# Read a string and find the first character that appears more than once.
# Example input: swiss
# Example output: s

start=True
word=input("Enter Word: ")
for i in word :
    for j in range(len(word)):
        if i == word[j] and j!=word.index(i) and start:
         print(i)
         start=False