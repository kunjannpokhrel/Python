# Read a string and print it in reverse order.
# Example input: hello
# Example output: olleh

word=input("Enter Word: ")
for i in range(len(word)):
    print(word[-i-1],end="")