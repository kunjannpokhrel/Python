# Read two strings and check whether they contain the same letters in a different order.
# Example input: listen / silent
# Example output: Anagrams

first_word=input("Enter your first word: ")
second_word=input("Enter your second word: ")
if sorted(first_word)==sorted(second_word):
    print("anagrams")
else:
    print("Not Anagrams")