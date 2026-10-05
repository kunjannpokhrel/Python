# Read a purchase amount. Give 10% off at 5000 or more, 15% off at 10000 or more, and no discount below 5000.
# Example input: 12000
# Example output: 10200

amt=int(input("Purchase Amount: "))
if amt in range(5000,10001):
    print(f"Price: {amt-amt*0.1}")
elif amt>=10000:
    print(f"Price: {amt-amt*0.15}")
else:
    print(f"Price: {amt}")