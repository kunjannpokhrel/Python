# Read a string and count its uppercase letters, lowercase letters, digits, and special characters.
# Example input: Hello123!
# Example output: Uppercase = 1, Lowercase = 4, Digits = 3, Special = 1

word=input("Enter The Word: ")
lowercases="abcdefghijklmnopqrstuvwxyz"
uppercases=lowercases.upper()
Digit="1234567890"
Specials='''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
Uppercase,Lowercase,Digits,Special=0,0,0,0

for i in word:
    if i in lowercases:
        Lowercase+=1
    elif i in uppercases:
        Uppercase+=1
    elif i in Digit:
        Digits+=1
    elif i in Specials:
        Special+=1
print(f"Uppercase = {Uppercase}, Lowercase = {Lowercase}, Digits = {Digits}, Special = {Special}")