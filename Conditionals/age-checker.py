# Ask for a person's age and say whether they are an adult or a minor
# Example input: 20
# Example output: You are an adult

age=int(input("Enter Your Age: "))
if age>=18:
    print("You Are An Adult")
else:
    print("You Are A Minor")