Amount = float(input("Enter a Shopping Amount:"))

if Amount >= 5000:
    Discount = Amount * 0.20

elif Amount >= 3000:
    Discount = Amount * 0.15

elif Amount >= 1000:
    Discount= Amount * 0.10     

else:
     Discount = 0

Final_Amount = Amount - Discount

print("Shoping Amount:",Amount)
print("Discount:",Discount)
print("Total Amount", Final_Amount)