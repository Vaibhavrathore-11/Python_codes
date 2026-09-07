units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units! Units cannot be negative.")
elif units <= 100:
    total_bill = units * 5
elif units <= 200:
    
    total_bill = (100 * 5) + ((units - 100) * 7)
else:
    # First 100 at ₹5 + next 100 at ₹7 + above 200 at ₹10
    total_bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

if units >= 0:
    print(f"Total Bill: ₹{total_bill}")