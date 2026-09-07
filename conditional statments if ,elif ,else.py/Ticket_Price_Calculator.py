Age = int(input("Enter Your Age:"))
Gender = (input("Enter Your Gender:"))

if Age < 5 :
    Ticket_price = 0

elif Age < 5:
    Ticket_price = 50

elif Age <= 12:
    Ticket_price = 100

elif Age <= 59:
    Ticket_price = 60


# Female discount
if Gender == "female":
    discount = Ticket_price * 0.10
else:
    discount = 0

final_price = Ticket_price - discount

print("Original Ticket Price:", Ticket_price)
print("Discount:", discount)
print("Final Ticket Price:", final_price)
